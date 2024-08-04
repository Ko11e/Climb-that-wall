from django import forms
from .models import Profile, ContactUs


class ProfileForm(forms.ModelForm):
    """Form for user profile"""

    class Meta:
        model = Profile
        fields = ["profile_pic", "fav_climb", "bio"]

        labels = {
            "profile_pic": "Avatar",
            "bio": "Bio",
            "fav_climb": "Favorite Climbing type",
        }


class ContactUsForm(forms.ModelForm):
    """Form for user contact information"""

    class Meta:
        model = ContactUs
        fields = ["name", "question", "email", "message"]

        labels = {
            "name": "Name (First and Last)",
            "question": "What is your question about?",
            "email": "Email",
            "message": "Your message",
        }

        widget = {
            "message": forms.Textarea(attrs={"rows": 4}),
            "question": forms.Select(choices=ContactUs.QUESTION),
            "name": forms.TextInput(
                attrs={"placeholder": "First and Last Name"}
            ),
            "email": forms.EmailInput(
                attrs={"placeholder": "ex. first.lastname@mailadress.com"}
            ),
        }
