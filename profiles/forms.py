from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    """ Form for user profile """
    
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic', 'fav_climb']

        labels = {
            'profile_pic': 'Avatar',
            'bio': 'Bio',
            'fav_climb': 'Favorite Climbing type'
        }