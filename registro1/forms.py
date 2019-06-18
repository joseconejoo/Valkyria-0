from django import forms
from django.contrib.auth.models import User
from .models import Pagos, Codigos, Datos, DatosPrev, Post, Bolsa, prod_Bolsa, product
from django.contrib.auth.forms import UserCreationForm

class PagosAF(forms.ModelForm):
	class Meta:
		model = Pagos
		fields = ('confirmacion',)

class PagosF(forms.ModelForm):
	class Meta:
		model = Pagos
		fields = ('referencia','banco','f_envio')

class ValidF(forms.ModelForm):

    class Meta:
        model = Codigos
        fields = ('codigo',)

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('titulo', 'texto',)

class DatosF(forms.ModelForm):
	class Meta:
		model = Datos
		fields = ('nombre', 'apellido', 'cedula', 'email', 'manzana')

class DatosPrevF(forms.ModelForm):
	class Meta:
		model = DatosPrev
		fields = ('nombre', 'apellido', 'cedula')

class BolsaF(forms.ModelForm):
	class Meta:
		model = Bolsa
		fields = ()

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
