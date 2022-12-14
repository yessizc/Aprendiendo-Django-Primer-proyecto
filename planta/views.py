from email.policy import HTTP
from multiprocessing import context
import re
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# MENSAJES TIPO COOKIES TEMPORALES
from django.contrib import messages

# PARA GESTIONAR ERRORES EN LA BASE DE DATOS
from django.db import IntegrityError

#para accedser a las consultas de base de datos

from.models import Categoria, Produccion, Producto, Trabajador

# Create your views here.

def index(request):
    return render (request,'planta/index.html')

def listarTrabajador (request):
    q = Trabajador.objects.all() #DICCIONARIO CON LOS DATOS DE TRABAJADOR
    context = {"datos":q}
    return render(request, 'planta/trabajador/listar_trabajador.html',context)

def formularioTrabajador (request, id):
    print(id)
    if id != 0:
        q = Trabajador.objects.get(pk = id) 
        context = {"trabajador":q}
        return render(request, 'planta/trabajador/nuevo_trabajador.html',context)
    else:
        t = {'id':id}
        context = {"trabajador":t}
        return render(request,'planta/trabajador/nuevo_trabajador.html', context)


def guardarTrabajador (request):
    print("save")
    try:
        if request.method=="POST":
        
            q = Trabajador(
                cedula = request.POST["cedula"],
                nombre = request.POST["nombre"],
                apellido = request.POST["apellido"],
                correo = request.POST["correo"],
            )
            q.save()
        #si todo esta bien.
            messages.success(request," El trabajador fue guardado correctamente!")
            #messages.info(request," probando info!")
            #messages.warning(request," probando warning!")
            #messages.debug(request," probando debug")
            #messages.error(request," probando error")
        
        else:
            messages.warning(request,"no se han eviado los datos correctamente...")
    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('planta:listarTrabajador')


def editarTrabajador (request, id):
    print("update")
    try :
        if request.method=="POST":

            trabajador = Trabajador.objects.get(pk = id)
            trabajador.cedula = request.POST["cedula"]
            trabajador.nombre = request.POST ["nombre"]
            trabajador.apellido = request.POST["apellido"]
            trabajador.correo = request.POST["correo"]

            trabajador.save()
            messages.success(request," El trabajador fue editado correctamente!")

        else:
            messages.warning(request,"no se han eviado los datos correctamente...")
    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('planta:listarTrabajador')


def eliminarTrabajador (request, id):
    try:
        print(id)
        trabajador = Trabajador.objects.get(pk = id)
        trabajador.delete()
        messages.success(request," El trabajador se ha eliminado correctamente!")

    except Exception as e:
        messages.error(request,f"error: {e}")
           
    return redirect('planta:listarTrabajador')
    #test




    
