from django.urls import path

from . import views

app_name= "planta"
urlpatterns = [
    path('', views.index,name="index"), 
    #Trabajadores
    path('trabajadores/',views.listarTrabajador, name="listarTrabajador"),
    path ('formularioTrabajador/<int:id>',views.formularioTrabajador, name="formularioTrabajador"),
    path ('guardarTrabajador/',views.guardarTrabajador, name="guardarTrabajador"),
    path ('editarTrabajador/<int:id>',views.editarTrabajador, name= "editarTrabajador"),
    path('eliminarTrabajador/<int:id>',views.eliminarTrabajador, name="eliminarTrabajador"),


    #Categoria


    #Producto

    #Produccion
    


]