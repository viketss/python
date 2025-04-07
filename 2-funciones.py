# FUNCIONES
'''
2. Escribir funciones para:
a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa
a través del teclado.
b. Recibir una lista como parámetro y devolver True si la misma contiene algún
elemento repetido. La función no debe modificar la lista.
c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
únicos de la lista original, sin importar el orden.
Combinar estas tres funciones en un mismo programa.
'''

import random
lista = []

def lista_numeros_random(cantidad):
    '''
    Generar una lista de N números aleatorios del 1 al 100.
    '''
    lista = []
    for i in range(cantidad):
        numero = random.randint(1, 100)
        lista.append(numero)
    return lista

def contiene_repetidos(lista):
    '''
    Recibir una lista como parámetro y devolver True si la misma contiene algún
    elemento repetido.
    '''
    # Iterar sobre cada elemento en la lista
    for elemento in lista:
        # Usar count() para verificar si el elemento aparece más de una vez
        if lista.count(elemento) > 1:
            return True  # Si se encuentra un duplicado, devolver True
    return False  # Si no se encuentran duplicados, devolver False

def eliminar_repetidos(lista):
    '''
    Recibir una lista como parámetro y devolver una nueva lista con los elementos
    únicos de la lista original, sin importar el orden.
    '''
    lista_unicos = []  # Crear una nueva lista para almacenar elementos únicos
    for elemento in lista:
        if elemento not in lista_unicos:  # Verificar si el elemento ya está en la lista de únicos
            lista_unicos.append(elemento)  # Agregar el elemento si no está presente

    return lista_unicos  # Devolver la nueva lista con elementos únicos

cantidad_numeros = int(input('Ingresar cantidad de numeros: '))
lista_numeros = lista_numeros_random(cantidad_numeros)
print('Numeros: ', lista_numeros)
print('Hay numeros repetidos?', contiene_repetidos(lista_numeros))
print('Lista de elementos unicos: ', eliminar_repetidos(lista_numeros))

