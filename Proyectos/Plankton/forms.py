from dataclasses import fields
from django import forms
from django.forms import widgets
from django.forms import ModelForm
from .models import Usuario, Producto, Categoria


class UsuarioRegForm(ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Usuario
        fields = ['run', 'correo', 'contrasena', 'nombre', 'apaterno', 'amaterno', 'celular']


class ProductoRegForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'foto', 'categoria']

