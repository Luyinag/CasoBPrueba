from dataclasses import fields
from django import forms
from django.forms import widgets
from django.forms import ModelForm
from .models import Usuario, Producto, Categoria
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UsuarioRegForm(ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Usuario
        fields = ['run', 'correo', 'contrasena', 'nombre', 'apaterno', 'amaterno', 'celular']


class ProductoRegForm(ModelForm):
    descripcion = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'descuento', 'foto', 'destacado', 'categoria']
    

class FormContacto(forms.Form):
    nombre=forms.CharField()
    asunto=forms.CharField()
    correo=forms.EmailField()
    mensaje=forms.CharField(widget=forms.Textarea)

class CustomCreationForm(UserCreationForm):
    pass

