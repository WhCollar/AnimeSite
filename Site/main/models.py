from django.db import models
from django.urls import reverse

'''
Content (Slug Title Photo Status Year Season Age_rating Genre Original_source Studio 
Director Content_type Number_of_episodes Dubbing_studio Synopsis)
======================

Status (id Title)
======================

Age_rating (id title)
======================

Genre (id title)
======================

Dubbing_studio (id title)
======================
'''


class VideoPlayer(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Плеер'
        verbose_name_plural = 'Плееры'
        ordering = ['title']


class Status(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
        ordering = ['title']


class Age_rating(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Возрастной рейтинг'
        verbose_name_plural = 'Возрастные рейтинги'
        ordering = ['title']


class Genre(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['title']


class Dubbing_studio(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Озвучка'
        verbose_name_plural = 'Озвучки'
        ordering = ['title']


class Content_type(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'
        ordering = ['title']


class IframeForContent(models.Model):
    title = models.CharField(max_length=255)
    src = models.TextField(blank=False)
    number_of_episodes = models.IntegerField(blank=False)
    dubbing_studio = models.ForeignKey(Dubbing_studio, on_delete=models.PROTECT, blank=False)
    video_player = models.ForeignKey(VideoPlayer, on_delete=models.PROTECT, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Iframe видео'
        verbose_name_plural = 'Iframe видео'


class Content(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    photo = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    year = models.IntegerField(blank=False)
    season = models.CharField(max_length=50, blank=True)
    age_rating = models.ForeignKey(Age_rating, on_delete=models.PROTECT, blank=False)
    genre = models.ManyToManyField(Genre, blank=True)
    original_source = models.CharField(max_length=255, blank=True)
    studio = models.CharField(max_length=255, blank=True)
    director = models.CharField(max_length=255, blank=True)
    content_type = models.ForeignKey(Content_type, on_delete=models.PROTECT, blank=False)
    Number_of_episodes = models.IntegerField(blank=False)
    dubbing_studio = models.ManyToManyField(Dubbing_studio, blank=True)
    synopsis = models.TextField(blank=True)
    iframe = models.ManyToManyField(IframeForContent, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('item', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Аниме'
        verbose_name_plural = 'Аниме'
        ordering = ['-year']
