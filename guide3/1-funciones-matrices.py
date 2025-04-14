# FUNCIONES CON MATRICES
'''
Desarrollar cada una de las siguientes funciones y escribir un programa que permi-
ta verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada fun-
ción:
'''
def cargarMatriz(filas, columnas):
    '''
    A -Cargar números enteros en una matriz de N x N, ingresando los datos desde
    teclado.
    '''
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            numero = int(input(f"Ingrese el número para la posición ({i + 1}, {j + 1}): "))
            fila.append(numero)
        matriz.append(fila)
        '''
        B - Ordenar en forma ascendente cada una de las filas de la matriz.
        '''
        fila.sort()
    return matriz

def imprimirmatriz(matriz): # Sin usar subíndices (solo lectura)
    for fila in matriz:
        for elemento in fila:
            print("%4d" %elemento, end="")
        print()

def intercambiarFilas(matriz, fila1, fila2):
    '''
    Intercambiar dos filas, cuyos números se reciben como parámetro.
    '''
    # convertir a las filas para basarlas en indice 0 
    fila1 -= 1
    fila2 -= 1
    # Intercambiar las filas en la matriz
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]

def intercambiarColumas(matriz, columna1, columna2):
    '''
    Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
    '''
    columna1 -= 1
    columna2 -= 1
    for i in range(len(matriz)):
        matriz[i][columna1], matriz[i][columna2] = matriz[i][columna2], matriz[i][columna1]

def transponerMatriz(matriz):
    '''
    Transponer la matriz sobre sí misma.
    '''
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(i + 1, columnas):  # Solo iterar sobre la parte superior de la matriz
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]

def calcularPromedioFila(matriz, fila):
    '''
    Calcular el promedio de los elementos de una fila, cuyo número se recibe como parámetro.
    '''
    fila -= 1 # elegir la fila exceptuando que empieza de 0
    if fila < 0 or fila >= len(matriz):
        return 0 # si la fila es invalida
    return sum(matriz[fila]) / len(matriz[fila])

def calcularPorcentajeDeImpares(matriz, columna):
    '''
    Calcular el porcentaje de elementos con valor impar en una columna, cuyo nú-
    mero se recibe como parámetro.
    '''
    columna -= 1  # Ajustar el índice para que sea basado en 0
    if columna < 0 or columna >= len(matriz[0]):
        return None  # Retornar None si la columna es inválida
    
    total_elementos = len(matriz)
    contador_impares = sum(1 for fila in matriz if fila[columna] % 2 != 0)

    if total_elementos == 0:
        return 0  # Evitar división por cero

    porcentajeImpares = (contador_impares / total_elementos) * 100
    return porcentajeImpares 

def main():
    filas = int(input("Ingrese el numero de filas: "))
    columnas = int(input("Ingrese el numero de columnas: "))

    # A
    mimatriz = cargarMatriz(filas, columnas)
    imprimirmatriz(mimatriz)

    # C 
    fila1 = int(input("Ingresa la primera fila para realizar el intercambio: "))
    fila2= int(input("Ingresa la segunda fila para realizar el intercambio: "))
    intercambiarFilas(mimatriz, fila1, fila2)
    print("Matriz con las filas intercambiadas: ")
    imprimirmatriz(mimatriz)

    # D
    columna1 = int(input("Ingresa la primera columna para realizar el intercambio: "))
    columna2= int(input("Ingresa la segunda columna para realizar el intercambio: "))
    intercambiarColumas(mimatriz, columna1, columna2)
    print("Matriz con las columnas intercambiadas: ")
    imprimirmatriz(mimatriz)

    # E
    transponerMatriz(mimatriz)
    print("Matriz transpuesta: ")
    imprimirmatriz(mimatriz)

    # F
    promedioFila = int(input("Ingresar el numero de la fila para calcular el promedio: "))
    promedio = calcularPromedioFila(mimatriz, promedioFila)
    print(f"El promedio de los elementos de la fila {promedioFila} es: {promedio}")

    porcentajeColumna = int(input("Calcular el porcentaje de impares en la columna: "))
    porcentaje = calcularPorcentajeDeImpares(mimatriz, porcentajeColumna)
    print(f"Porcentaje de impares en la columna {porcentajeColumna}: {porcentaje}")


# Programa principal
main()