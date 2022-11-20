from django.db import models
from .resourses import STATUS


class User(models.Model):
    email = models.EmailField(unique=True)
    fam = models.CharField(max_length=25)
    name = models.CharField(max_length=15)
    otc = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)


class Pereval(models.Model):
    beauty_title = models.CharField(max_length=10, default='пер.')
    title = models.CharField(max_length=25)
    other_titles = models.CharField(max_length=25)
    connect = models.CharField(max_length=25, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    level_winter = models.CharField(max_length=2, blank=True)
    level_summer = models.CharField(max_length=2, blank=True)
    level_autumn = models.CharField(max_length=2, blank=True)
    level_spring = models.CharField(max_length=2, blank=True)
    status = models.CharField(max_length=2, choices=STATUS, default='NW')


class Coords(models.Model):
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='coords')
    latitude = models.CharField(max_length=15)
    longitude = models.CharField(max_length=15)
    height = models.CharField(max_length=15)


class Image(models.Model):
    data = models.ImageField()
    title = models.CharField(max_length=50)


class PerevalImage(models.Model):
    foto = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='image')
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='pereval')
