# TEATRO/CINE
'''
Desarrollar un programa que permita realizar reservas en una sala de cine de N
filas con M butacas por cada fila. Desarrollar las siguientes funciones y utilizarlas
en un mismo programa:
mostrar_butacas: Mostrará por pantalla el estado de cada una de las butacas
del cine. Esta función deberá ser invocada antes de que se realice la reserva, y
se volverá a invocar luego de la misma con los estados actualizados.
reservar: Deberá recibir una matriz y la butaca seleccionada, y actualizará la
sala en caso de estar disponible dicha butaca. La función devolverá True/False
si logró o no reservar la butaca.
cargar_sala: Recibirá una matriz como parámetro y la cargará con valores
aleatorios para simular una sala con butacas ya reservadas.

butacas_libres: Recibirá como parámetro la matriz y retornará cuántas buta-
cas desocupadas hay en la sala.

butacas_contiguas: Buscará la secuencia más larga de butacas libres conti-
guas en una misma fila y devolverá las coordenadas de inicio de la misma.
'''
import random

def crearSalaCine(filas, butacas):
    '''
    Crear sala de cine con filas y butacas
    '''
    matrizSala = []
    for i in range(filas):
        fila = []
        for j in range(butacas): # columnas
            fila.append("0")
        matrizSala.append(fila)
        '''
        B - Ordenar en forma ascendente cada una de las filas de la matriz.
        '''
        fila.sort()
    return matrizSala

def imprimirSalaDeCine(matrizSala): 
    for fila in matrizSala:
        for elemento in fila:
            print("%4s" %elemento, end="")
        print()

def mostrarButacas(sala):
    print("\nButacas disponibles:")
    for pos, fila in enumerate(sala):
        print(f"Fila {pos + 1}: " + " ".join(fila)) # transforma en strings
    print()

def reservarButaca(sala, fila, butaca):
    fila -= 1
    butaca -= 1
    if sala[fila][butaca] == 'X':
        return False # la butaca ya esta reservada
    else:
        sala[fila][butaca] = 'X' # marcar la butaca como reservada
        return True
    
'''
cargar_sala: Recibirá una matriz como parámetro y la cargará con valores
aleatorios para simular una sala con butacas ya reservadas.
'''
def cargarSalaRandom(sala):
    filas = int(input("Ingresa la cantidad de filas: "))
    butacas = int(input("Ingresa la cantidad de butacas: "))
    sala = crearSalaCine(filas, butacas)
    for fila in range(filas):
        for columna in range(butacas):
            num = random.choice(["0", "X"])
            sala[fila][columna] = num  # Ingresar el valor random en la posición actual
    return sala # Retornar la sala actualizada

def butacasLibres(matriz):
    return sum(fila.count('0') for fila in matriz) #cuenta butacas libres

def main():
    filas = int(input("Ingresar la cantidad de filas de la sala: "))
    butacas = int(input("Ingresar la cantidad de butacas de la sala: "))
    salaCine = crearSalaCine(filas, butacas)
    
    mostrarButacas(salaCine)

    # Solicitar la fila y columna para reservar
    fila = int(input("Ingrese el número de la fila que desea reservar: ")) 
    butaca = int(input("Ingrese el número de la butaca que desea reservar: "))

    # Verificar que la fila y columna sean válidas
    if fila < 0 or fila >= filas or butaca < 0 or butaca >= butacas:
        print("Número de fila o butaca inválido. Intente de nuevo.")

    # Realizar la reserva
    if reservarButaca(salaCine, fila, butaca):
        print("Reserva realizada con éxito.")
    else:
        print("La butaca ya está reservada. Por favor, elige otra.")

    # Mostrar el estado actualizado de las butacas
    mostrarButacas(salaCine)

    salaRandom = cargarSalaRandom(salaCine)
    print("Sala random: ")
    imprimirSalaDeCine(salaRandom)

    print("Butacas libres: ", butacasLibres(salaRandom))


# PROGRAMA PRINCIPAL
main()




