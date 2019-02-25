from django import forms
from django.contrib.auth.models import User
from .models import Datos, Post, Bolsa, prod_Bolsa, product
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class DatosF(forms.ModelForm):
	class Meta:
		model = Datos
		fields = ('nombre', 'apellido','dingreso', 'cedula', 'email','fedicion')

class BolsaF(forms.ModelForm):
	class Meta:
		model = Bolsa
		fields = ('fecha_B', 'coste_B')

class prod_BolsaF(forms.ModelForm):
	class Meta:
		model = prod_Bolsa
		fields = ('cant_prod',)

class productF(forms.ModelForm):
	class Meta:
		model = product
		fields = ('nombre', 'precio')

class Crea_u(UserCreationForm):
	def save(self, commit=True):
	    user = super().save(commit=False)
	    user.set_password(self.cleaned_data["password1"])
	    if commit:
	        user.save()
	    return user