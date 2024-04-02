import logging 

from django.db.models.signals import post_save
from django.dispatch import receiver

from core_apps.profiles.models import Profile
from algocode_backend.settings.base import AUTH_USER_MODEL

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs): 
    if created: 
        Profile.objects.create(user=instance)
        logger.info("--- Message from 'create_user_profile' signal --- ")
        logger.info(f"{instance}'s Profile has been created!")
