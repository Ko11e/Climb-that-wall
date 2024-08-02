from django.urls import path

# imported the views
from .views import (
    ClimbingGymsView,
    ClimbGymView,
    EditClimbingGymView,
    CreateCommentsView,
    EditCommentsView,
    create_climbing_gym,
    not_authorized_view,
)

urlpatterns = [
    path("search/", ClimbingGymsView.as_view(), name="search_gyms"),
    
    # Climbing gyms detail view
    path("<slug:slug>/", ClimbGymView.as_view(), name="gyms"),
    path("create-climbing-gym/", create_climbing_gym, name="create_climbing_gym"),
    
    # Edit climbing gym
    path("edit-gym/<int:pk>", EditClimbingGymView.as_view(), name="edit_climbing_gym"),
    
    # Comments
    path("comment/<int:pk>", CreateCommentsView.as_view(), name="create_comment"),
    path("comment/edit/<int:pk>", EditCommentsView.as_view(), name="edit_comment"),
    path("create-climbing-gym/not-authorized/", not_authorized_view, name="not_authorized"),
]