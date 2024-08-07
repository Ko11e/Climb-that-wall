from django.views.generic import (
    ListView,
    TemplateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.db.models import Q
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import user_passes_test

from .models import ClimbingGyms, Images, Socialmedia, Comments
from .forms import ClimbingGymsForm, SocialmediaForm, ImagesForm


def is_staff(user):
    return user.is_staff


def not_authorized_view(request):
    return render(request, "climb_gyms/not-authorized.html")


class ClimbingGymsView(ListView):
    """ " Search view for the Climbing gyms"""

    template_name = "climb_gyms/climb-gyms.html"
    model = ClimbingGyms
    context_object_name = "climbing_gyms"
    paginate_by = 3

    def get_queryset(self, **kwargs):
        """Get queryset"""
        query = self.request.GET.get("q")
        button_query = self.request.GET.get("button_query")
        reset_filter = self.request.GET.get("reset")
        filter_query = self.request.GET.get("filter")

        if query:
            climbing_gyms = self.model.objects.filter(
                Q(description__icontains=query) | Q(city__icontains=query)
            )

        elif button_query:
            climbing_gyms = self.model.objects.filter(
                Q(city__icontains=button_query)
            )

        elif reset_filter:
            climbing_gyms = self.model.objects.all()

        elif filter_query:
            if filter_query == "rating":
                climbing_gyms = self.model.objects.all().order_by("-rating")
            elif filter_query == "az":
                climbing_gyms = self.model.objects.all().order_by("title")
            elif filter_query == "za":
                climbing_gyms = self.model.objects.all().order_by("-title")

        else:
            climbing_gyms = self.model.objects.all()

        return climbing_gyms


class ClimbGymView(DetailView):
    """ "  gym view"""

    template_name = "climb_gyms/gym.html"
    model = ClimbingGyms
    context_object_name = "gym"

    def get_context_data(self, **kwargs):
        climbing_gym = ClimbingGyms.objects.get(slug=self.kwargs["slug"])
        climbing_gym.average_rating()
        context = super().get_context_data(**kwargs)
        context["comments"] = Comments.objects.filter(
            climbing_gym=self.get_object()
        )
        context["comment_count"] = context["comments"].count()

        return context


@user_passes_test(is_staff, login_url="not_authorized")
def create_climbing_gym(request):

    if request.method == "POST":
        climbing_gym_form = ClimbingGymsForm(request.POST)
        socialmedia_form = SocialmediaForm(request.POST)
        images_form = ImagesForm(request.POST, request.FILES)

        if (
            climbing_gym_form.is_valid()
            and socialmedia_form.is_valid()
            and images_form.is_valid()
        ):
            climbing_gym = climbing_gym_form.save(commit=False)
            climbing_gym.user = request.user  # Set the active user

            socialmedia = socialmedia_form.save(commit=False)
            socialmedia.gym = climbing_gym
            socialmedia.save()

            images = images_form.save(commit=False)
            images.gym = climbing_gym
            images.save()

            climbing_gym.socialmedia = socialmedia
            climbing_gym.images = images
            climbing_gym.save()

            messages.success(request, "Your climbing gym has been added.")
            return redirect("gyms", slug=climbing_gym.slug)

    else:
        climbing_gym_form = ClimbingGymsForm()
        socialmedia_form = SocialmediaForm()
        images_form = ImagesForm()

    context = {
        "climbing_gym_form": climbing_gym_form,
        "socialmedia_form": socialmedia_form,
        "images_form": images_form,
    }

    return render(request, "climb_gyms/create_climbinggym.html", context)


class EditClimbingGymView(
    LoginRequiredMixin, UserPassesTestMixin, TemplateView
):
    """Veiw the Edit sections climbing gym view"""

    template_name = "climb_gyms/edit_climbinggym.html"

    def get_context_data(self, **kwargs):
        climbing_gym = ClimbingGyms.objects.get(id=self.kwargs["pk"])
        social_media = climbing_gym.socialmedia
        images = climbing_gym.images
        context = {
            "gym": climbing_gym,
            "social_media": social_media,
            "images": images,
            "climbing_gym_form": ClimbingGymsForm(instance=climbing_gym),
            "socialmedia_form": SocialmediaForm(instance=social_media),
            "images_form": ImagesForm(instance=images),
        }

        return context

    def test_func(self):
        return self.request.user == ClimbingGyms.objects.get(
            id=self.kwargs["pk"]
        ).user


class EditGymTextView(LoginRequiredMixin, UpdateView):
    """Edit the text information of the climbing gym"""

    model = ClimbingGyms
    form_class = ClimbingGymsForm

    def get_object(self, queryset=None):
        return get_object_or_404(ClimbingGyms, pk=self.kwargs["pk"])

    def form_valid(self, form):
        form.instance.user = self.request.user
        self.success_url = f"/climb_gyms/{form.instance.slug}"

        messages.info(
            self.request,
            "The text in Your climbing gym has been updated."
        )
        return super().form_valid(form)


class EditGymImagesView(LoginRequiredMixin, UpdateView):
    """Edit the images of the climbing gym"""

    model = Images
    form_class = ImagesForm

    def get_object(self, queryset=None):
        return get_object_or_404(Images, pk=self.kwargs["pk"])

    def form_valid(self, form):
        images = Images.objects.get(pk=self.kwargs["pk"])
        form.instance.gym = images.images
        self.success_url = f"/climb_gyms/{images.images.slug}"

        messages.info(
            self.request,
            "The images in Your climbing gym has been updated."
        )
        return super().form_valid(form)


class EditSocialmediaView(LoginRequiredMixin, UpdateView):
    """Edit the social media links of the climbing gym"""

    model = Socialmedia
    form_class = SocialmediaForm

    def get_object(self, queryset=None):
        return get_object_or_404(Socialmedia, pk=self.kwargs["pk"])

    def form_valid(self, form):
        socialmedia = Socialmedia.objects.get(pk=self.kwargs["pk"])
        form.instance.gym = socialmedia.socialmedia
        self.success_url = f"/climb_gyms/{socialmedia.socialmedia.slug}"

        messages.info(
            self.request,
            "The social media links in Your climbing gym has been updated.",
        )
        return super().form_valid(form)


class DeleteClimbingGymView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView
):
    """Delete climbing gym view"""

    model = ClimbingGyms
    template_name = "climb_gyms/delete_climbinggym.html"
    success_url = "climb_gyms/search/"
    context_object_name = "gym"
    success_message = "Your climbing gym has been deleted."

    def test_func(self):
        return self.request.user == self.get_object().user

    def handle_no_permission(self):
        # Handle what happens if the user does not pass the test
        if self.request.user.is_authenticated:
            messages.error(
                self.request,
                "You are not authorized to delete this climbing gym."
            )
            return redirect(
                "search"
            )  # Redirect to item list if authenticated but does not pass test
        else:
            messages.error(
                self.request,
                "You must be logged in to delete a climbing gym."
            )
            return redirect("login")


class CreateCommentsView(UserPassesTestMixin, LoginRequiredMixin, View):
    """Create comment view"""

    def post(self, request, *args, **kwargs):
        """POST request to create a new comment"""
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to add a review.")
            return redirect("login")
        # Redirect to login page if not authenticated

        # Retrieve the climbing gym instance
        climbing_gym = get_object_or_404(ClimbingGyms, pk=kwargs["pk"])

        # Check if the user has already commented on the gym
        existing_comments = Comments.objects.filter(
            climbing_gym=climbing_gym, user=request.user
        )
        if existing_comments.exists():
            messages.info(
                request,
                f"You have already commented on this gym."
            )
            return redirect(
                "gyms", slug=climbing_gym.slug
            )  # Adjust the URL pattern accordingly

        # Create a new comment instance
        try:
            new_rating = int(request.POST.get("rating"))
            comment = Comments(
                user=request.user,
                climbing_gym=climbing_gym,
                rating=new_rating,
                body=request.POST.get("body") or "None",
            )
            comment.save()
            climbing_gym.average_rating()  # Update the average rating
            messages.success(request, "Your comment has been added.")

        except Exception as e:
            messages.error(request,
                           f"An error occurred while adding your review.\n Did you forgot to enter your ranking"
                           )
            return redirect("gyms", slug=climbing_gym.slug)

        return redirect("gyms", slug=climbing_gym.slug)

    def test_func(self):
        return self.request.user.is_authenticated


class EditCommentsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit comment view"""

    model = Comments
    fields = ["rating", "body"]
    template_name = "climb_gyms/edit_comment.html"
    context_object_name = "comment"

    def get_object(self, queryset=None):
        comment = get_object_or_404(Comments, pk=self.kwargs["pk"])
        comment.climbing_gym.average_rating()
        return comment

    def form_valid(self, form):
        comment = get_object_or_404(Comments, pk=self.kwargs["pk"])
        messages.info(self.request, f"Your comment has been updated.")
        comment.climbing_gym.average_rating()
        return super().form_valid(form)
    
    def get_success_url(self):
        climbing_gym = get_object_or_404(
            Comments, pk=self.kwargs["pk"]
        ).climbing_gym
        return reverse("gyms", kwargs={"slug": climbing_gym.slug})

    def test_func(self):
        return self.request.user == self.get_object().user


class DeleteCommentsView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView
):
    """Delete comment view"""

    model = Comments
    template_name = "climb_gyms/delete-comment.html"
    context_object_name = "comment"
    success_message = "Your comment has been deleted."

    def get_success_url(self):
        climbing_gym = get_object_or_404(
            Comments, pk=self.kwargs["pk"]
        ).climbing_gym
        return reverse("gyms", kwargs={"slug": climbing_gym.slug})

    def test_func(self):
        return self.request.user == self.get_object().user

    def handle_no_permission(self):
        # Handle what happens if the user does not pass the test
        if self.request.user.is_authenticated:
            messages.error(
                self.request,
                "You are not authorized to delete this comment."
            )
            return redirect("profile", pk=self.request.user.id)
        else:
            messages.error(self.request,
                           "You must be logged in to delete a comment.")
            return redirect("login")
