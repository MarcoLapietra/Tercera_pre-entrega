from django.urls import path, include
from AppCoder.views import *
urlpatterns = [
    path('', inicio, name="Inicio"),
    path('crea-cliente/', cliente),
    path('lista-clientes/',lista_clientes),
    path('crea-mayorista/',mayorista),
    path('lista-mayorista/',lista_mayorista),
    path('formulario-curso/',formularioCurso),
    path('lista-cursos/',lista_cursos),
    path("formulario-mayorista/",formularioMayorista, name='formularioMayorista'),

 
]
