from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import Template, Context
import sqlite3 as sql
from django.core.mail import send_mail
from django.conf import settings
from Plankton.models import Producto, Usuario, Categoria
from  .forms import UsuarioRegForm, ProductoRegForm, FormContacto, UserCreationForm
from rest_framework import viewsets
from rest_producto.serializers import ProductoSerializer, CategoriaSerializer
import requests
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes



# Create your views here.

@permission_classes((IsAuthenticated,))
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        productos = Producto.objects.all()
        nombre = self.request.GET.get('nombre')
        destacado = self.request.GET.get('destacado')
        oferta = self.request.GET.get('oferta')
        categoria = self.request.GET.get('categoria')
        idProducto = self.request.GET.get('identificador')

        if nombre:
            productos = productos.filter(nombre__contains=nombre)

        elif destacado:
            productos = productos.filter(destacado=True)

        elif oferta:
            productos = productos.exclude(descuento=0)

        elif categoria:
            productos = productos.filter(categoria=categoria)

        elif idProducto:
            productos = productos.filter(idProducto=idProducto)
    
        return productos
               
@permission_classes((IsAuthenticated,))
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    def get_queryset(self):
        categorias = Categoria.objects.all()
        nombre = self.request.GET.get('nombre')

        if nombre:
            categorias = categorias.filter(nombre__contains=nombre)
        
        return categorias

def index(request):
    response=requests.get('http://127.0.0.1:8000/api/v2/productos/?destacado=true', headers={'Authorization': 'Token 8d1f99e9f7a579185f647a84d3532ee581cad43c'}).json()
    return render(request, 'Plankton/index.html', {'productos':response})

def nosotros(request):
    return render(request, 'Plankton/nosotros.html')

def tienda(request):
    response=requests.get('http://127.0.0.1:8000/api/v2/productos/', headers={'Authorization': 'Token 8d1f99e9f7a579185f647a84d3532ee581cad43c'}).json()
    return render(request, 'Plankton/tienda.html', {'productos':response})

def donacion(request):
    return render(request, 'Plankton/donacion.html')

def faq(request):
    return render(request, 'Plankton/faq.html')

def pagoexitoso(request):
    return render(request, 'Plankton/pagoexitoso.html')



def producto(request, id):
    response=requests.get('http://127.0.0.1:8000/api/v2/productos/?identificador='+str(id), headers={'Authorization': 'Token 8d1f99e9f7a579185f647a84d3532ee581cad43c'}).json()
    context = {'selectprod': response}
    return render(request, 'Plankton/producto.html', context)

def contacto(request):
    if request.method=="POST":
        form=FormContacto(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            send_mail(info['asunto'],"Nombre: " + info['nombre'] + "\nCorreo: " + info['correo'] + "\nMensaje: " + info['mensaje'],
            info.get('correo',''),['luyinnag@gmail.com'],)
            return render(request, 'Plankton/index.html')
    else:
        form=FormContacto()
    
    return render(request, 'Plankton/contacto.html', {"form":form})

def registro(request):
    context={'form':UserCreationForm}
    if request.method=='POST':
        formulario=UserCreationForm(request.POST)
        if formulario.is_valid():    
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            if user is not None:
                login(request, user)
                return redirect(to="index")
        else:
            print("Error. Ya existe")
        context['form'] = formulario
    return render(request, 'registration/registro.html', context)

@permission_required('Plankton.view_producto', login_url="../accounts/login")
def listaproductos(request):
    response=requests.get('http://127.0.0.1:8000/api/v2/productos/', headers={'Authorization': 'Token 8d1f99e9f7a579185f647a84d3532ee581cad43c'}).json()
    return render(request, 'Plankton/listaproductos.html', {'productos':response})

def listausuarios(request):
    
    return render(request, 'Plankton/listausuarios.html')

@permission_required('Plankton.add_producto', login_url="../accounts/login")
def productoregistro(request):
    context={'form':ProductoRegForm}
    if request.method=='POST':
        formulario=ProductoRegForm(request.POST, request.FILES)
        if formulario.is_valid():    
            formulario.save()
            return redirect(to='listaproductos')
    return render(request, 'Plankton/productoregistro.html', context)

@permission_required('Plankton.change_producto', login_url="../accounts/login")
def modificarproducto(request, id):
    producto=Producto.objects.get(idProducto=id)
    contexto={
        'form':ProductoRegForm(instance=producto)
    }
    if request.method=='POST':
        formulario=ProductoRegForm(request.POST, request.FILES, instance=producto)
        if formulario.is_valid():    
            formulario.save()
            return redirect(to='listaproductos')
        
    return render(request, 'Plankton/modificarproducto.html', contexto)

@permission_required('Plankton.delete_producto', login_url="../accounts/login")
def eliminarproducto(request, id):
    producto=Producto.objects.get(idProducto=id)
    producto.delete()
    return redirect(request.META['HTTP_REFERER'])

def borrarDestacados(request):
    productolista=Producto.objects.filter(destacado=True)
    for producto in productolista:
        producto.destacado = False
        producto.save()
    return redirect(request.META['HTTP_REFERER'])

def tiendaplantas(request):
    response=requests.get('http://127.0.0.1:8000/api/v2/productos/?categoria=1', headers={'Authorization': 'Token 8d1f99e9f7a579185f647a84d3532ee581cad43c'}).json()
    return render(request, 'Plankton/tiendaplantas.html', {'productos':response})

def tiendaherramientas(request):
    response=requests.get('http://127.0.0.1:8000/api/v2/productos/?categoria=2', headers={'Authorization': 'Token 8d1f99e9f7a579185f647a84d3532ee581cad43c'}).json()
    return render(request, 'Plankton/tiendaherramientas.html', {'productos':response})

def tiendaaccesorios(request):
    response=requests.get('http://127.0.0.1:8000/api/v2/productos/?categoria=3', headers={'Authorization': 'Token 8d1f99e9f7a579185f647a84d3532ee581cad43c'}).json()
    return render(request, 'Plankton/tiendaaccesorios.html', {'productos':response})

def tiendaofertas(request):
    response=requests.get('http://127.0.0.1:8000/api/v2/productos/?oferta=0', headers={'Authorization': 'Token 8d1f99e9f7a579185f647a84d3532ee581cad43c'}).json()   
    return render(request, 'Plankton/tiendaofertas.html', {'productos':response})