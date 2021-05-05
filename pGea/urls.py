"""pGea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from miaplicacion.views import Base,BaseSeccion,Index,QueQuiCom,Estatuts,Seccions,FormularioContacto,contactoExitoso,Seccions,Seccion1,Seccion2,Seccion3,Seccion4, usuario
#sign
from miaplicacion import views as user_view
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('miaplicacion.urls')),
 
    path('Base/', Base, name='Base'),

    path('BaseSeccion/', BaseSeccion, name='BaseSeccion'),

    path('', Index, name='Index'),

    path('QueQuiCom/', QueQuiCom, name='QueQuiCom'), 

    path('Estatuts/',Estatuts, name='Estatuts'),
    
    path('Seccions/',Seccions, name='Seccions'),

    path('Escalada/', Seccion1, name='Seccion1'),
    
    path('Bici/', Seccion2, name='Seccion2'),

    path('Ski/', Seccion3, name='Seccion3'),

    path('Farigoleros/', Seccion4, name='Seccion4'),

    path('Escalada/', Seccion1, name='Seccion1'),

    path('FormularioContacto/',FormularioContacto, name='FormularioContacto'),

    path('contactoExitoso/', contactoExitoso ),

    path('sign/', auth_views.LoginView.as_view(template_name='sign.html'), name='sign'),

    path('signout/', auth_views.LogoutView.as_view(template_name='signout.html'), name='signout'),

    path('usuario/<Nombre_id>/',usuario, name='usuario'),

  

]




