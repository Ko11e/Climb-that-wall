from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from django.db.models import Avg


class Images(models.Model):
    """Model for user images"""

    headimage = ResizedImageField(
        size=[600, 300],
        quality=75,
        upload_to="climbing-gyms/",
        force_format="WEBP",
        help_text="This will be the front image of the climbing gym",
        blank=False,
        null=False,
    )
    headimage_alt = models.CharField(
        max_length=100,
        help_text="Enter a breif text for the head image",
        blank=False,
        null=False,
    )
    image1 = ResizedImageField(
        size=[600, 300],
        quality=75,
        upload_to="climbing-gyms/",
        force_format="WEBP",
        blank=True,
        null=True,
    )
    image2 = ResizedImageField(
        size=[600, 300],
        quality=75,
        upload_to="climbing-gyms/",
        force_format="WEBP",
        blank=True,
        null=True,
    )
    image3 = ResizedImageField(
        size=[600, 300],
        quality=75,
        upload_to="climbing-gyms/",
        force_format="WEBP",
        blank=True,
        null=True,
    )
    image_alt = models.CharField(
        max_length=100,
        help_text="Enter a breif text for the three images",
        default="image of climbing hall",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.headimage_alt


class Socialmedia(models.Model):
    """Model for social media links"""

    website = models.URLField(
        max_length=200,
        help_text="example: https://www.your-website.com",
        blank=True,
        null=True,
    )
    facebook = models.URLField(
        max_length=200,
        help_text="example: https://www.facebook.com/your-page",
        blank=True,
        null=True,
    )
    instagram = models.URLField(
        max_length=200,
        help_text="example: https://www.instagram.com/your-page",
        blank=True,
        null=True,
    )
    other = models.URLField(
        max_length=200,
        help_text="Other links where people can find more information",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.website


class ClimbingGyms(models.Model):
    """Modle for climbing gyms"""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, null=False
    )
    title = models.CharField(max_length=100, blank=False, null=False)
    slug = models.SlugField(
        max_length=100,
        help_text="Slug (example: name-of-the-gym)",
        blank=False,
        null=False,
    )
    description = models.TextField(max_length=2000, blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    maps = models.CharField(
        max_length=100,
        help_text="ex. 59°25'15.7" + '"N 17°54' + "'58.3" + '"E"',
        blank=False,
        null=False,
    )
    images = models.OneToOneField(
        Images, related_name="images", on_delete=models.CASCADE
    )
    rating = models.FloatField(blank=True, null=True, default=0)
    socialmedia = models.OneToOneField(
        Socialmedia, related_name="socialmedia", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def average_rating(self) -> float:
        """Get the average rating of the gym"""
        comments = Comments.objects.filter(climbing_gym=self)
        self.rating = (
            comments.aggregate(Avg("rating"))[
                "rating__avg"
            ]
            or 0
        )
        self.save()

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.title


class Ratings(models.Model):
    """Model for ratings"""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, null=False
    )
    climbing_gym = models.ForeignKey(
        ClimbingGyms, on_delete=models.CASCADE, blank=False, null=False
    )
    rating = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return f"{self.rating} by {self.user.username}"


class Comments(models.Model):
    """Model for comments"""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False, null=False
    )
    climbing_gym = models.ForeignKey(
        ClimbingGyms, on_delete=models.CASCADE, blank=False, null=False
    )
    body = models.TextField(max_length=2000, blank=True, null=True)
    rating = models.IntegerField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.body} by {self.user.username}"
