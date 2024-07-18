from django.urls import path

from .views import ClimbingGymsView

urlpatterns = [
    path("search/", ClimbingGymsView.as_view(), name="search_gyms"),
    # path("/<title>", ClimbGymView.as_view(), name="gyms"),
]