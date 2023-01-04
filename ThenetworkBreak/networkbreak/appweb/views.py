from importlib.resources import path
import re
import pandas as pd

from sqlite3 import enable_shared_cache
from django.shortcuts import render, get_object_or_404, redirect
from .models import Persons, Archivo, ImagenesModelo
from .forms import FormularioForm
from django.conf import settings


def index(request):
    Top1Women = Persons.objects.filter(genero="2")[:1]
    Top1men = Persons.objects.filter(genero="1")[:1]
    data = {
        'Top1Women': Top1Women,
        'Top1men': Top1men
    }

    return render(request, 'appweb/index.html', data)


def profile(request, id):
    modelo = get_object_or_404(Persons, id=id)
    photos = ImagenesModelo.objects.filter(modelo=modelo)
    data = {
        'modelo': modelo,
        'photos': photos

    }
    print(data)
    return render(request, 'appweb/profile.html', data)


def tableform(request):

    if request.method == "POST":
        formulario = FormularioForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()

    modelos = Persons.objects.all()
    data = {
        'modelos': modelos,
        "form": FormularioForm(),
    }

    return render(request, 'appweb/tableform.html', data)


def editarModelo(request, id):
    modelo = get_object_or_404(Persons, id=id)

    data = {
        'form': FormularioForm(instance=modelo)
    }
    if request.method == "POST":
        formulario = FormularioForm(
            data=request.POST, instance=modelo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="tableform")
        else:
            data["form"] = formulario

    return render(request, 'appweb/editarModelo.html', data)


def eliminarModelo(request, id):
    modelo = get_object_or_404(Persons, id=id)
    modelo.delete()
    return redirect(to="tableform")


def actualizar(request):
    if request.method == "POST":
        file = request.FILES["files"]
        obj = Archivo.objects.create(
            file=file
        )
        path = str(obj.file)
        path = (f'{settings.BASE_DIR}/media/{path}')
        df = pd.read_excel(path)
        diccionario = df.set_index('nombre').T.to_dict('list')
        for i in diccionario:
            valor = diccionario[i]
            valor = str(valor)
            valor = valor.replace('[', "")
            valor = valor.replace(']', "")
            nombre = i
            print(nombre, valor)
            datoActualizar = Persons.objects.get(nombre=nombre)
            datoActualizar.valor = int(valor)
            datoActualizar.save()

    return render(request, "appweb/actualizar.html")


def menmodel(request):
    Top1men = Persons.objects.filter(genero="1")[:1]
    personas = Persons.objects.filter(genero="1")[1:30]
    data = {
        'personas': personas,
        'Top1men': Top1men
    }
    return render(request, 'appweb/menmodel.html', data)


def womenmodel(request):
    Top1Women = Persons.objects.filter(genero="2")[:1]
    personas = Persons.objects.filter(genero="2")[1:30]
    data = {
        'Top1Women': Top1Women,
        'personas': personas
    }

    return render(request, 'appweb/womenmodel.html', data)

def allmodeltop30(request):
    allTop1 = Persons.objects.all()[:1]
    allTop = Persons.objects.all()[1:30]
    data = {
        'allTop1': allTop1,
        'allTop': allTop
    }

    return render(request, 'appweb/allmodeltop30.html', data)
