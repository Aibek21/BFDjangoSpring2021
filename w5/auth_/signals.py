from django.db.models.signals import post_save
from django.dispatch import receiver
from auth_.models import MainUser, Profile


@receiver(post_save, sender=MainUser)
def user_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
