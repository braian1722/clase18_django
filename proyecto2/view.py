from django.http import HttpResponse
from django.template import loader
from appcoder.models import curso
def home(self, name):
    return HttpResponse (f"hola soy {name}")

def homepage(self):
    lista = [1,2,3,4,5,7,8,9,10]
    data = {"nombre":"braian","apellido":"kandyba","lista":lista}
    

    planilla =loader.get_template("home.html")  #carga la ruta
    documento = planilla.render(data)
    return HttpResponse(documento)


def cursos(self):
    Curso = curso(nonbre ="UX/UI",camada ="12345")
    Curso.save()

    documento = f"curso: {Curso.nonbre}  camada: {Curso.camada}" 
    return HttpResponse(documento)
