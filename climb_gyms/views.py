from django.views.generic import ListView

from .models import ClimbingGyms

class ClimbingGymsView(ListView):
    """" Climbing gyms view """
    template_name = 'climb_gyms/climb-gyms.html'
    model = ClimbingGyms
    context_object_name = 'climbing_gyms'
    paginate_by = 5