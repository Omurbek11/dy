from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    poster = models.ImageField(upload_to='posters/', verbose_name="Постер")
    description = models.TextField(verbose_name="Описание")
    genre = models.CharField(max_length=100, verbose_name="Жанр")
    duration = models.IntegerField(verbose_name="Продолжительность (минуты)")
    age_rating = models.CharField(max_length=10, verbose_name="Возрастной рейтинг")
    is_coming_soon = models.BooleanField(default=False, verbose_name="Скоро в кино")
    release_date = models.DateField(null=True, blank=True, verbose_name="Дата выхода")
    trailer_url = models.URLField(null=True, blank=True, verbose_name="Ссылка на трейлер")

    def __str__(self):
        return self.title

class ComingSoon(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    release_date = models.DateField()
    trailer_url = models.URLField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    duration = models.IntegerField()
    age_rating = models.CharField(max_length=10)

    def __str__(self):
        return self.title

class ComingSoon(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    release_date = models.DateField()
    trailer_url = models.URLField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class TheaterPhoto(models.Model):
    image = models.ImageField(upload_to='theater_photos/', blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption or f"Фото {self.id}"
    from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    duration = models.IntegerField()
    age_rating = models.CharField(max_length=10)

    def __str__(self):
        return self.title

class ComingSoon(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    release_date = models.DateField()
    trailer_url = models.URLField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    duration = models.IntegerField()
    age_rating = models.CharField(max_length=10)

    def __str__(self):
        return self.title

class ComingSoon(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    release_date = models.DateField()
    trailer_url = models.URLField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    duration = models.IntegerField()
    age_rating = models.CharField(max_length=10)

    def __str__(self):
        return self.title

class ComingSoon(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='posters/', blank=True, null=True)
    release_date = models.DateField()
    trailer_url = models.URLField(blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

class TheaterPhoto(models.Model):
    image = models.ImageField(upload_to='theater_photos/', blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption or f"Фото {self.id}"
    from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    duration = models.IntegerField()
    age_rating = models.CharField(max_length=10)
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.poster:
            img = Image.open(self.poster)
            if img.width > 350:
                output_size = (350, int(350 * img.height / img.width))
                img = img.resize(output_size, Image.Resampling.LANCZOS)
                output = BytesIO()
                img.save(output, format='JPEG', quality=80)
                self.poster = InMemoryUploadedFile(
                    output, 'ImageField', f"{self.poster.name.split('.')[0]}.jpg",
                    'image/jpeg', sys.getsizeof(output), None
                )
        super().save(*args, **kwargs)
       
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    duration = models.IntegerField()
    age_rating = models.CharField(max_length=10)
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.poster:
            img = Image.open(self.poster)
            if img.mode != 'RGB':
                img = img.convert('RGB')  # Конвертируем в RGB для JPEG
            if img.width > 350:
                output_size = (350, int(350 * img.height / img.width))  # Сохраняем пропорции
                img = img.resize(output_size, Image.Resampling.LANCZOS)
                output = BytesIO()
                img.save(output, format='JPEG', quality=80, optimize=True)
                output.seek(0)
                self.poster = InMemoryUploadedFile(
                    output, 
                    'ImageField', 
                    f"{self.poster.name.split('.')[0]}.jpg",
                    'image/jpeg', 
                    sys.getsizeof(output), 
                    None
                )
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class ComingSoon(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    poster = models.ImageField(upload_to='coming_soon_posters/', null=True, blank=True)
    trailer_url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class TheaterPhoto(models.Model):
    image = models.ImageField(upload_to='theater_photos/')
    caption = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption or f"Photo {self.id}"