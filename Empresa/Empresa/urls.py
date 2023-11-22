"""
URL configuration for Empresa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from AppEmpresa import views as app1
from Personal import views as app2
from Transporte import views as app3

urlpatterns = [
    path('admin/', admin.site.urls),
    path('render/', app1.renderTemplate),
    path("hola/", app1.display),
    path("ahora/", app1.displayDateTime),
    path("productos/", app1.productoData),
    #path("", productoRegistrationView),
    path('', app1.index),
    path('producto/', app1.listadoProductos),
    path('agregarProducto/', app1.agregarProducto),
    path('eliminarProducto/<int:id>', app1.eliminarProducto),
    path('actualizarProducto/<int:id>', app1.actualizarProducto),
    # Rutas de la aplicación Personal
    path('personal/', app2.listadoPersonal, name='listado_personal'),
    path('agregarpersonal/', app2.agregarPersonal, name='agregar_personal'),
    path('eliminarpersonal/<int:id>/', app2.eliminarPersonal, name='eliminar_personal'),
    path('actualizarpersonal/<int:id>/', app2.actualizarPersonal, name='actualizar_personal'),

    # Rutas de la aplicación Transporte
    path('transportes/', app3.listadoTransportes, name='listado_transportes'),
    path('agregartransporte/', app3.agregarTransporte, name='agregar_transporte'),
    path('eliminartransporte/<int:id>/', app3.eliminarTransporte, name='eliminar_transporte'),
    path('actualizartransporte/<int:id>/', app3.actualizarTransporte, name='actualizar_transporte'),
]
