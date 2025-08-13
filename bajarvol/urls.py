from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenBlacklistView
)
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    #captcha
    #apps
    path('api/users/', include('apps.users.urls')),
    path('api/tasks/', include('apps.tasks.urls')),

    #jwt
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # refresh
    path('api/logout/', TokenObtainPairView.as_view(), name='token_blacklist'),
]

urlpatterns += [
    #docs
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'), # OpenAPI schema json uchun
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'), # Swagger UI
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),     # ReDoc UI

]