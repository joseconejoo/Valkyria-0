from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list '),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),	
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('registros', views.registros1, name='registros1'),
    #si no se define no actua el int:pk
    path('perfil/<int:pk>/', views.datos_u, name='datos_u'),
    #habia colocado mal el int:pk/> no lo habia cerrado y ocasiono un bug con el "/"
    # habia colocado <int:pk/>
    # lo corregi a <int:pk>/ pero daba error le agregue // y luego le borre uno
    path('perfil', views.Datos1, name='datos1'),
    path('datos/<int:pk>/edit/', views.datose, name='datose'),
    path('login/', views.login.as_view(), name='login'),
    #error de 1 tomado pero regresa 2. si no coloco as_view

    path('u_lista', views.v_us1, name='v_us1'),
    path('bolsa/<int:pk>/', views.Bolsa1, name='Bolsa'),
    path('bolsa/', views.Bolsa_N, name='Bolsa_N'),
    path('bolsas/lista', views.Bolsas, name='Bolsas'),
    path('producto/<int:pk>/', views.Product_N, name='Product_N'),
    path('Codigos', views.Valid_v, name='Valid_v'),
    path('Codigos/gen', views.Valid1, name='Valid'),
    path('Error', views.Error, name='Error'),
    path('pago/<int:pk>/', views.Pago1, name='Pago1'),
    path('pagos/<int:pk>/', views.Pago2, name='Pago2'),
    path('Datos-Pdf/<int:pk>/', views.reportD, name='reportD'),
    path('buscador/', views.def_V, name='def_V'),
    path('añadiradm/<int:pk>/', views.adminM, name='añadm'),
    path('quitaradm/<int:pk>/', views.adminQ, name='quadm'),
    path('Bolsa_P/<int:pk>/', views.Bolsa1_P, name='Bolsa1_P'),
    path('aceptarusers/', views.a_us, name='a_us'),
    path('User?12@#|2aprove?/<int:pk>', views.userAP, name='userAP'),
    path('User?14@#|2aprove?/<int:pk>', views.userNE, name='userNE'),
    path('Bolsr?11@#@|2close?/<int:pk>', views.cerrarBols, name='cerrarBols'),


]
