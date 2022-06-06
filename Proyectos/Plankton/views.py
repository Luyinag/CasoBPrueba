from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Template, Context
import sqlite3 as sql
from Plankton.models import Producto, Usuario
from    .forms import UsuarioRegForm, ProductoRegForm

# Create your views here.

def index(request):
    return render(request, 'Plankton/index.html')

def nosotros(request):
    return render(request, 'Plankton/nosotros.html')

def tienda(request):
    return render(request, 'Plankton/tienda.html')

def donacion(request):
    return render(request, 'Plankton/donacion.html')

def faq(request):
    return render(request, 'Plankton/faq.html')

def pagoexitoso(request):
    return render(request, 'Plankton/pagoexitoso.html')

def producto(request):
    return render(request, 'Plankton/producto.html')

def contacto(request):
    return render(request, 'Plankton/contacto.html')

def usuarioreg(request):
    context={'form':UsuarioRegForm}
    if request.method=='POST':
        formulario=UsuarioRegForm(request.POST)
        if formulario.is_valid():    
            formulario.save()
            context['message']="Se ha registrado con éxito"
        else:
            print("Error. Ya existe")
    return render(request, 'Plankton/usuarioreg.html', context)

def listaproductos(request):
    productos=Producto.objects.all()
    context={
        'productos':productos
    }
    return render(request, 'Plankton/listaproductos.html', context)

def listausuarios(request):
    
    return render(request, 'Plankton/listausuarios.html')

def productoregistro(request):
    context={'form':ProductoRegForm}
    if request.method=='POST':
        formulario=ProductoRegForm(request.POST, request.FILES)
        if formulario.is_valid():    
            formulario.save()
            context['message']="Se ha registrado con éxito"
        else:
            print("Error. Ya existe")
    return render(request, 'Plankton/productoregistro.html', context)

def modificarproducto(request, id):
    producto=Producto.objects.get(idProducto=id)
    contexto={
        'form':ProductoRegForm(instance=producto)
    }
    if request.method=='POST':
        formulario=ProductoRegForm(request.POST, request.FILES, instance=producto)
        if formulario.is_valid():    
            formulario.save()
            contexto['mensaje'] = "Modificao"
            return redirect(to='listaproductos')
        
    return render(request, 'Plankton/modificarproducto.html', contexto)

def eliminarproducto(id):
    producto=Producto.objects.get(idProducto=id)
    producto.delete()
    return redirect(to='listaproductos')