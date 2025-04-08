# MATRIZ CON NUM ALEATORIOS
'''
Desarrollar un programa para rellenar una matriz de N x N con números enteros al
azar comprendidos en el intervalo [0,N2), de tal forma que ningún número se repi-
ta. Imprimir la matriz por pantalla.
'''
import random

def crearMatriz(filas, columas):

    matriz = [] # crear una matriz vacia
    for f in range(filas):
        fila = [] # nueva fila vacía (lista)
        for c in range(columnas):
            fila.append(0) # agrega elementos a la fila vacía
        matriz.append(fila) # Agrega fila a la matriz
    return matriz

def rellenarMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    num = int(input('Ingresar un numero random para generar numeros en la matriz: '))
    for f in range(filas):
        for c in range (columnas):
            numAleatorio = random.randint(0, num**2)
            matriz[f][c] = numAleatorio #Ingresar el num en la posicion actual
    return matriz

filas = int(input('Ingresar cantidad de filas: '))
columnas = int(input('Ingresar cantidad de columnas: '))
mimatriz = crearMatriz(filas, columnas)
print(mimatriz)

matriz_rellena = rellenarMatriz(mimatriz)
print('Matriz con datos aleatorios de 0 al numero dado (cada valor elevado al cuadrado): ', matriz_rellena)


