# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import ExampleSimple, NotasPorEstado, NotasPeriodico


# Create your views here.
def grafica_simple(request):
    return render(request, "graficas/graficas_view.html", {})

def example_simple_db(request):
    data = ExampleSimple.objects.all()
    return render(request, "graficas/grafica_db.html", {"data": data })

# 24 Estados
ESTADOS = ["AGU", "BCN", "BCS", "CHH", "CMX", "COA", "COL", "DUR", "GRO", "GUA", "JAL", "MEX", "MIC", "MOR", "NAY", "NLE", "OAX", "PUE", "QUE", "SIN", "SON", "TAM", "VER", "ZAC"]
# 11 años
ANIOS = range(2006,2017)

# estado_x_anio  conteo
# porcentaje  , total de totales 158. observacion entre el total por 100
def notas_por_estado(request):
    """Datos para notas por estado """
    qs = NotasPorEstado.objects.all()
    dicc = {}
    lista_obj = []
    for estado in ESTADOS:
        lista_obj = []
        suma = 0
        for year in ANIOS:
            obj = qs.filter(estado=estado).get(year=year)
            lista_obj.append(obj)
            percent = (obj.sucesos / 158.0 ) * 100
            suma += percent
        lista_obj.append(suma)
        dicc[estado] = lista_obj
    print dicc["AGU"][:-1]
    return render(request,"graficas/grafica_sucesos_estado.html",{"data": dicc,"years": ANIOS, "estados": ESTADOS})

