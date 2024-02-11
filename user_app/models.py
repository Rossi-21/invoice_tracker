from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, instance, created, **kwargs):
    # If a Profile is created
    if created:
        # Create a variable with the Profile that was just made
        user_profile = Profile(user=instance)
        # Save the Profile to the database
        user_profile.save()


# connect the profile to the User
post_save.connect(create_profile, sender=User)
