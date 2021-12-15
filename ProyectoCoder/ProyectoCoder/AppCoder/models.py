from django.db import models

# Create your models here.


    
class Clientes(models.Model):
    
    apellido = models.CharField(max_length=40)
    numeroCliente = models.IntegerField()
    
    
    
class Productos(models.Model):
    
    nombreProducto = models.CharField(max_length=40)
    cantidad = models.IntegerField()
    
    
class Ventas(models.Model):
    
    producto = models.CharField(max_length=40)
    precio = models.IntegerField()