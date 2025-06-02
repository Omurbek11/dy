from django.views.generic import ListView
from .models import Session
from django.utils import timezone

class ScheduleView(ListView):
    model = Session
    template_name = 'cinema_sessions/schedule.html'
    context_object_name = 'sessions'

    def get_queryset(self):
        queryset = Session.objects.all()
        date = self.request.GET.get('date')
        if date:
            queryset = queryset.filter(date_time__date=date)
        return queryset.order_by('date_time')
