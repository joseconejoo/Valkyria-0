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
    #El __str__ es lo que devolvera al escribir xxxx.objects.all()
    def __str__(self):
        return self.title

class Datos(models.Model):
    usuario = models.OneToOneField('auth.User',on_delete=models.CASCADE, primary_key=True, unique=True)
    nombre = models.CharField(max_length=200, default = "Ingrese Nombre")
    apellido= models.CharField(max_length=200, default = "Ingrese Apellido")
    dingreso=models.DateTimeField(default=timezone.now)
    cedula=models.IntegerField(default = 20000)
    email=models.EmailField(default = 'ejemplo@go.com')
    fedicion=models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.fedicion = timezone.now()
        self.save()

    def __str__(self):
        return str(self.usuario_id)+" "+(self.nombre)

class Bolsa(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    fecha_B = models.DateTimeField(blank=True)
    coste_B = models.IntegerField(default=100)

    def __str__(self):
        return str(self.fecha_B)

class prod_Bolsa(models.Model):
    Num_Bolsa = models.ForeignKey(Bolsa,on_delete=models.CASCADE)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    id_prod = models.IntegerField(unique=True)
    cant_prod = models.IntegerField(default=1)

    def __str__(self):
        return str(self.Num_Bolsa)

class product(models.Model):
    Num_prod = models.OneToOneField(prod_Bolsa, on_delete=models.CASCADE,primary_key=True, unique=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=200, default = "Ingrese Producto")
    precio = models.IntegerField(default=100)

    def __str__(self):
        return self.nombre