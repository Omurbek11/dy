from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Movie, ComingSoon, TheaterPhoto
from cinema_sessions.models import Session
from datetime import datetime
from django.core.paginator import Paginator

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.all()
        return context

def afisha_view(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 6)  # 6 фильмов на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'afisha.html', {'page_obj': page_obj})

def sessions_view(request):
    movie_id = request.GET.get('movie')
    date_str = request.GET.get('date')
    sessions = Session.objects.all()
    if movie_id:
        sessions = sessions.filter(movie_id=movie_id)
    if date_str:
        try:
            selected_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            sessions = sessions.filter(date_time__date=selected_date)
        except ValueError:
            pass
    return render(request, 'sessions.html', {'sessions': sessions})

def coming_soon_view(request):
    coming_soon = ComingSoon.objects.all()
    return render(request, 'coming_soon.html', {'coming_soon': coming_soon})

def about_view(request):
    photos = TheaterPhoto.objects.all()
    return render(request, 'about.html', {'photos': photos})

def contacts_view(request):
    return render(request, 'contacts.html')

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movie_detail.html', {'movie': movie})
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Movie, ComingSoon, TheaterPhoto
from cinema_sessions.models import Session
from datetime import datetime
from django.core.paginator import Paginator

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.all()
        return context

def afisha_view(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 6)  # 6 фильмов на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'afisha.html', {'page_obj': page_obj})

def sessions_view(request):
    movie_id = request.GET.get('movie')
    date_str = request.GET.get('date')
    sessions = Session.objects.all()
    if movie_id:
        sessions = sessions.filter(movie_id=movie_id)
    if date_str:
        try:
            selected_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            sessions = sessions.filter(date_time__date=selected_date)
        except ValueError:
            pass
    return render(request, 'sessions.html', {'sessions': sessions})

def coming_soon_view(request):
    coming_soon = ComingSoon.objects.all()
    return render(request, 'coming_soon.html', {'coming_soon': coming_soon})

def about_view(request):
    photos = TheaterPhoto.objects.all()
    return render(request, 'about.html', {'photos': photos})

def contacts_view(request):
    return render(request, 'contacts.html')

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movie_detail.html', {'movie': movie})

from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Movie, ComingSoon, TheaterPhoto
from cinema_sessions.models import Session
from datetime import datetime
from django.core.paginator import Paginator

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = Movie.objects.all()
        return context

def afisha_view(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 6)  # 6 фильмов на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'afisha.html', {'page_obj': page_obj})

def sessions_view(request):
    movie_id = request.GET.get('movie')
    date_str = request.GET.get('date')
    sessions = Session.objects.all()
    if movie_id:
        sessions = sessions.filter(movie_id=movie_id)
    if date_str:
        try:
            selected_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            sessions = sessions.filter(date_time__date=selected_date)
        except ValueError:
            pass
    return render(request, 'sessions.html', {'sessions': sessions})

def coming_soon_view(request):
    coming_soon = ComingSoon.objects.all()
    return render(request, 'coming_soon.html', {'coming_soon': coming_soon})

def about_view(request):
    photos = TheaterPhoto.objects.all()
    return render(request, 'about.html', {'photos': photos})

def contacts_view(request):
    return render(request, 'contacts.html')

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movie_detail.html', {'movie': movie})

def buy_ticket(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    return render(request, 'buy_ticket.html', {'session': session})
