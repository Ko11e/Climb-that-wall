from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    """ Form for user profile """
    
    class Meta:
        model = Profile
        fields = ['profile_pic', 'fav_climb', 'bio']

        labels = {
            'profile_pic': 'Avatar',
            'bio': 'Bio',
            'fav_climb': 'Favorite Climbing type'
        }