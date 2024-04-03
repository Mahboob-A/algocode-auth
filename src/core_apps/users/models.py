from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ 
from django.urls import reverse

import uuid 

from core_apps.users.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin): 
    ''' Custom User model '''
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    first_name = models.CharField(verbose_name=_('First Name'), max_length=35)
    last_name = models.CharField(verbose_name=_('Last Name'), max_length=35)
    email = models.EmailField(verbose_name=_('Email Address'), max_length=50, db_index=True, unique=True)

    is_active = models.BooleanField(verbose_name=_('Is Active'), default=True)
    is_staff = models.BooleanField(verbose_name=_('Is Staff'), default=False)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    class Meta: 
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    @property
    def get_full_name(self): 
        return f'{self.first_name.title()} {self.last_name.title()}'

    @property
    def get_short_name(self): 
        return f'{self.first_name.title()}'

    @property
    def get_email(self): 
        return self.email

    def __str__(self): 
        return f'USER: {self.first_name.title()} {self.last_name.title()}'

    def get_absolute_url(self):
        return reverse('user-details-id', kwargs={"id": self.id})