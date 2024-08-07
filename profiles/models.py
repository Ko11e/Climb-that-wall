from django.db import models

from django.contrib.auth.models import User
from climb_gyms.models import Comments
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_resized import ResizedImageField


class Profile(models.Model):
    """ " Model for user profile"""

    TYPE_OF_CLIMBS = (
        ("Boulder", "boulder"),
        ("Lead", "lead"),
        ("Speed", "speed"),
        ("Outdoors", "outdoors"),
    )
    user = models.OneToOneField(
        User, related_name="profile", on_delete=models.CASCADE
    )
    bio = models.TextField(max_length=2000, blank=True, null=True)
    profile_pic = ResizedImageField(
        size=[300, 300],
        quality=75,
        upload_to="profile_pics/",
        force_format="WEBP",
        blank=True,
        null=True,
    )
    fav_climb = models.CharField(choices=TYPE_OF_CLIMBS, default="null")
    comments = models.ForeignKey(
        Comments, on_delete=models.CASCADE, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """Create a user profile when a new user is created"""
    if created:
        Profile.objects.create(user=instance)


class ContactUs(models.Model):
    """Model for user contact information
    An instance of this model is created when
    a user sends a message to the site admin
    """

    QUESTION = [
        ("General", "General"),
        ("Bug", "Bug"),
        ("Staff Request", "Staff Request"),
        ("Other", "Other"),
    ]
    user = models.CharField(max_length=75, blank=False, null=False)
    name = models.CharField(max_length=75, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    question = models.CharField(choices=QUESTION, default="General")
    message = models.TextField(max_length=500, blank=True, null=True)
    answered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username, self.email
