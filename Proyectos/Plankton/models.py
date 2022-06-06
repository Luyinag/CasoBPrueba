from django.db import models

# Create your models here.

#Modelo Usuarios
class Usuario(models.Model):
    run=models.CharField(primary_key=True, max_length=9, verbose_name="Rut")
    correo=models.CharField(max_length=50, verbose_name="Correo")
    contrasena=models.CharField(max_length=20, verbose_name="Contraseña")
    nombre=models.CharField(max_length=20, verbose_name="Nombre")
    apaterno=models.CharField(max_length=20, verbose_name="Apellido paterno")
    amaterno=models.CharField(max_length=20, verbose_name="Apellido materno")
    celular=models.IntegerField(max_length=9, verbose_name="Celular")

    def __str__(self):
        return self.run

class Categoria(models.Model):
    idCategoria=models.AutoField(primary_key=True, verbose_name="ID Categoria")
    nombreCategoria=models.CharField(max_length=50,verbose_name="Nombre Categoria")

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    idProducto=models.AutoField(primary_key=True,verbose_name="ID Producto")
    nombre=models.CharField(max_length=20,verbose_name="Nombre")
    descripcion=models.CharField(max_length=200, null=True, blank=True, verbose_name="Descripción")
    precio=models.CharField(max_length=10, null=True, blank=True, verbose_name="Precio")
    foto=models.ImageField(upload_to='users/%Y/%m/%d/', height_field=None, width_field=None, max_length=100, verbose_name="Foto")
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre