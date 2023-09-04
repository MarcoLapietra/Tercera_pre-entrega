from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *


# Create your views here.

def inicio(req):
    return render(req, "inicio.html")   


def curso(req,nombre,profesor):
    
    curso= Cursos(nombre=nombre, profesor=profesor)
    curso.save()
    return HttpResponse


def lista_cursos(req):
    lista = Cursos.objects.all()

    return render(req,'lista-cursos.html',{"lista-cursos":lista})





def cliente(req,nombre,telefono):
    cliente= Cliente(nombre=nombre, telefono=telefono)
    cliente.save()
    return HttpResponse(f"""
            <p>Cliente: {cliente.nombre} creado exitosamente!</p>
                                     
""")


def lista_clientes(req):
    lista = Cliente.objects.all()

    return render(req,'lista-clientes.html',{"lista-clientes":lista})



def mayorista(req,nombre,telefono,nroMayorista):
    mayorista = Mayorista(nombre=nombre, telefono=telefono, nroMayorista=nroMayorista)
    mayorista.save()
    return HttpResponse(f"""
            <p>Cliente: {mayorista.nombre} creado exitosamente!</p>
            """)


def lista_mayorista(req):
    lista = Mayorista.objects.all()

    return render(req,'lista-mayorista.html',{"lista-mayorista":lista})



def formularioCurso(req: HttpResponse):
    
    miFormulario = CursoFormulario(req.POST)
    if miFormulario.is_valid():

        miData=miFormulario.cleaned_data

        curso = Cursos(nombre=miData["curso"], profesor=miData["profesor"])
        curso.save()
        return render(req, "inicio.html", {"mensaje: Curso creado con exito"})
    else:
        miFormulario = CursoFormulario(req.POST)
        return render(req,"formulario-curso.html", {"miFormulario":miFormulario})    



def formularioMayorista(req: HttpResponse):
    
    miFormulario = MayoristaFormulario(req.POST)
    if miFormulario.is_valid():

        miData=miFormulario.cleaned_data

        mayorista = Mayorista(nombre=miData["nombre"], telefono=miData["telefono"], nroMayorista=miData["nroMayorista"])
        mayorista.save()
        return render(req, "inicio.html", {"mensaje: Mayorista creado con exito"})
    else:
        miFormulario = MayoristaFormulario(req.POST)
        return render(req,"formulario_mayorista.html", {"miFormulario":miFormulario})    
     
