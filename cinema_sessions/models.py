from django.db import models
from movies.models import Movie

class Session(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    hall = models.CharField(max_length=50, default="Зал 1")
    date_time = models.DateTimeField()
    language = models.CharField(max_length=50, choices=[
        ('original', 'Оригинал'),
        ('dubbed', 'Дублированный'),
    ])

    def __str__(self):
        return f"{self.movie.title} - {self.date_time.strftime('%d.%m.%Y %H:%M')}"

