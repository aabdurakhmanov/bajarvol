# users/urls.py
from django.urls import path
from .views import register_view, CustomLoginView
from .views import UserRegisterView, UserDetailView, confirm_email, CustomTokenObtainPairView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('register-form/', register_view, name='register_form'),  # FBV: oddiy form
    path('profile/', UserDetailView.as_view(), name='user-detail'),
    path('confirm-email/<int:uid>/<str:token>/', confirm_email, name='confirm-email'),
    path('login/', CustomLoginView.as_view(), name='user-login'),


]
