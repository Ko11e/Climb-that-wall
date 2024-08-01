from django.views.generic import ListView, DetailView, UpdateView
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from django.db.models import Q
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect

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
        context['comment_count'] = context['comments'].count()
        return context


class CreateCommentsView(UserPassesTestMixin, LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        """ POST request to create a new comment """
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to add a comment.')
            return redirect('login')  # Redirect to login page if not authenticated

        # Retrieve the climbing gym instance
        climbing_gym = get_object_or_404(ClimbingGyms, pk=kwargs['pk'])
        
        # Check if the user has already commented on the gym
        existing_comments = Comments.objects.filter(climbing_gym=climbing_gym, user=request.user)
        if existing_comments.exists():
            messages.info(request, 'You have already commented on this gym./n If you want to change your comment, please delete/edit the previous one.')
            return redirect('gyms', slug=climbing_gym.slug)  # Adjust the URL pattern accordingly
        
        # Create a new comment instance
        try:
            new_rating= int(request.POST.get('rating'))
            comment = Comments(
                user=request.user,
                climbing_gym=climbing_gym,
                rating=new_rating,
                body=request.POST.get('body') or 'None'
            )
            comment.save()
            climbing_gym.average_rating() # Update the average rating of the gym
            messages.success(request, 'Your comment has been added.')

        except Exception as e:
            messages.error(request, f'An error occurred while adding your comment: {e}')
            return redirect('gyms', slug=climbing_gym.slug)
        
        
        return redirect('gyms', slug=climbing_gym.slug)
    
    def test_func(self):    
        return self.request.user.is_authenticated
    

class EditCommentsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ Edit comment view """
    model = Comments
    fields = ['rating', 'body']
    template_name = 'climb_gyms/edit_comment.html'
    success_url = '/'
    context_object_name = 'comment'

    def get_object(self, queryset=None):
        comment = get_object_or_404(Comments, pk=self.kwargs['pk'])
        comment.climbing_gym.average_rating()
        return comment

    
    def test_func(self):
        return self.request.user == self.get_object().user
