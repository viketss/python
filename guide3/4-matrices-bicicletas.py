# FABRICA DE BICICLETAS
'''
Una fábrica de bicicletas guarda en una matriz la cantidad de unidades producidas
en cada una de sus plantas durante una semana. De este modo, cada columna re-
presenta el día de la semana y cada fila a una de sus fábricas. Ejemplo:
Se solicita:
a. Crear una matriz con datos generados al azar para N fábricas durante una
semana, considerando que la capacidad máxima de fabricación es de 150
unidades por día y puede suceder que en ciertos días no se fabrique nin-
guna.
b. Mostrar la cantidad total de bicicletas fabricadas por cada fábrica.
c. Cuál es la fábrica que más produjo en un solo día (detallar día y fábrica).
d. Cuál es el día más productivo, considerando todas las fábricas combinadas.
e. Crear una lista por comprensión que contenga la menor cantidad fabricada
por cada fábrica.
'''
import random
# FILAS: fabrica N
# COLUMNAS: dia - 0 = lunes \ 1 = martes y asi (hasta sabado)
# DATOS[f][c]: unidades producidas (bicicletas)

# A - crear matriz de produccion con datos aleatorios
def crearMatrizProduccion():
    filas_cantidad_fabricas = int(input('Ingresar cantidad de fabricas (filas de la matriz): '))
    columnas = 6 # dias de la semana
    matriz_produccion = []
    
    for f in range(filas_cantidad_fabricas):
        fila = []
        for c in range(columnas):
            fila.append(random.randint(1, 150)) #meter datos random de produccion de bicis, entre 0 y 150
        matriz_produccion.append(fila)
    return matriz_produccion

def mostrarMatriz(matriz):
    print('Matriz de produccion: ')
    print('Dias: (Lunes) (Martes) (Miercoles) (Jueves) (Viernes) (Sabado)')
    for i, fila in enumerate(matriz):
        print(f'Fabrica {i + 1}: {fila}')

def totalBicicletasPorFabrica(matriz):
    #listas por compresion --> <lista> = [<expresion> for <elemento> in <secuencia>]
    total_por_fabrica = [sum(fila) for fila in matriz]
    return total_por_fabrica 


# c. Cuál es la fábrica que más produjo en un solo día (detallar día y fábrica).
def fabricaMasProductiva(matriz):
    max_produccion = 0
    dia_max = 0
    fabrica_max = 0

    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[f][c] > max_produccion:
                max_produccion = matriz[f][c]
                dia_max = c
                fabrica_max = f

    return fabrica_max + 1, dia_max + 1, max_produccion 

# d. Cuál es el día más productivo, considerando todas las fábricas combinadas.
def diaMasProductivo(matriz):
    total_por_dia = [0] * len(matriz[0])  # cantidad de elementos de la primer fila = cantidad de columnas

    for c in range(len(matriz[0])):
        for f in range(len(matriz)):
            total_por_dia[c] += matriz[f][c]

    dia_max = total_por_dia.index(max(total_por_dia))  # índice del día más productivo
    return dia_max + 1, total_por_dia[dia_max]  # (+1 para que sea más legible)

def menorProduccionPorFabrica(matriz):
    return [min(fila) for fila in matriz]  # lista por comprensión para la menor producción

# PROGRAMA PRINCIPAL
# (a)
mimatriz = crearMatrizProduccion()
mostrarMatriz(mimatriz)

# (b) cantidad total de bicicletas fabricadas por cada fábrica
total_bicicletas = totalBicicletasPorFabrica(mimatriz)
print("\nTotal de bicicletas fabricadas por cada fábrica (por semana):")
for i, total in enumerate(total_bicicletas):
    print(f'Fábrica {i + 1}: {total} bicicletas') # suma de cada fila (fabrica)

# (c) fábrica que más produjo en un solo día
fabrica_max, dia_max, max_produccion = fabricaMasProductiva(mimatriz)
print(f'\nLa fábrica {fabrica_max} produjo la mayor cantidad de bicicletas en un solo día: {max_produccion} bicicletas (Día {dia_max})')

# (d) dia mas productivo
dia_max, total_dia_max = diaMasProductivo(mimatriz)
print(f'\nEl día más productivo fue el día {dia_max} con un total de {total_dia_max} bicicletas producidas.')

# (e) menor cantidad fabricada por cada fábrica
menor_produccion = menorProduccionPorFabrica(mimatriz)
print("\nMenor cantidad fabricada por cada fábrica:")
for i, menor in enumerate(menor_produccion):
    print(f'Fábrica {i + 1}: {menor} bicicletas')
