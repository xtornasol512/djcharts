from django.shortcuts import render

# Create your views here.
def grafica_simple(request):
    return render(request, "graficas/graficas_view.html", {})