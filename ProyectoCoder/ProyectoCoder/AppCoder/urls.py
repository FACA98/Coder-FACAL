from django.urls import path
from AppCoder import views


urlpatterns = [
   
    
    path('inicio', views.inicio, name="Inicio"),
    path('clientes', views.clientes, name="Clientes"),
    path('productos', views.productos, name="Productos"),
    path('VentasFormulario', views.VentasFormulario),

    
]