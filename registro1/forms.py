from django import forms
from django.contrib.auth.models import User
from .models import Post, Datos
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class DatosF(forms.ModelForm):
	class Meta:
		model = Datos
		fields = ('nombre', 'apellido','dingreso', 'cedula', 'email','fedicion')

class Crea_u(UserCreationForm):
	def save(self, commit=True):
	    user = super().save(commit=False)
	    user.set_password(self.cleaned_data["password1"])
	    if commit:
	        user.save()
	    return user