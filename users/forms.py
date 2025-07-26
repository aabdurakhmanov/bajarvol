# users/forms.py
from django import forms
from django.contrib.auth import  authenticate
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox
from .models import CustomUser, UserProfile



class RegisterForm(forms.Form):
    # CustomUser fields
    email = forms.EmailField(label="Email")
    username = forms.CharField(label="Username", max_length=30)

    # UserProfile fields
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    country = forms.CharField(max_length=100, required=False)
    password = forms.CharField(widget=forms.PasswordInput)

    # CAPTCHA
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    def save(self, commit=True):
        # Foydalanuvchini yaratish
        user = CustomUser.objects.create_user(
            email=self.cleaned_data['email'],
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            is_active=False  # <<< MUHIM! Email tasdiqlangunga qadar aktiv bo‘lmaydi
        )
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()

        # UserProfile ni yaratish
        UserProfile.objects.create(
            user=user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            country=self.cleaned_data.get('country'),
            phone=self.cleaned_data.get('phone'),
        )

        return user


class CustomLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        user = authenticate(email=email, password=password)
        if not user:
            raise forms.ValidationError("Email yoki parol noto‘g‘ri")
        if not user.is_email_verified:
            raise forms.ValidationError("Email hali tasdiqlanmagan")
        cleaned_data['user'] = user
        return cleaned_data