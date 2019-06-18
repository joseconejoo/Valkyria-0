from django.views.generic import FormView, TemplateView, RedirectView
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from .models import Pagos, Codigos, Datos, Post, Bolsa, prod_Bolsa, product
from .forms import PagosAF, PagosF, ValidF, PostForm,DatosF, BolsaF, prod_BolsaF, productF
import time

import random

from io import BytesIO
from reportlab.pdfgen import canvas

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.views import generic

from django.contrib.auth.views import LoginView

# Create your views here.
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
def post_list(request):
    """
    print (User.objects.get(id=6))
    misReservas = Datos.objects.filter(usuario__username='Metal')
    #misReservas = Datos.objects.filter(usuario='Metal')
    #eso retorn un int por lo visto, y da error si no lo coloco con usuario __username
    #la instruccion hecha correctamente me retorna el return de la tabla Datos
    for x12 in misReservas:
        print (x12)
        print (x12)


    print (str(request.user) + "hola "+str(request.user.pk))

    for x in post1:
        print (x.Nombre_Del_CaMPO)
    """
    if request.user.is_authenticated == True:
        
        posts = Post.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
        # el - en fecha_publicacion se imprime descendente si quito el " - " se vuelve ascendente
        #fecha_publicacion__lte es una fecha para comparar y ordenad el fecha_publicacion
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
    else:
        return HttpResponseRedirect("login")

def datos_u(request, pk):
    try:
        dat=Datos.objects.get(pk=pk)
        Verthandi=User.objects.get(pk=pk)
            
        datos = get_object_or_404(Datos, pk=pk)
        return render(request, 'datos_u.html', {'datos': datos,'dat': dat,'usuario1':Verthandi})

    except:
        if request.method == "POST":
            form = DatosF(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.usuario = User.objects.get(id=pk)
                #Si no coloco user.objects.get y solo coloco la pk o variable, no funciona
                #Todo debe estar "instanciado"
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
            """
            print (post.usuario + "AKA1")
            ese print no se va a imprimir porque se ejecuta con POST y lo "protege"
            """
            return redirect('datos_u', pk=post.pk)
            #si cambio la pk de post a datos.usuario permite crear varios datos bug. y unique en models
            #Permite crear varios "datos" a un mismo usuario por un Bug. Ademas de que no tenia habilitado 
            #el request.user
    else:

        if Datos.objects.filter(usuario_id=request.user.pk).exists():
            return redirect('datos_u', pk=request.user.pk)
        form = DatosF()
    return render(request, 'datose.html', {'form': form})
    #datos1 no tiene HTML porque esta usando el de datose
    #podria usar diccionarios en el form para cambiar nombre de campos quizas
def datose(request, pk):
    post = get_object_or_404(Datos, pk=pk)
    if request.method == "POST":
        form = DatosF(request.POST, instance=post)
        #la instancia sirve para almacenar los datos que se recogieron en el formulario
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = request.user
            post.fedicion = timezone.now()
            #en vez de fedicion estaba fecha_publicacion, esto ocasionaba que no me guardara nada en fedicion
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

def v_us1(request):

    if request.user.is_authenticated==True:
        v_us = User.objects.order_by('id')
        datos = Datos.objects.order_by('usuario_id')
        return render(request, 'v_us1.html', {'v_us': v_us,'datos': datos})
    
    else:
        return HttpResponseRedirect("/")

def Bolsa_N(request):
    if request.method == "POST":
        if request.user.is_superuser:
            try:
                valks2 = Datos.objects.get(usuario_id=request.user.pk)
                form = BolsaF(request.POST) 
                if form.is_valid():
                    post = form.save(commit=False)
                    post.autor = request.user
                    post.fecha_B = timezone.now()
                    post.save()
                    return redirect('Bolsa', pk=post.pk)


            except:
                return redirect('datos_u', pk=request.user.pk)
        else:
            return redirect('Bolsas')


    else:
        form = BolsaF()
    return redirect('Bolsas')
def Bolsa1(request, pk,asd=1):
    post = get_object_or_404(Bolsa, pk=pk)
    post2 = prod_Bolsa.objects.filter(Num_Bolsa=pk).order_by('id')
    #post1 = get_object_or_404(Pagos, pk=pk)
    fox = ""
    form3 = "" 
    form2 = ""
    Metal = ""
    if 'arriba1' in request.POST:
        asd+=1

    if request.user.is_superuser:
        Metal = Bolsa.objects.latest('id')
        form2 = PagosAF()

        if int(str(Metal)) == pk:
            fox = prod_BolsaF()
            form3 = productF()
        

    
    Skuld=[]
    for x2 in post2:
        Skuld.append(x2)

    post1=""
    try:
        valks2 = Datos.objects.get(usuario_id=request.user.pk)
        valks2=valks2.manzana

        Valhalla = []
        if (request.user.is_superuser or request.user.is_staff):
            post1 = Pagos.objects.filter(Num_Bolsa=pk).order_by('Num_Bolsa')
            for x in post1:
                Verthandi= (int(str(x.origen_id)))
                try:

                    Urd = Datos.objects.get(usuario_id=Verthandi)
                    if Urd.manzana == valks2:
                        Valhalla.append(x)
                except:
                    pass

    except:
        return redirect('datos_u', pk=request.user.pk)




    
    
    obtn = product.objects.filter(Num_prod__in=Skuld).order_by('Num_prod')
    diccionario={'post': post,'post2':post2,'post3':obtn,'post4':Valhalla,'form':fox,'form2':form2,'form3':form3,'Metal':Metal}
    return render(request, 'Bolsa.html', diccionario)


def Bolsas(request):
    post = Bolsa.objects.order_by('id')
    form = PagosF()
    form2 =''
    if request.user.is_superuser or request.user.is_staff:
        form2 = BolsaF() 
    

    #post1 = get_object_or_404(Pagos, pk=pk)
    # creacion de nuevo campo para mostrar en html abajo
    post1 = Pagos.objects.filter(origen=request.user.pk).order_by('Num_Bolsa')
    Verthandi = []
    for obj in post:
        Valkyria=0
        Valhalla = prod_Bolsa.objects.filter(Num_Bolsa=obj.pk).order_by('Num_Bolsa')
        for Skuld in Valhalla:
            try:
                Urd = product.objects.get(Num_prod=obj.pk)
                Valkyria+=Urd.precio*Skuld.cant_prod
            except:
                pass
            

        obj.costo = Valkyria

    obtn,obtn2 = [],[]
    for x in post1:
        obtn2.append(int(str(x.Num_Bolsa)))
    for x in post:
        if x.pk not in obtn2:
            obtn.append(x.pk)

    return render(request, 'Bolsas.html', {'posts': post,'posts2':post1,'posts3':obtn,'form':form,'form2':form2})
    
def Product_N(request, pk):
    if request.method == "POST":
        asdddd=get_object_or_404(Bolsa, pk=pk)
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
    return render(request, 'producto.html', {'form': fox})

def Valid_v(request):
    post = Codigos.objects.order_by('id')

    return render(request, 'valids.html', {'code': post})

def Valid1(request):
    if request.user.is_superuser or request.user.is_staff:
        if request.method == "POST":
            while True:
                x12 = random.randint(100000000000, 999999999999)
                if not Codigos.objects.filter(codigo=x12).exists() :
                    Codigos.objects.create(codigo=x12)
                    return redirect('Valid_v')


        else:
            form = ValidF()
        return render(request, 'valid.html', {'form': form})
    else:
        return HttpResponseRedirect("/Error")

def Error(request):
    return render(request, "Negado.html")

def Pago1(request, pk):
    if request.method == "POST":
        pagb = Bolsa.objects.filter(id=pk).order_by('id')
        pag = Pagos.objects.filter(origen=request.user.pk).order_by('Num_Bolsa')
        obtn,obtn2 = [],[]

        for x in pagb:
            if obtn2:
                break
            else:
                obtn2.append(x.pk)
        for x in pag:
            if int(str(x.Num_Bolsa)) in obtn2:
                if obtn:
                    break
                else:
                    obtn.append(int(str(x.Num_Bolsa)))
        
        #comprobacion que no haya realizado pago antes
        Verthandi = Bolsa.objects.latest('id')
        if not obtn:
            form = PagosF(request.POST)
            if form.is_valid():

                if pk == Verthandi.pk:
                    post = form.save(commit=False)
                    post.origen = request.user
                    post.Num_Bolsa = Bolsa.objects.get(id=pk)
                    post.f_envio = timezone.now()
                    post.save()
                    return redirect('Bolsas')

                else:
                    return redirect('Bolsas')    
                

        else:
            return HttpResponseRedirect("/Error")

    else:
        form = PagosF()


    return redirect('Bolsas')    

    #return render(request, 'Pagos1.html', {'form': form})

def Pago2(request, pk):
    if request.user.is_staff:
        post = get_object_or_404(Pagos, pk=pk)
        if request.method == "POST":
            form = PagosAF(request.POST, instance=post)
            if not post.confirmacion:
                if form.is_valid():
                    post = form.save(commit=False)
                    data1 = request.POST.get('confirmacion')
                    if data1=="true":
                        post.save()
                    else:
                        Pagos.objects.filter(pk=pk).delete()
                        
                    return redirect('Bolsa',pk=int(str(post.Num_Bolsa)))
            else:
                return redirect('Bolsa',pk=int(str(post.Num_Bolsa)))


        else:
            if not post.confirmacion:
                form = PagosAF(instance=post)
            else:
                return redirect('Bolsa',pk=int(str(post.Num_Bolsa)))

        return render(request, 'Pagos1.html', {'form': form})
    else:
        return redirect('/Error')

def reportD(request, pk):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="mypdf.pdf"'
    Eldhrimnir = Datos.objects.get(usuario_id=pk)

    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    # Start writing the PDF here
    # End writing
    p.setLineWidth(.3)
    p.setFont('Helvetica', 12)
     
    px=30
    py=650

    py-=16
    p.drawString(70,750,"            Este es el perfil de usuario nº "+str(Eldhrimnir.pk))
    p.drawString(470,660,"Fecha de informacion")
    p.drawString(500,700,(time.strftime("%d/%m/%y")))
    p.drawString(px,py,"Nombre: "+str(Eldhrimnir.nombre))
    py-=16
    p.drawString( px,py,"Apellido: "+str(Eldhrimnir.apellido))
    py-=16
    p.drawString( px,py,"Cedula: "+ str(Eldhrimnir.cedula))
    py-=16
    p.drawString( px,py,"Manzana: " + str(Eldhrimnir.manzana))
    py-=16

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

def def_V(request):
    if request.user.is_authenticated==True:
        query = request.POST['B_V']
        v_us = User.objects.filter(username__icontains=query).order_by('id')
        return render(request, 'v_us1.html', {'v_us': v_us,'query':query})
    
    else:
        return HttpResponseRedirect("/")


def adminM(request, pk):
    if request.user.is_superuser:
        Verthandi = User.objects.get(id=pk)
        Eldhrimnir = Datos.objects.get(usuario_id=pk)
        Urd = Datos.objects.filter(manzana=Eldhrimnir.manzana)

        Valhalla = []
        for x in Urd:
            if User.objects.get(id=x.pk).is_superuser:
                Valhalla.append(x)
                break

        if not Valhalla:
            Verthandi.is_staff = True
            Verthandi.save()
            return redirect('datos_u', pk=pk)
        else:
            return redirect('datos_u', pk=pk)

    else:
        return redirect ("/")

def adminQ(request, pk):
    if request.user.is_superuser:
        Verthandi = get_object_or_404(User, pk=pk)

        Verthandi.is_staff = False
        Verthandi.save()
        return redirect('datos_u', pk=pk)

    else:
        return redirect ("/")
