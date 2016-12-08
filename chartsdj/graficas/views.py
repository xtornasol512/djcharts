# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import ExampleSimple


# Create your views here.
def grafica_simple(request):
    return render(request, "graficas/graficas_view.html", {})

def example_simple_db(request):
    data = ExampleSimple.objects.all()
    return render(request, "graficas/grafica_db.html", {"data": data })