from django.urls import path
from .views import Index, ThankYou
from profiles.views import CreateContactUsView

urlpatterns = [
    path('', Index.as_view() , name='home'),
    path('contact/', CreateContactUsView.as_view() , name='contactus'),
    path('contact/thank-you/', ThankYou.as_view() , name='thankyou'),
]