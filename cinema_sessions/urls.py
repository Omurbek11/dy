from django.urls import path
from . import views

app_name = 'cinema_sessions'

urlpatterns = [
    path('schedule/', views.ScheduleView.as_view(), name='schedule'),
]