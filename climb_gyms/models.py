from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.db.models import Avg

# import the User model

# Create your models here.

class Images(models.Model):
    """ Model for user images """
    headimage = ResizedImageField(
        size=[300, 300], 
        quality=75, 
        upload_to='climbing-gyms/',
        force_format="WEBP", 
        blank=False, null=False
    )
    headimage_alt = models.CharField(
        max_length=100,
        help_text="Enter a breif text for the head image",
        blank=False,
        null=False
    )
    image1 = ResizedImageField(
        size=[300, 300], 
        quality=75, 
        upload_to='climbing-gyms/',
        force_format="WEBP", 
        blank=True, null=True
    )
    image2 = ResizedImageField(
        size=[300, 300], 
        quality=75, 
        upload_to='climbing-gyms/',
        force_format="WEBP", 
        blank=True, null=True
    )
    image3 = ResizedImageField(
        size=[300, 300], 
        quality=75, 
        upload_to='climbing-gyms/',
        force_format="WEBP", 
        blank=True, null=True
    )
    image_alt = models.CharField(
        max_length=100,
        help_text="Enter a breif text for the three images",
        default="image of climbing hall",
        blank=True,
        null=True)

    def __str__(self):
        return self.headimage_alt
    
class Socialmedia(models.Model):
    """ Model for social media links """
    website = models.URLField(max_length=200, blank=True, null=True)
    facebook = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    other = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.website


class ClimbingGyms(models.Model):
    """ Modle for climbing gyms """
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=2000, blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    maps = models.CharField(max_length=100, blank=False, null=False)
    images = models.ForeignKey(Images, on_delete=models.CASCADE)
    rating = models.FloatField(blank=True, null=True, default=0)
    socialmedia = models.ForeignKey(Socialmedia, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def average_rating(self) -> float:
        """ Get the average rating of the gym """
        self.rating = Ratings.objects.filter(climbing_gym=self).aggregate(Avg("rating"))["rating__avg"] or 0
        number_of_ratings = Ratings.objects.filter(climbing_gym=self).count()

        return self.rating, number_of_ratings

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title


class Ratings(models.Model):
    """ Model for ratings """
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    climbing_gym = models.ForeignKey(ClimbingGyms, on_delete=models.CASCADE, blank=False, null=False)
    rating = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.rating} by {self.user.username}"


class Comments(models.Model):
    """ Model for comments """
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    climbing_gym = models.ForeignKey(ClimbingGyms, on_delete=models.CASCADE, blank=False, null=False)
    body = models.TextField(max_length=2000, blank=True, null=True)
    rating = models.ForeignKey(Ratings, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.body} by {self.user.username}"
   
