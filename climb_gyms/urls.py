from django.urls import path

# imported the views
from .views import ClimbingGymsView, ClimbGymView, CreateCommentsView

urlpatterns = [
    path("search/", ClimbingGymsView.as_view(), name="search_gyms"),
    path("<slug:slug>/", ClimbGymView.as_view(), name="gyms"),
    path("comment/<int:pk>", CreateCommentsView.as_view() , name="create_comment"),
]
