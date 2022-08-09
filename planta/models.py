#yessi  nombre de ususario
#correo yessi@sena.com
#contrasela yessica
from django.db import models

# Create your models here.

class Trabajador(models.Model):
    cedula = models.IntegerField(unique= True)
    nombre = models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    correo= models.EmailField(max_length=250,null=True,blank= True)
    
    def nombreCompleto(self):
        return f'{self.nombre} {self.apellido}'


    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    

class Categoria(models.Model):
    nombre =models.CharField(max_length=100)
    desc =models.CharField(max_length=254, null=True, blank=True) #para que no esea obligatorio llenar el campo
    
    def __str__(self):
        return f"{self.nombre} "

class Producto(models.Model):
    nombre= models.CharField(max_length=100,unique=True)
    ficha_tecnica= models.TextField()
    costo = models.IntegerField()
    categoria =models.ForeignKey(Categoria, on_delete= models.DO_NOTHING) # para crear llave foranea DO NOTHING para no dejarlo borrar
    COLOR =(
        ('r','Rojo'),
        ('v','Verde'),
        ('a','Azul'), #para que el ususario agrege bajo las condiciones que yo neecesito, o sea que elija solo las opciones que le doy
    )
    color = models.CharField(max_length=100, choices=COLOR, default='r')
   
    
    def __str__(self):
        return f"{self.nombre} "
    
    
class Produccion (models.Model):
    trabajador =models.ForeignKey(Trabajador, on_delete= models.DO_NOTHING)
    producto =models.ForeignKey(Producto, on_delete= models.DO_NOTHING)
    cantidad = models.IntegerField()
    fecha_creation= models.DateTimeField()
    
    
    def __str__(self):
        return f"{self.producto} {self.cantidad} "
    
    
    
