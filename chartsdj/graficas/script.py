from graficas.models import ExampleSimple
import random

def numRam():
    return random.uniform(0.0, 5.0)

direccion = "N"
for n in range(0,16):
    name = direccion + str(n)
    dato = ExampleSimple(direccion=name,
                         float_1= numRam(),
                         float_2= numRam(), 
                         float_3= numRam(),
                         float_4= numRam(), 
                         float_5= numRam(), 
                         float_6= numRam(), 
                         float_7= numRam(),
                         )
    dato.save()

print("Creado exitoso!")

from graficas.models import NotasPeriodico
from graficas.models import NotasPorEstado

# 24 Estados
ESTADOS = ["AGU", "BCN", "BCS", "CHH", "CMX", "COA", "COL", "DUR", "GRO", "GUA", "JAL", "MEX", "MIC", "MOR", "NAY", "NLE", "OAX", "PUE", "QUE", "SIN", "SON", "TAM", "VER", "ZAC"]
# 11 años
ANIOS = range(2006,2017)

for estado in ESTADOS: # Estados
    suma_list = []
    name = estado
    for i in ANIOS: #años
        q = NotasPorEstado.objects.filter(estado=estado).get(year=i) 
        suma_list.append(q.sucesos)
        print estado
    print suma_list
    nuevo = NotasPeriodico(name, suma_list[0],suma_list[1],suma_list[2], suma_list[3], suma_list[4], suma_list[5],
                           suma_list[6], suma_list[7], suma_list[8], suma_list[9], suma_list[10])
    nuevo.save()
