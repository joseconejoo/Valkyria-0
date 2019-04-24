from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms


class Codigos(models.Model):
    codigo = models.IntegerField(default=100, unique=True)

    def __str__(self):
        return str(self.id)

class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.fecha_creacion = timezone.now()
        self.save()
    #El __str__ es lo que devolvera al escribir xxxx.objects.all()
    #Si se buguea la clave foranea se debe borrar todo lo de migrations
    #menos el __init__ y el cache, y el archivo de la base de datos
    def __str__(self):
        return self.titulo

class Datos(models.Model):
    usuario = models.OneToOneField('auth.User',on_delete=models.CASCADE, primary_key=True, unique=True)
    nombre = models.CharField(max_length=200, default = "Ingrese Nombre")
    apellido= models.CharField(max_length=200, default = "Ingrese Apellido")
    #dingreso=models.DateTimeField(default=timezone.now)
    #Si da algun error a  la hora de hacer migraciones y pide que rellene campo
    # solo debo escribir algo como str("Null") si es letra o int(1)
    cedula=models.IntegerField(default = 20000)
    email=models.EmailField(default = 'ejemplo@go.com')
    fedicion=models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.fedicion = timezone.now()
        self.save()

    def __str__(self):
        return str(self.usuario_id)+" "+(self.nombre)

class Bolsa(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    fecha_B = models.DateTimeField(blank=True)
    coste_B = models.IntegerField(default=100)

    def __str__(self):
        return str(self.id)

class prod_Bolsa(models.Model):
    Num_Bolsa = models.ForeignKey(Bolsa,on_delete=models.CASCADE)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    cant_prod = models.IntegerField(default=1)

    def __str__(self):
        return str(self.id)

class product(models.Model):
    Num_prod = models.OneToOneField(prod_Bolsa, on_delete=models.CASCADE,primary_key=True, unique=True)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=200, default = "Ingrese Producto")
    precio = models.IntegerField(default=100)

    def __str__(self):
        return self.nombre

class Pagos(models.Model):
    Num_Bolsa = models.ForeignKey(Bolsa,on_delete=models.CASCADE, null=True)
    referencia = models.IntegerField(unique=True)
    confirmacion = models.BooleanField(null=True, blank=True)
    origen = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    f_envio = models.DateTimeField(blank=True, null=True)
    banco = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)
