from django.urls import path

# imported the views
from .views import ClimbingGymsView, ClimbGymView, CreateCommentsView, EditCommentsView

urlpatterns = [
    path("search/", ClimbingGymsView.as_view(), name="search_gyms"),
    path("<slug:slug>/", ClimbGymView.as_view(), name="gyms"),
    path("comment/<int:pk>", CreateCommentsView.as_view() , name="create_comment"),
    path("comment/edit/<int:pk>", EditCommentsView.as_view(), name="edit_comment"),
]
