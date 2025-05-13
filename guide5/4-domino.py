'''
Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True
o False. Escribir también un programa para verificar su comportamiento. Considerar
el uso de conjuntos para resolver este ejercicio.
'''

#Ejercicio 5
import random
def generarFichas():
    #lado1 = random.randint(1,6)
    #lado2 = random.randint(1,6)
    lado1 = 1
    lado2 = 2
    
    ficha1 = (lado1,lado2)

    #lado4 = random.randint(1,6)
    #lado3 = random.randint(1,6)
    lado3 = 3
    lado4 = 4

    ficha2 = (lado3, lado4)

    return ficha1, ficha2

def conversion_tuplas_a_conjuntos(ficha1,ficha2):
    conjunto = set(ficha1)
    conjunto2 = set(ficha2)
    return conjunto, conjunto2

def verificar_encaje(conjunto, conjunto2):
    union_conjunto = conjunto | conjunto2
    if len(union_conjunto) < 4:
        print("Las fichas encastran")
    else:
        print("Las fichas no encastran") 

ficha1, ficha2= generarFichas()
conjunto, conjunto2 = conversion_tuplas_a_conjuntos(ficha1,ficha2)
verificar_encaje(conjunto, conjunto2)
print(ficha1,ficha2) 
