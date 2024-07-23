from django.urls import path

# imported the views
from .views import ClimbingGymsView, ClimbGymView

urlpatterns = [
    path("search/", ClimbingGymsView.as_view(), name="search_gyms"),
    path("<slug:slug>/", ClimbGymView.as_view(), name="gyms"),
]