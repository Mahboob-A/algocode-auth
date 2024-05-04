from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core_apps.users.serializers import UserSerializer
from core_apps.users.renderers import UserJSONRenderer
from core_apps.common.utils import generate_full_url


User = get_user_model()


class CustomUserDetailsView(RetrieveUpdateAPIView):
    """API for authenticated user's details"""

    serializer_class = UserSerializer
    renderer_classes = [UserJSONRenderer]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user_id = self.kwargs.get("id", None)
        if user_id:
            try:
                return User.objects.get(id=user_id)
            except User.DoesNotExist:
                raise Http404(f"Profile with id {user_id} does not exist.")
        else:
            return self.request.user

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        profile_link = generate_full_url(request=request, instance=instance, instance_profile=True)
        user_link = generate_full_url(request=request, instance=instance)

        response_data = serializer.data
        response_data["links"] = {"self": profile_link, "user": user_link}
        return Response(response_data)


class CustomUserDetailsView2(APIView):
    """API for authenticated user's details"""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(
            {"status": "success", "data": serializer.data}, status=status.HTTP_200_OK
        )


from core_apps.users.serializers import CustomTokenObtainPairSerializer, UserTokenSerializer


class UserTokenObtainPairView(APIView):
    '''API to get access and refresh token.'''
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)
