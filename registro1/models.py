from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
class Datos(models.Model):
    usuario = models.ForeignKey("auth.User",on_delete=models.CASCADE, primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido= models.CharField(max_length=200)
    dingreso=models.DateTimeField(default=timezone.now)
    cedula=models.IntegerField()
    email=models.EmailField()
    fedicion=models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.fedicion = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre