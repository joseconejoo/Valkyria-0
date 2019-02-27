from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list '),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),	
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('registros', views.registros1.as_view(), name='registros1'),
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
    #detail
    path('bolsa/', views.Bolsa_N, name='Bolsa_N'),
    path('bolsas/lista', views.Bolsas, name='Bolsas'),
    #detail
    path('producto/', views.Product_N, name='Product_N'),
    path('productos/lista', views.productos, name='productos'),

]
