
'''
Escribir una función que reciba una lista de números enteros como parámetro y la
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las pro-
porciones relativas que cada elemento tiene en la lista original. Desarrollar también
un programa que permita verificar el comportamiento de la función. Por ejemplo,
normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].
'''

def normalizar(lista):
    '''
    Normaliza una lista de números enteros para que todos sus elementos sumen 1.0.
    '''
    total = sum(lista)  # Sumar todos los elementos de la lista
    
    # Si la suma es 0, devolvemos una lista de ceros del mismo tamaño
    if total == 0:
        return [0] * len(lista)

    # Crear una nueva lista donde cada elemento es su proporción respecto al total
    lista_normalizada = []
    for x in lista:
        lista_normalizada.append(x / total)  # Dividir cada elemento por la suma total

    return lista_normalizada  # Devolver la lista normalizada

# Programa para verificar el comportamiento de la función
lista_original = [1, 1, 2]
lista_normalizada = normalizar(lista_original)

print('Lista original:', lista_original)
print('Lista normalizada:', lista_normalizada)
print('Suma de la lista normalizada:', sum(lista_normalizada))  # Debería ser 1.0

# Ejemplo adicional
lista_adicional = [10, 20, 30]
lista_normalizada_adicional = normalizar(lista_adicional)

print('Lista original adicional:', lista_adicional)
print('Lista normalizada adicional:', lista_normalizada_adicional)
print('Suma de la lista normalizada adicional:', sum(lista_normalizada_adicional))  # Debería ser 1.0