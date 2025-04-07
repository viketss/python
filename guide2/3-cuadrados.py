# CUADRADOS DE LOS NUMEROS
'''
Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos),
donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valo-
res de la lista.
'''

def numeros_cuadrados(cantidad):
    '''
    Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos).
    '''
    lista_numeros = []
    for i in range(1, cantidad + 1):
        cuadrados = i ** 2  # Calcular el cuadrado del número
        lista_numeros.append(cuadrados)  # Agregar el cuadrado a la lista
    return lista_numeros  # Devolver la lista de cuadrados

cantidad_numeros = int(input('Ingresar la cantidad de numeros para la lista: '))
lista_cuadrados = numeros_cuadrados(cantidad_numeros)
print('Lista de cuadrados:', lista_cuadrados)

# Imprimir los últimos 10 valores de la lista
if len(lista_cuadrados) > 10:
    print('Últimos 10 valores:', lista_cuadrados[-10:])
else:
    print('Todos los valores:', lista_cuadrados)

    