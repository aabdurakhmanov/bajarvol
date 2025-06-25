# users/utils.py
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.conf import settings


def send_confirmation_email(user):
    token = default_token_generator.make_token(user)
    uid = user.pk
    confirm_url = f"http://{settings.DOMAIN}/api/users/confirm-email/{uid}/{token}/"

    message = f"Assalomu alaykum {user.username},\n\nProfilingizni tasdiqlash uchun quyidagi havolani bosing:\n{confirm_url}"

    send_mail(
        subject='Emailni tasdiqlang',
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
    )
