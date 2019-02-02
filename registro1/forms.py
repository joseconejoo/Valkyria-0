from django import forms
from django.contrib.auth.models import User
from .models import Post, Datos

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class DatosF(forms.ModelForm):
	class Meta:
		model = Datos
		fields = ('usuario', 'nombre', 'apellido', 'dingreso', 'cedula', 'email')


