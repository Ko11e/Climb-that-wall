from django.views.generic import (
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import logout
from django.contrib import messages

from django.contrib.auth.models import User
from .models import Profile, ContactUs
from climb_gyms.models import ClimbingGyms, Comments

from .forms import ProfileForm, ContactUsForm


class ProfileView(TemplateView):
    """User profile view"""

    template_name = "profiles/profile.html"

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(user=self.kwargs["pk"])
        comments = Comments.objects.filter(user=self.kwargs["pk"])
        my_gyms = ClimbingGyms.objects.filter(user=self.kwargs["pk"])
        context = {
            "profile": profile,
            "comments": comments,
            "climbing_gyms": my_gyms,
            "form": ProfileForm(instance=profile),
        }

        return context


class EditProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Edit user profile view"""

    form_class = ProfileForm
    model = Profile

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user__id=self.kwargs["pk"])

    def form_valid(self, form):
        success_message = "Your profile has been updated."
        messages.info(self.request, success_message)
        self.success_url = f'/profiles/user/{self.kwargs["pk"]}/'
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user


class ConfirmDeleteProfileView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    """Confirm delete user profile view"""

    template_name = "profiles/delete_profile_confirm.html"

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(user=self.kwargs["pk"])
        context = {"profile": profile}

        return context

    def test_func(self):
        return self.request.user == Profile.objects.get(user=self.kwargs["pk"]).user


class DeleteProfileView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete user profile view"""

    model = User
    template_name = "profiles/profile_delete.html"
    success_url = "/"

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.kwargs["pk"])

    def form_valid(self, form):
        # Perform the deletion
        super().form_valid(form)
        # Log the user out
        logout(self.request)
        # Redirect to the success URL
        messages.error(
            self.request, "Your account has been deleted.\n We're sorry to see you go."
        )
        return redirect(self.get_success_url())

    def test_func(self):
        return self.request.user == self.get_object()


class CreateContactUsView(CreateView):
    """Create contact us view"""

    template_name = "home/contact_us.html"
    model = ContactUs
    form_class = ContactUsForm
    success_url = "thank-you/"

    def form_valid(self, form):
        if self.request.user:
            form.instance.user = self.request.user.username
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "There was an error with your form. Please try again."
        )
        return super().form_invalid(form)
