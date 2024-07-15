from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'bio',
        'fav_climb',
        'created_at')
    search_fields = ('user', 'bio', 'fav_climb')

# Register your models here.
admin.site.register(Profile, ProfileAdmin)