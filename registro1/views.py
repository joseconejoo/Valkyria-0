from django.views.generic import FormView, TemplateView, RedirectView
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from .models import Pagos, Codigos, Datos, Post, Bolsa, prod_Bolsa, product
from .forms import PagosAF, PagosF, ValidF, PostForm,DatosF, BolsaF, prod_BolsaF, productF


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.views import generic

from django.contrib.auth.views import LoginView

# Create your views here.
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
def post_list(request):
    if request.user.is_authenticated == True:
        
        posts = Post.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
        if request.user.is_authenticated==True and Datos.objects.filter(usuario_id=request.user.pk).exists()==True:
            usuarioPs=request.user.pk
            datos = Datos.objects.get(usuario_id=usuarioPs)
            return render(request, 'post_list.html', {'posts': posts, 'datos': datos})
        else:
            return render(request, 'post_list.html', {'posts': posts})
    else:
        return HttpResponseRedirect("login")

def datos_u(request, pk):
    try:
       dat=Datos.objects.get(pk=pk)
       datos = get_object_or_404(Datos, pk=pk)
       return render(request, 'datos_u.html', {'datos': datos,'dat': dat})

    except:
        if request.method == "POST":
            form = DatosF(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.usuario = User.objects.get(id=pk)
                post.fedicion = timezone.now()
                post.save()

                return redirect('datos_u', pk=post.pk)
        else:
            form = DatosF()
        return render(request, 'datose.html', {'form': form})
def Datos1(request):
    if request.method == "POST":
        form = DatosF(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = request.user
            post.fedicion = timezone.now()
            post.save()
            return redirect('datos_u', pk=post.pk)
    else:
        form = DatosF()
    return render(request, 'datose.html', {'form': form})
def datose(request, pk):
    post = get_object_or_404(Datos, pk=pk)
    if request.method == "POST":
        form = DatosF(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = request.user
            post.fedicion = timezone.now()
            post.save()
            return redirect('datos_u', pk=post.pk)
    else:
        form = DatosF (instance=post)
    return render(request, 'datose.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fecha_publicacion = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.fecha_publicacion = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


def registros1(request):
    if request.method == "POST":
        foxr = UserCreationForm(request.POST)
        form = ValidF(request.POST)
        if foxr.is_valid():
            post = foxr.save(commit=False)
            data1 = request.POST.get('codigo')
            if Codigos.objects.filter(codigo=data1).exists()==True:
                Codigos.objects.filter(codigo=data1).delete()
                post.save()
                return redirect('login')


            else:
                return HttpResponseRedirect("Error")
    else:
        foxr = UserCreationForm()
        form = ValidF()

    return render(request, 'registros1.html', {'form': foxr,'form2':form})

class login(LoginView):
    template_name = 'login.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated!=True:

            if self.redirect_authenticated_user and self.request.user.is_authenticated:
                redirect_to = self.get_success_url()
                return HttpResponseRedirect(redirect_to)
            return super().dispatch(request, *args, **kwargs)
        else:
            redirect_to = self.get_success_url()
            return HttpResponseRedirect(redirect_to)

def v_us1(request):

    if request.user.is_authenticated==True:
        v_us = User.objects.order_by('id')
        datos = Datos.objects.order_by('usuario_id')
        return render(request, 'v_us1.html', {'v_us': v_us,'datos': datos})
    
    else:
        return HttpResponseRedirect("/")

def Bolsa_N(request):
    if request.method == "POST":
        form = BolsaF(request.POST) 
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('Bolsa', pk=post.pk)
    else:
        form = BolsaF()
    return render(request, 'Bolsa_N.html', {'form': form})

def Bolsa1(request, pk):
    post = get_object_or_404(Bolsa, pk=pk)
    post2 = prod_Bolsa.objects.filter(Num_Bolsa=pk).order_by('id')

    skuld=[]
    for x2 in post2:
        skuld.append(x2)
    obtn = product.objects.filter(Num_prod__in=skuld).order_by('Num_prod')
    diccionario={'post': post,'post2':post2,'post3':obtn}
    return render(request, 'Bolsa.html', diccionario)


def Bolsas(request):
    post = Bolsa.objects.order_by('id')
    post1 = Pagos.objects.filter(origen=request.user.pk).order_by('Num_Bolsa')
    obtn,obtn2 = [],[]
    for x in post1:
        obtn2.append(int(str(x.Num_Bolsa)))
    for x in post:
        if x.pk not in obtn2:
            obtn.append(x.pk)

    return render(request, 'Bolsas.html', {'posts': post,'posts2':post1,'posts3':obtn})
    
def Product_N(request, pk):
    if request.method == "POST":
        asddd=Bolsa.objects.get(id=pk)
        fox = prod_BolsaF(request.POST)
        form2 = productF(request.POST) 

        if fox.is_valid() and form2.is_valid():
            post = fox.save(commit=False)
            post.autor = request.user
            post.Num_Bolsa=asddd
            post2 = form2.save(commit=False)
            post2.Num_prod=post.pk
            post2.autor = request.user
            post.save()
            post2.save()

            return redirect('Bolsa', pk=pk)
    else:
        fox = prod_BolsaF()
        form2 = productF() 
    return render(request, 'producto.html', {'form': fox,"form2": form2})


def Valid_v(request):
    post = Codigos.objects.order_by('id')

    return render(request, 'valids.html', {'code': post})

def Valid1(request):
    if request.method == "POST":
        form = ValidF(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('Valid_v')
    else:
        form = ValidF()
    return render(request, 'valid.html', {'form': form})

def Error(request):
    return render(request, "Negado.html")

def Pago1(request, pk):
    if request.method == "POST":
        form = PagosF(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.origen = request.user
            post.Num_Bolsa = Bolsa.objects.get(id=pk)
            post.f_envio = timezone.now()
            post.save()
            return redirect('Bolsas')
    else:
        form = PagosF()
    return render(request, 'Pagos1.html', {'form': form})

def Pago2(request, pk):
    if request.method == "POST":
        form = PagosAF(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('Bolsas')
    else:
        form = PagosAF()
    return render(request, 'Pagos1.html', {'form': form})