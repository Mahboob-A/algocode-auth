# django
# allauth
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

# dj rest auth
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model

# jwt
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# others
from django_countries.serializer_fields import CountryField
from phonenumber_field.serializerfields import PhoneNumberField

# drf
from rest_framework import serializers

from core_apps.profiles.models import Profile
from core_apps.profiles.serializers import UserDetailsProfileSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User"""

    profile_id = serializers.UUIDField(source="profile.id")
    gender = serializers.CharField(source="profile.gender")
    phone_number = PhoneNumberField(source="profile.phone_number")
    profile_photo = serializers.ReadOnlyField(source="profile.profile_photo.url")
    country = CountryField(source="profile.country")
    city = serializers.CharField(source="profile.city")
    twitter_handle = serializers.CharField(source="profile.twitter_handle")

    class Meta:
        model = User
        fields = [
            "id",
            "profile_id",
            "email",
            "first_name",
            "last_name",
            "gender",
            "phone_number",
            "profile_photo",
            "country",
            "city",
            "twitter_handle",
        ]

    def to_representation(self, instance):
        representation = super(UserSerializer, self).to_representation(instance)

        if instance.is_superuser:
            representation["admin"] = True
        return representation


class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def get_cleaned_data(self):
        super().get_cleaned_data()
        return {
            "username": self.validated_data.get("username", ""),
            "email": self.validated_data.get("email", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "last_name": self.validated_data.get("last_name", ""),
            "password1": self.validated_data.get("password1", ""),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user = adapter.save_user(request, user, self)

        user.save()

        setup_user_email(request, user, [])
        user.first_name = self.cleaned_data.get("first_name")
        user.last_name = self.cleaned_data.get("last_name")

        user.username = self.cleaned_data.get("username")
        user.email = self.cleaned_data.get("email")

        user.password = self.cleaned_data.get("password1")

        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Serializer class to include some other user info in the jwt claim."""

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # additional user details to the token payload
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["username"] = user.username
        token["email"] = user.email
        return token


class UserTokenSerializer(TokenObtainPairSerializer):
    """Serializer to pass data along with access and refresh toke. USER DATA is not encoded into access token."""

    user = serializers.SerializerMethodField()

    def get_user(self, user):
        return {
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
        }

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["user"] = self.get_user(self.user)
        return data
