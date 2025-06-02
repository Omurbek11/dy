from django.contrib import admin
from .models import Session

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('movie', 'date_time', 'language')
    list_filter = ('date_time', 'language')
    search_fields = ('movie__title',)
