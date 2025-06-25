# users/serializers.py
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from .models import CustomUser, UserProfile

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'birth_date', 'country', 'phone', 'avatar']

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'password', 'profile']
        read_only_fields = ['id']

    def validate_email(self, value):
        if not value.endswith('@gmail.com'):
            raise serializers.ValidationError("Faqat @gmail.com emailga ruxsat berilgan.")
        return value

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')

        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()

        UserProfile.objects.filter(user=user).update(**profile_data)

        # Tasdiqlovchi email yuboramiz
        from .utils import send_confirmation_email
        send_confirmation_email(user)

        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if profile_data:
            profile = instance.profile
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()
        return instance



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        if not self.user.is_email_verified:
            raise AuthenticationFailed("Email hali tasdiqlanmagan.")

        return data
