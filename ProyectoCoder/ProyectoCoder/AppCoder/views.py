from django.shortcuts import render

from django.http import HttpResponse

from AppCoder.forms import VentasFormulario

from AppCoder.models import Productos, Ventas



# Create your views here.

def ventasFormulario(request):
    
    #obtiene la direccion y el anioFund
    
    if request.method == "POST":
        
        miFormulario = VentasFormulario(request.POST)
        
        if miFormulario.is_valid():  
            
            informacion = miFormulario.cleaned_data
        
            vendido = Ventas(producto=informacion["producto"] ,precio= informacion["precio"])
            
            vendido.save() 
            
            return render(request, 'AppCoder/inicio.html')
    
    
    else:
        
        miFormulario = VentasFormulario()
    
    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/VentasFormulario.html',{"miFormulario":miFormulario})



#Primer vista
def inicio(request):
    
    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/inicio.html')


def clientes(request):
    
    
    return render(request, 'AppCoder/clientes.html')


def productos(request):
    
    
    return render(request, 'AppCoder/producto.html')