# users/urls.py
from django.urls import path
from .views import UserRegisterView, UserDetailView, confirm_email, CustomTokenObtainPairView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
    path('confirm-email/<int:uid>/<str:token>/', confirm_email, name='confirm-email'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
