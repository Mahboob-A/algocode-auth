from dj_rest_auth import registration, urls
from dj_rest_auth.views import PasswordResetConfirmView
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf.urls.static import static

from core_apps.users.views import CustomUserDetailsView, CustomUserDetailsView2

# documentation
doc_schema_view = get_schema_view(
    openapi.Info(
        title="Algocode Backend API",
        default_version="v1.0",
        description="API Endpoints for Algocode Backend",
        contact=openapi.Contact(email="iammahboob.a@gmail.com"),
        license=openapi.License(name="GPL-3.0 Licence"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # admin
    path(settings.ADMIN_URL, admin.site.urls),
    # doc
    path("redoc/", doc_schema_view.with_ui("redoc", cache_timeout=0)),
    # Registration and Password reset urls | V1
    path("api/v1/auth/", include("dj_rest_auth.urls")),
    path("api/v1/auth/registration/", include("dj_rest_auth.registration.urls")),
    path(
        "api/v1/auth/password/reset/confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    # users app
    path(
        "api/v1/user/",
        include("core_apps.users.urls"),
    ),
    # profile app
    path("api/v1/profiles/", include("core_apps.profiles.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Algocode Auth Service"
admin.site.site_title = "Algocode Auth Service Admin Portal"
admin.site.index_title = "Welcome to Algocode Auth Service Portal"
