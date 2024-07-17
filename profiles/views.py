from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from .models import Profile
from .forms import ProfileForm

class ProfileView(TemplateView):
    """ User profile view """
    template_name = 'profiles/profile.html'

    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(user=self.kwargs['pk'])
        context = {
            'profile': profile
        }

        return context
    
class EditProfileView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Edit user profile view """
    from_class = ProfileForm
    model = Profile
    template_name = 'profiles/edit_profile.html'

    def from_valid(self, form):
        self.success_url = f'/profile/view/{self.kwargs["pk"]}/'
        return super().form_valid(form)
    
    def test_func(self):
        return self.request.user == self.get_object().user

    

