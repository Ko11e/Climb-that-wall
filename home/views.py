from django.views.generic import ListView

from climb_gyms.models import ClimbingGyms

class Index(ListView):
    """ Home view """
    template_name = 'home/index.html'
    model = ClimbingGyms
    context_object_name = 'climbing_gyms'
    paginate_by = 3

    


