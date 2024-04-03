from django import forms
from django.contrib.auth import forms as forms_handler
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreationForm(forms_handler.UserCreationForm):
    class Meta(forms_handler.UserCreationForm):
        model = User
        fields = ["first_name", "last_name", "email"]

    error_messages = {
        "email_exists": "User with this email already existis!",
    }

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise forms_handler.ValidationError(self.error_messages["email_exists"])


class UserChangeForm(forms_handler.UserChangeForm):
    class Meta(forms_handler.UserChangeForm):
        model = User
        fields = [
            "first_name",
            "last_name",
        ]
