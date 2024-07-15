from django.db import models
from djrichtextfield.models import RichTextField

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_resized import ResizedImageField

class Profile(models.Model):
    """" Model for user profile """
    TYPE_OF_CLIMBS = (
        (0, 'Boulder'), (1, 'Lead'),
        (2, 'Speed'), (3, 'Outdoors')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = RichTextField(max_length=2000, blank=True, null=True)
    profile_pic = ResizedImageField(
        size=[300, 300], 
        quality=75, 
        upload_to='profile_pics/',
        force_format="WEBP", 
        blank=True, null=True
    )
    fav_climb = models.IntegerField(choices=TYPE_OF_CLIMBS, default=0)
    #comments = models.ForeigeKey(Comments, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """ Create a user profile when a new user is created """
    if created:
        Profile.objects.create(user=instance)