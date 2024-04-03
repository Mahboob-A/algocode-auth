# django
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.http import Http404

# drf
from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# local
from core_apps.profiles.models import Profile
from core_apps.profiles.paginations import ProfilePageNumberPagination
from core_apps.profiles.serializers import (
    ProfileSerializer,
    ProfileUpdateSerializer,
    UserDetailsProfileSerializer,
)
from core_apps.profiles.renderers import ProfileJSONRenderer, MultiProfileJSONRenderer
from core_apps.common.utils import generate_full_url

User = get_user_model()


class ProfileListAPIView(generics.ListAPIView):
    """API for listing all the user profiles."""

    queryset = Profile.objects.all()
    pagination_class = ProfilePageNumberPagination
    serializer_class = ProfileSerializer
    renderer_classes = [MultiProfileJSONRenderer]


class ProfileDetailAPIView(generics.RetrieveAPIView):
    """API for user profile details."""

    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    renderer_classes = [ProfileJSONRenderer]

    def get_object(self):
        profile_id = self.kwargs.get("id", None)
        if profile_id:
            try:
                return Profile.objects.get(id=profile_id)
            except Profile.DoesNotExist:
                raise Http404(f"Profile with id {profile_id} does not exist.")
        else:
            return self.request.user.profile
        
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        
        profile_link = generate_full_url(request=request, instance=instance)
        user_link = generate_full_url(request=request, instance=instance, instance_user=True)
        
        response_data = serializer.data
        response_data["links"] = {
            "self": profile_link, 
            "user": user_link
        }
        return Response(response_data) 


class ProfileUpdateAPIView(generics.UpdateAPIView):
    """API for updating user profile."""

    serializer_class = ProfileUpdateSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]
    renderer_classes = [ProfileJSONRenderer]

    def get_object(self):
        return self.request.user.profile

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        is_partial = True if request.method == "PATCH" else False
        print('is partial: ', is_partial)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=True if request.method == "PATCH" else False,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Construct HATEOAS links
        # profile_link = reverse('profile-details', kwargs={'id':instance.id})
        # user_link = reverse('user-details', kwargs=({'id':instance.user.id}))

        profile_link = generate_full_url(request=request, instance=instance)
        user_link = generate_full_url(request=request, instance=instance, instance_user=True)

        response_data = serializer.data
        response_data["links"] = {
            "self": profile_link, 
            "user": user_link
        }
        return Response(response_data)
