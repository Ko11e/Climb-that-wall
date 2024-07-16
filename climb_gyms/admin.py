from django.contrib import admin
from .models import ClimbingGyms, Comments, Ratings, Images, Socialmedia


class ClimbingGymsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'city',
        'created_at'
    )
    search_fields = ('name', 'city', 'country')


class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'body',
        'rating',
        'created_at'
    )
    search_fields = ('user', 'climbing_gym', 'rating')


class RatingsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'climbing_gym',
        'rating'
    )
    search_fields = ('user', 'climbing_gym', 'rating')


class ImagesAdmin(admin.ModelAdmin):
    list_display = (
        'headimage',
        'headimage_alt'
    )
    search_fields = ('headimage', 'headimage_alt')


class SocialmediaAdmin(admin.ModelAdmin):
    list_display = (
        'website',
        'facebook',
        'instagram',
        'other'
    )
    search_fields = ('website', 'facebook', 'instagram', 'other')



admin.site.register(ClimbingGyms)
admin.site.register(Comments)
admin.site.register(Ratings)
admin.site.register(Images)
admin.site.register(Socialmedia)
