from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django.urls import reverse, reverse_lazy

from phonenumber_field.modelfields import PhoneNumberField

from core_apps.common.models import TimeStampModel

User = get_user_model()


class Profile(TimeStampModel):
    """Model to store individual user info data. Signal is used to create a profile instance. core_apps.profiles.signals"""

    class Gender(models.TextChoices):
        MALE = ("M", _("Male"))
        FEMALE = ("F", _("Female"))
        OTHER = ("O", _("Other"))

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_photo = models.ImageField(
        verbose_name=_("Profile Photo"),
        upload_to="CustomUsers/ProfilePictures/",
        default="CustomUsers/default-user-image.jpg",
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=Gender.choices,
        default=Gender.MALE,
        max_length=1,
    )
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"), max_length=20, default="+918513998991"
    )

    about_me = models.TextField(
        verbose_name=_("About Me"), default="Say something about yourself"
    )

    country = CountryField(verbose_name=_("Country"), default="", blank=True)
    city = models.CharField(
        verbose_name=_("City"), max_length=30, default="", blank=True
    )

    twitter_handle = models.CharField(
        verbose_name=_("Twitter/X Handle"), max_length=25, blank=True, default=""
    )

    def __str__(self):
        return f"{self.user.get_full_name()}'s Profile"

    def get_absolute_url(self):
        return reverse('profile-details-id', kwargs={"id": self.id})
