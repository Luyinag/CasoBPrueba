from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, nosotros, tienda, donacion, faq, pagoexitoso, producto, contacto, usuarioreg, listaproductos, listausuarios, productoregistro, modificarproducto, eliminarproducto

urlpatterns = [
    path('', index, name="index"),
    path('Plankton/nosotros.html', nosotros, name="nosotros"),
    path('Plankton/tienda.html', tienda, name="tienda"),
    path('Plankton/donacion.html', donacion, name="donacion"),
    path('Plankton/faq.html', faq, name="faq"),
    path('Plankton/pagoexitoso.html', pagoexitoso, name="pagoexitoso"),
    path('Plankton/producto.html', producto, name="producto"),
    path('Plankton/contacto.html', contacto, name="contacto"),
    path('Plankton/usuarioreg.html', usuarioreg, name="usuarioreg"),
    path('Plankton/listaproductos.html', listaproductos, name="listaproductos"),
    path('Plankton/listausuarios.html', listausuarios, name="listausuarios"),
    path('Plankton/productoregistro.html', productoregistro, name="productoregistro"),
    path('Plankton/modificarproducto.html/<id>', modificarproducto, name="modificarproducto"),
    path('Plankton/eliminarproducto.html/<id>', eliminarproducto, name="eliminarproducto"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)