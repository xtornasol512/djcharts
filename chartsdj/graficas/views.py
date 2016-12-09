# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import ExampleSimple, NotasPorEstado


# Create your views here.
def grafica_simple(request):
    return render(request, "graficas/graficas_view.html", {})

def example_simple_db(request):
    data = ExampleSimple.objects.all()
    return render(request, "graficas/grafica_db.html", {"data": data })

# 24 Estados
# 11 años
# estado_x_anio  conteo
# porcentaje  , total de totales 158. observacion entre el total por 100

def notas_por_estado(request):
    """Datos para notas por estado """
    qs = NotasPorEstado.objects.all()
    estados_x_anios = qs.filter(year="2016")
    mex_total = qs.filter(estado="MEX")





