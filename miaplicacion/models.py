
from django.db import models
# Models Blog
from django.template.defaultfilters import slugify
# Models Usuario/Activida/Seccion
from django.db import models
from django.contrib.auth.models import User



# Models Blog

class Entrada(models.Model):
    titulo  = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_contenido=models.DateTimeField()
    imagen= models.ImageField(upload_to="static/images/fotospost")
    slug= models.SlugField(max_length=255, unique=True, editable=False)
    
   
    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if not self.id:
             self.slug=slugify(self.titulo)
        super(Entrada, self).save(*args, **kwargs)


# Models Usuario/Activida/Seccion.

class Seccion(models.Model):
     Nombre_Sección=models.CharField(max_length=30, primary_key=True)
     Nombre_Responsable=models.CharField(max_length=30)

     def __str__(self):
         #txt = "{0} (Responsable {1})"
         #return txt.format(self.Nombre_Sección, self.Nombre_Responsable)
         txt = "{0}"
         return txt.format(self.Nombre_Sección)
     


class Usuario(models.Model):

     Nombre=models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True) #Para linkar la base de datos de django con el modelo que tengo: Usamos el campo OneToOneField
     Dni=models.CharField(max_length=9)
     Fecha_Nacimiento=models.DateField()
     Fecha_Alta_Usuario= models.DateField(auto_now_add=True)
     

     sexos=[('F','Femenino'),('M','Masculino')]
     Sexo=models.CharField(max_length=1, choices=sexos, default='F')


     seccion=models.ForeignKey(Seccion, null=False, blank=False, on_delete=models.CASCADE)
     Vigencia=models.BooleanField(default=True)


     def __str__(self):
         txt="{0}"
         return txt.format(self.Nombre)

     def nombreCompleto (self):

         txt= "{0}{1},{2}"
         return txt.format(self.Nombre,self.Dni,self.Fecha_Nacimiento)
        


class Actividad(models.Model):
    Codigo= models.CharField(max_length=30)
    Nombre_Actividad=models.CharField(max_length=50,primary_key=True)
    Fecha_Actividad=models.DateTimeField()
    Numero_Usuarios=models.PositiveSmallIntegerField(default=100)

    seccion=models.ForeignKey(Seccion, null=False, blank=False, on_delete=models.CASCADE)
    Descripcion_Actividad=models.CharField(max_length=550)
    usuarioActividad=models.ManyToManyField(Usuario, null= True, blank=True)

     
    def __str__(self):
        return str(self.Nombre_Actividad)

    
    
   


     

