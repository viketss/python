# FUNCIONES RANDOM
'''
Desarrollar cada una de las siguientes funciones y escribir un programa que per-
mita verificar su funcionamiento imprimiendo la lista luego de invocar a cada fun-
ción:

a. Cargar una lista con números al azar de cuatro dígitos. La cantidad de elemen-
tos también será un número al azar de dos dígitos.
b. Calcular y devolver el producto de todos los elementos de la lista anterior.
c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar
se ingresa desde el teclado y la función lo recibe como parámetro. No utilizar
listas auxiliares.
d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50].
'''

import random
lista_random = []

def random_lista():
    cantidad_elementos = random.randint(10,99) 
    for i in range (cantidad_elementos):
        lista_random.append(random.randint(1000,9999))
    print("La lista es: ", lista_random)
    return lista_random

def producto_lista():
    producto = 1
    rango = len(lista_random)
    for i in range (rango):
        producto = producto * lista_random[i]
    print("El producto de la lista es: ", producto)
    return producto

def eliminar_dato(dato):
    for i in range(len(lista_random)):
        if lista_random[i] == dato:
            lista_random.pop(i)
            return True
    return False

def es_capicua(lista_random):
    for i in range(len(lista_random) // 2):
        if lista_random[i] != lista_random[-(i + 1)]:
            return False
    return True

random_lista()
producto_lista()
dato = int(input("Dame un dato para eliminar: "))
print("El dato fue eliminado: ", eliminar_dato(dato))       
eliminar_dato(dato)
es_capicua(lista_random)
print("La lista es capicua: ", es_capicua(lista_random))





