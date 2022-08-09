from django.contrib import admin
from.models import Categoria, Produccion, Producto, Trabajador

# Register your models here.

@admin.register(Trabajador) #decorador
class TrabajadorAdmin (admin.ModelAdmin):
    list_display =('cedula','nombre','apellido','correo','nombreCompleto','id') # para que salgan los campos que se desean
    search_fields=['nombre', 'cedula'] # para buscar, en este caso por nombre y/o cedula
    
    
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display= ('id','nombre','desc')
    
@admin.register(Producto)   
class ProductoAdmin(admin.ModelAdmin):
    list_display =('nombre', 'ficha_tecnica', 'costo', 'categoria', 'descripCategoria')
    search_fields= ['nombre','categoria__nombre'] #'categoria__nombre' se trabaja como un objeto, para buscar por nombre de la categoria ya que es foranea
    list_filter =['categoria']
    #list_editable =['color']# para editar "no me funciona, me daña todo el software"
 
    
    def descripCategoria(self,obj): #para agregar la descripcion de la categoria
        return obj.categoria.desc
    
    
@admin.register(Produccion)
class ProduccionAdmin(admin.ModelAdmin):
    list_display =('trabajador', 'producto', 'cantidad', 'fecha_creation', )

    
    







