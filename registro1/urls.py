from django.urls import path, include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list '),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),	
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('registros', views.registros1, name='registros1'),
    path('perfil/<int:pk>/', views.datos_u, name='datos_u'),
    path('perfil', views.Datos1, name='datos1'),
    path('datos/<int:pk>/edit/', views.datose, name='datose'),
    path('login/', views.login.as_view(), name='login'),

    path('u_lista', views.v_us1, name='v_us1'),
    path('bolsa/<int:pk>/', views.Bolsa1, name='Bolsa'),
    path('bolsa/', views.Bolsa_N, name='Bolsa_N'),
    path('bolsas/lista', views.Bolsas, name='Bolsas'),
    path('producto/<int:pk>/', views.Product_N, name='Product_N'),
    path('Codigos', views.Valid_v, name='Valid_v'),
    path('Codigos/gen', views.Valid1, name='Valid'),
    path('Error', views.Error, name='Error'),
    path('pago/<int:pk>/', views.Pago1, name='Pago1'),
    path('pago/<int:pk>/', views.Pago2, name='Pago2'),




]
