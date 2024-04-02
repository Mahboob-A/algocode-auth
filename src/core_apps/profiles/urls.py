from django.urls import path 
from core_apps.profiles.views import(
    ProfileDetailAPIView, ProfileListAPIView, ProfileUpdateAPIView
)

urlpatterns = [
    path("all-user-profiles/", ProfileListAPIView.as_view(), name="all-user-profiles"),
    path("profile/", ProfileDetailAPIView.as_view(), name="profile-details"),
    path("profile/<uuid:id>/", ProfileDetailAPIView.as_view(), name="profile-details-id"),
    path("profile/update/", ProfileUpdateAPIView.as_view(), name="profile-update"),
]
