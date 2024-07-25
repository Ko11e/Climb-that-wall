from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404

from .models import Profile
from .forms import ProfileForm

class ProfileView(TemplateView):
    """ User profile view """
    template_name = 'profiles/profile.html'

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(user=self.kwargs['pk'])
        context = {
            'profile': profile,
            'form': ProfileForm(instance=profile)
        }

        return context
    
class EditProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Edit user profile view """
    form_class = ProfileForm
    model = Profile

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user__id=self.kwargs['pk'])

    def form_valid(self, form):
        self.success_url = f'/profiles/user/{self.kwargs["pk"]}/'
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user == self.get_object().user

    

