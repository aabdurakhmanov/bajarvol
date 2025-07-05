# users/views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.tokens import default_token_generator
from django.http import JsonResponse
from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import UserSerializer


from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer


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
            user.is_active = True  # SMTP bo'lmasa, email tasdiqlashni vaqtincha o‘tkazib turamiz
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def contact_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        # Ma'lumotlar to'g'ri va captcha ham ishladi!
        return render(request, "users/success.html", {})
    return render(request, "users/contact.html", {"form": form})
