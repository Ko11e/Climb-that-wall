from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Profile, ContactUs


@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):
    list_display = (
        'pk',
        'user',
        'bio',
        'fav_climb',
        'created_at')
    search_fields = ('user', 'bio', 'fav_climb', 'created_at')
    summer_note_fields = ('bio',)


@admin.register(ContactUs)
class ContactFormAdmin(SummernoteModelAdmin):
    list_display = (
        'user',
        'name',
        'email',
        'message',
        'answered',)
    search_fields = ('user', 'name', 'email', 'message')
    summer_note_fields = ('message',)
