from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Profile

class ProfileAdmin(SummernoteModelAdmin):
    list_display = (
        'pk',
        'user',
        'bio',
        'fav_climb',
        'created_at')
    search_fields = ('user', 'bio', 'fav_climb', 'created_at')
    summer_note_fields = ('bio',)

# Register your models here.
admin.site.register(Profile, ProfileAdmin)