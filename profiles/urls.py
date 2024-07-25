from django.urls import path

from .views import ProfileView, EditProfileView

urlpatterns = [
    path('user/<slug:pk>/', ProfileView.as_view(), name='profile'),
    path('edit/<slug:pk>/', EditProfileView.as_view(), name='edit_profile'),
]