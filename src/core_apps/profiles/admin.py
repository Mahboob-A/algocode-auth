from django.contrib import admin

from core_apps.profiles.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "pkid",
        "id",
        "user",
        "twitter_handle",
        "gender",
        "phone_number",
        "country",
        "city",
    ]
    list_display_links = ["pkid", "id", "user"]
    list_filter = ["pkid", "id"]
