from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.ContactsView.as_view(), name='contacts'),
]