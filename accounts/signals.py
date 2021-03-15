# To get user profile automatically created when a user is created
#The User model == The sender
#The django.dispatch receiver == receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import  User
from django.dispatch import receiver
from .models import Profile


# The decorator == tiering up created user and user profile(displayed automatically in navbar)
@receiver(post_save, sender=User)
def create_profile(sender, instance, created,  **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()