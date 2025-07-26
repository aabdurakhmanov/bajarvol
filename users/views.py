# users/views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm, CustomLoginForm
from django.views.generic import FormView
from django.contrib.auth import login
from django.contrib.auth.tokens import default_token_generator
from django.http import JsonResponse
from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from .utils import send_confirmation_email


class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserDetailView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user



def confirm_email(request, uid, token):
    try:
        user = CustomUser.objects.get(pk=uid)
    except CustomUser.DoesNotExist:
        return JsonResponse({'detail': 'Foydalanuvchi topilmadi.'}, status=404)

    if default_token_generator.check_token(user, token):
        user.is_email_verified = True
        user.is_active = True  # <<< MUHIM QATOR!
        user.save()
        return JsonResponse({'detail': 'Email muvaffaqiyatli tasdiqlandi.'})
    else:
        return JsonResponse({'detail': 'Token noto‘g‘ri yoki eskirgan.'}, status=400)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.is_active = False  # Email tasdiqlanmaguncha aktiv emas
            user.save()  # MUHIM! PK va token ishlashi uchun kerak
            send_confirmation_email(user)  # Endi bu ishlaydi
            return JsonResponse({'detail': 'Emailingizga tasdiqlovchi link yuborildi.'})
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})



class CustomLoginView(FormView):
    template_name = 'users/login.html'
    form_class = CustomLoginForm

    def form_valid(self, form):
        user = form.cleaned_data['user']
        login(self.request, user)

        # Token yaratish
        refresh = RefreshToken.for_user(user)
        response = redirect('user-detail')  # profile page nomi
        response.set_cookie('access', str(refresh.access_token), httponly=True)
        response.set_cookie('refresh', str(refresh), httponly=True)
        return response
