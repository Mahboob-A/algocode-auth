from django.urls import path

from core_apps.users.views import CustomUserDetailsView

urlpatterns = [
    path("user-detail/", CustomUserDetailsView.as_view(), name="user-details"),
    path("user-detail/<uuid:id>/", CustomUserDetailsView.as_view(), name="user-details-id"),
]
