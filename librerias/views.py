from types import NoneType
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Producto
from .forms import ProductoForm
from django.contrib import messages

from .models import Persona
from .serializers import PersonaSerializer
from .serializers import ProductoSerializer
from rest_framework.viewsets import ModelViewSet

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def indexV3(request):
    return render(request, 'paginas/indexV3.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/index.html', {'productos': productos} )

def crear(request):
    formulario = ProductoForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('productos')
    return render(request, 'productos/crear.html', {'formulario': formulario})
# Hasta Crear todo OK

def editar(request, id):
    
    producto = get_object_or_404(Producto, id=id)
    data = {
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Modificado correctamente')
            return redirect(to='productos')
        data['form'] = formulario

    return render(request, 'productos/editar.html', data)

def eliminar(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('productos')



def CatalogoCompleto(request):
    return render(request, 'paginas/CatalogoCompleto.html')
def compra(request):
    return render(request, 'paginas/compra.html')
def SuscFundV2(request):
    return render(request, 'paginas/SuscFundV2.html')
def MicuentaV2(request):
    return render(request, 'paginas/MicuentaV2.html')
def SuscFundV2(request):
    return render(request, 'paginas/SuscFundV2.html')
def FormularioV12(request):
    return render(request, 'paginas/FormularioV12.html')
def MiPedidoV2(request):
    return render(request, 'paginas/MiPedidoV2.html')
def Suscrito1(request):
    return render(request, 'paginas/Suscrito1.html')
def Suscrito2(request):
    return render(request, 'paginas/Suscrito2.html')
def Suscrito3(request):
    return render(request, 'paginas/Suscrito3.html')

class ProductoApiViewSet (ModelViewSet):
   # serializer_class = 
   queryset = Producto.objects.all()