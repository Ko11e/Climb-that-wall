from django import forms
from .models import ClimbingGyms, Socialmedia, Images


class ClimbingGymsForm(forms.ModelForm):
    """Form for climbing gyms"""

    class Meta:
        model = ClimbingGyms
        fields = [
            "title",
            "slug",
            "city",
            "description",
            "maps",
        ]

        labels = {
            "title": "Name of the Climbing Gym",
            "slug": "Slug",
            "city": "City",
            "description": "Description (max 2000 characters)",
            "maps": "Map Coordinates",
        }


class SocialmediaForm(forms.ModelForm):
    """ Form for social media links """

    class Meta:
        model = Socialmedia
        fields = ['website', 'facebook', 'instagram', 'other']

        labels = {
            'website': 'Website Link',
            'facebook': 'Facebook Page',
            'instagram': 'Instagram Page',
            'other': 'Other',
        }


class ImagesForm(forms.ModelForm):
    """ Form for images """

    class Meta:
        model = Images
        fields = ['headimage', 'headimage_alt', 'image1', 'image2', 'image3', 'image_alt']

        labels = {
            'headimage': 'Main Image',
            'headimage_alt': 'Main Image Alt',
            'image1': 'Image 1 (Optional)',
            'image2': 'Image 2 (Optional)',
            'image3': 'Image 3 (Optional)',
            'image_alt': 'Small description for the extra three images',
        }
