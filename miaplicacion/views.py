from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import Entrada, Actividad, Seccion, Usuario

from django.core.mail import send_mail # Para Correo
from django.conf import settings


from django.db.models import Q  # Para implementar la barra de busqueda

from django.http import HttpResponse

from django.template.loader import get_template


from django.contrib.auth import views as auth_views



# BASES######################################
def Base(request):
    return render(request,"Base.html")
def BaseSeccion(request):
    return render(request,"BaseSeccion.html")
##############################################


def Index(request):
    return render(request, "Index.html")

def QueQuiCom(request):
    return render(request,"QueQuiCom.html")

def Estatuts(request):
    return render(request,"Estatuts.html")


# SECCIONS####################################
def Seccions(request):
    return render(request,"Seccions.html")

def Seccion1(request):
    
    return render(request,"Seccion1.html")

def Seccion2(request):
    return render(request,"Seccion2.html")

def Seccion3(request):
    return render(request,"Seccion3.html")

def Seccion4(request):
    return render(request,"Seccion4.html")

##############################################

# CONTACTO####################################
def FormularioContacto(request):
    return render(request, "FormularioContacto.html")

def contactoExitoso(request):
    if request.method == "POST":
      asunto=request.POST["txtNom"]
      mensaje=request.POST["txtMissatge"] + " /Email: " + request.POST["txtEmail"]
      email_desde=settings.EMAIL_HOST_USER
      email_para=["caraculitodemar@gmail.com"]
      send_mail(asunto,mensaje,email_desde,email_para, fail_silently=False)
      return render(request, "contactoExitoso.html")
    return render(request, "FormularioContacto.html")
##############################################

##BLOG#########################################

class BlogListView(ListView):
    model=Entrada
    template_name='Index.html'
    paginate_by= 2

class EntradaDetailView(DetailView):
    model=Entrada
    template_name='entrada_detail.html'

# override context data
    def get_context_data(self, *args, **kwargs):
        context = super(EntradaDetailView,
             self).get_context_data(*args, **kwargs)
        # add extra field 
        #context["category"] = "MISC"        
        return context

class SearchResultsView(ListView): # Creamos la clase para filtrar las busqueda
    model = Entrada
    template_name = 'search_results.html'

    def get_queryset(self): # Para filtrar los querysets

        query = self.request.GET.get('Busqueda')

        if query:
            lista_de_objetos = Entrada.objects.filter(
            Q(titulo__icontains = query) | Q(contenido__icontains= query)
            )
        return lista_de_objetos
##############################################

def sign(request):
    return render(request, "sign.html")

##USUARIO######################################
def usuario(request, Nombre_id):
    #Obtiene el usuario que esta en linea
    usuarios=Usuario.objects.get(pk=Nombre_id) #Use of "id" instead of "pk", causes error when there is a primary key in the table that is not called "id"
    
    #total_actividades=actividades.filter().count()
    
    print(usuarios)
    print(Nombre_id)
   
    
    #context ={
        #'usuarios':usuarios,
        #'actividades':actividades,
        #'total_actividades':total_actividades
   # }

    context={}
    system=request.POST.get('system',None)
    if request.method == 'POST':
        
        #Introduce al usuario en la actividad con un click
        obj=Actividad.objects.get(Nombre_Actividad__iexact=system)
        obj.usuarioActividad.add(Nombre_id)
        

    
    #Filtra los querysets a los que el usuario se ha inscrito
    usuarioactividad=Actividad.objects.filter(usuarioActividad=usuarios)
    actividad=Actividad.objects.all()
    print(usuarioactividad)



    context ={
    
    'usuarioactividad':usuarioactividad,
    'actividad':actividad
    #'total_actividades':total_actividades
    }

    return render(request,"usuario.html", context)   

    
    #return HttpResponse ("""<html><script>window.location.replace('/');</script></html>""")

class Seccion1ListView(ListView):
    model=Actividad
    template_name='Seccion1.html'

    def get_queryset(self):
        queryset = Actividad.objects.filter(seccion="escalada")
        return (queryset)




###############################################




    