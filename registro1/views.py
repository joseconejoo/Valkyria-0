from django.views.generic import FormView, TemplateView, RedirectView
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from .models import Datos, Post
from .forms import PostForm,DatosF


from django.contrib.auth.forms import UserCreationForm
from django.views import generic

from django.contrib.auth.views import LoginView

# Create your views here.
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    # el - en published_date se imprime descendente si quito el " - " se vuelve ascendente
    #published_date__lte es una fecha para comparar y ordenad el published_date
    #datos = Datos.objects.get(usuario_id=10)
    if request.user.is_authenticated==True and Datos.objects.filter(usuario_id=request.user.pk).exists()==True:
        #datos no lleva request.datos porque eso se configura en el wsgi, es decir porque
        #la de user es externa lleva request.user en resumidas palabras
        #if user is not None:
        #Books.objects.order_by('name')
        usuarioPs=request.user.pk
        datos = Datos.objects.get(usuario_id=usuarioPs)
        return render(request, 'post_list.html', {'posts': posts, 'datos': datos})
    else:
        return render(request, 'post_list.html', {'posts': posts})

    #usar usuario_id=10 y pk=10 es lo mismo
    #objects.get es el que funciona
    #datos = Datos.objects.filter(Datos, pk=pk)
    #datos = Datos.objects.filter(dingreso__lte=timezone.now()).order_by('dingreso')


def datos_u(request, pk):
    datos = get_object_or_404(Datos, pk=pk)
    return render(request, 'datos_u.html', {'datos': datos})

def Datos1(request):
    if request.method == "POST":
        form = DatosF(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = request.user
            post.fedicion = timezone.now()
            post.save()
            return redirect('datos_u', pk=post.usuario)
            #si cambio la pk de post a datos.usuario permite crear varios datos bug. y unique en models
            #Permite crear varios "datos" a un mismo usuario por un Bug. Ademas de que no tenia habilitado 
            #el request.user
    else:
        form = DatosF()
    return render(request, 'datose.html', {'form': form})
    #datos1 no tiene HTML porque esta usando el de datose
def datose(request, pk):
    post = get_object_or_404(Datos, pk=pk)
    if request.method == "POST":
        form = DatosF(request.POST, instance=post)
        #la instancia sirve para almacenar los datos que se recogieron en el formulario
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = request.user
            post.fedicion = timezone.now()
            #en vez de fedicion estaba published_date, esto ocasionaba que no me guardara nada en fedicion
            post.save()
            return redirect('datos_u', pk=post.pk)
    else:
        form = DatosF (instance=post)
    return render(request, 'datose.html', {'form': form})
def datos_vi(request):
    posts = Datos.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'Datos1.html', {'datos': datos})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

class registros1(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registros1.html'

class login(LoginView):
    template_name = 'login.html'
    #la funcion dispatch viene de LoginView el cual como template_name se sobreescribe como
    #si fuese un molde
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated!=True:

            if self.redirect_authenticated_user and self.request.user.is_authenticated:
                redirect_to = self.get_success_url()
                return HttpResponseRedirect(redirect_to)
            return super().dispatch(request, *args, **kwargs)
        else:
            redirect_to = self.get_success_url()
            return HttpResponseRedirect(redirect_to)