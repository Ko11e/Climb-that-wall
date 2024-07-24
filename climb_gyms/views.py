from django.views.generic import ListView, DetailView

from django.db.models import Q

from .models import ClimbingGyms, Comments

class ClimbingGymsView(ListView):
    """" Search view for the Climbing gyms """
    template_name = 'climb_gyms/climb-gyms.html'
    model = ClimbingGyms
    context_object_name = 'climbing_gyms'
    paginate_by = 5

    def get_queryset(self, **kwargs):
        """ Get queryset """
        query = self.request.GET.get('q')
        button_query = self.request.GET.get('button_query')
        reset_filter = self.request.GET.get('reset')
        filter_query = self.request.GET.get('filter')

        if query:
            climbing_gyms = self.model.objects.filter(
                Q(description__icontains=query) |
                Q(city__icontains=query)
            )
        elif button_query:
            climbing_gyms = self.model.objects.filter(
                Q(city__icontains=button_query)
            )
        elif reset_filter:
            climbing_gyms = self.model.objects.all()
        elif filter_query:
            if filter_query == 'rating':
                climbing_gyms = self.model.objects.all().order_by('-rating')
            elif filter_query == 'az':
                climbing_gyms = self.model.objects.all().order_by('title')
            elif filter_query == 'za':
                climbing_gyms = self.model.objects.all().order_by('-title')

        else:
            climbing_gyms = self.model.objects.all()

        return climbing_gyms
    
class ClimbGymView(DetailView):
    """"  gym view """
    template_name = 'climb_gyms/gym.html'
    model = ClimbingGyms
    context_object_name = "gym"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comments.objects.filter(climbing_gym=self.get_object())
        return context