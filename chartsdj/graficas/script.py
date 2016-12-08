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
