from django.urls import path

# imported the views
from .views import (
    ClimbingGymsView,
    ClimbGymView,
    EditClimbingGymView,
    EditGymTextView,
    EditGymImagesView,
    EditSocialmediaView,
    DeleteClimbingGymView,
    CreateCommentsView,
    EditCommentsView,
    DeleteCommentsView,
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
    path(
        "edit-gym-text/<int:pk>", EditGymTextView.as_view(),
        name="edit_gym_text"
    ),
    path(
        "edit-gym-images/<int:pk>", EditGymImagesView.as_view(),
        name="edit_gym_images"
    ),
    path(
        "edit-gym-socialmedia/<int:pk>",
        EditSocialmediaView.as_view(),
        name="edit_gym_socialmedia",
    ),
    path(
        "delete-gym/<int:pk>",
        DeleteClimbingGymView.as_view(),
        name="delete_climbing_gym",
    ),
    
    # Comments
    path(
        "comment/<int:pk>", CreateCommentsView.as_view(),
        name="create_comment"
    ),
    path(
        "comment/edit/<int:pk>", EditCommentsView.as_view(),
        name="edit_comment"
    ),
    path(
        "comment/delete/<int:pk>",
        DeleteCommentsView.as_view(),
        name="delete_comment"
    ),
    path(
        "create-climbing-gym/not-authorized/",
        not_authorized_view,
        name="not_authorized",
    ),
]
