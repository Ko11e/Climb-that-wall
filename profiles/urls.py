from django.urls import path

from .views import ProfileView, EditProfileView, DeleteProfileView, ConfirmDeleteProfileView

urlpatterns = [
    path('user/<slug:pk>/', ProfileView.as_view(), name='profile'),
    path('edit/<slug:pk>/', EditProfileView.as_view(), name='edit_profile'),
    path('delete/<slug:pk>/', DeleteProfileView.as_view(), name='delete_profile'),
    path('delete/<slug:pk>/confirm/', ConfirmDeleteProfileView.as_view(), name='delete_profile_confirm'),
]