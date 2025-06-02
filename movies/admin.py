from django.contrib import admin
from .models import Movie, ComingSoon, TheaterPhoto

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'duration', 'age_rating')
    list_filter = ('genre', 'age_rating')
    search_fields = ('title',)

@admin.register(ComingSoon)
class ComingSoonAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date')
    list_filter = ('release_date',)
    search_fields = ('title',)

@admin.register(TheaterPhoto)
class TheaterPhotoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('caption',)