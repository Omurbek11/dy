from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('afisha/', views.afisha_view, name='afisha'),
    path('sessions/', views.sessions_view, name='sessions'),
    path('coming_soon/', views.coming_soon_view, name='coming_soon'),
    path('about/', views.about_view, name='about'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('movie/<int:pk>/', views.movie_detail, name='movie_detail'),
    path('buy-ticket/<int:session_id>/', views.buy_ticket, name='buy-ticket'),
]