'''
Desarrollar las siguientes funciones utilizando tuplas para representar fechas y ho-
rarios, y luego escribir un programa que las vincule:
a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha
válida.
b. Sumar N días a una fecha.
c. Ingresar un horario desde teclado, verificando que sea correcto.
d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
segundo se considerará que el primero corresponde al día anterior. En ningún
caso la diferencia en horas puede superar las 24 horas.
'''

fecha = input("Ingrese una fecha con el siguiente formato: DD MM AA - ")
tupla_fecha = (fecha.split())

n = int(input("Ingrese la cantidad de días que desea sumar a la fecha: "))
lista_tupla = list(tupla_fecha)

dia = int(lista_tupla[0]) + n
lista_tupla[0] = dia

new_tupla_fecha = tuple(lista_tupla)
print(new_tupla_fecha)

hora = int(input("Ingrese la hora: "))
while hora > 23 or hora < 0:
    hora = int(input("Ingrese una hora valida: "))
minutos = int(input("Ingrese los minutos: "))
while minutos > 59 or minutos < 0:
    minutos = int(input("Ingrese una cantidad de minutos valida: "))
tupla = (hora, minutos)
hora_n2 = int(input("Ingrese la hora: "))
while hora_n2 > 23 or hora_n2 < 0:
    hora_n2 = int(input("Ingrese una hora valida: "))
minutos_n2 = int(input("Ingrese los minutos: "))
while minutos_n2 > 59 or minutos_n2 < 0:
    minutos_n2 = int(input("Ingrese una cantidad de minutos valida: "))
tupla_n2 = (hora_n2, minutos_n2) 
"""
En esta primera parte se crean las tuplas y 
se hace la verificacion de valores
"""
minutos_totales = hora * 60 + minutos
minutos_totales_n2 = hora_n2 * 60 + minutos_n2

if minutos_totales > minutos_totales_n2:
    minutos_totales_n2 = minutos_totales_n2 + 1440 # Se suma 1440 ya que es la cantidad de minutos en un dia
    diferencia_minutos = minutos_totales_n2 - minutos_totales
    print(f"La diferencia es de {diferencia_minutos} minutos.")


elif minutos_totales_n2 > minutos_totales:
    minutos_totales = minutos_totales  + 1440
    diferencia_minutos = minutos_totales - minutos_totales_n2
    print(f"La diferencia es de {diferencia_minutos} minutos.")


else:
    print("Ambos horarios corresponden al mismo momento")

