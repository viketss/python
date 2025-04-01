#VIAJES DE SUBTE
"""
Una persona desea llevar el control de los gastos realizados al viajar en el subte-
rráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un es-
quema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarro-
llar una función que reciba como parámetro la cantidad de viajes realizados en un
determinado mes y devuelva el total gastado en viajes. Realizar también un pro-
grama para verificar el comportamiento de la función.

Cantidad de viajes Valor del pasaje
1 a 20          Averiguar en Internet el valor actualizado
21 a 30         20% de descuento sobre tarifa máxima
31 a 40         30% de descuento sobre tarifa máxima
Más de 40       40% de descuento sobre tarifa máxima
"""

def viajes(cantidad):
    tarifa = 832
    if cantidad <= 20:
        total = tarifa * cantidad
        print("Total gastado: $", tarifa * cantidad, "en ", cantidad, "viajes\nCada viaje cuesta $", tarifa)
    elif cantidad > 20 and cantidad <= 30:
        total = tarifa * cantidad * 0.8
        print("Total gastado: $", tarifa * cantidad * 0.8, "en ", cantidad, "viajes\nCada viaje cuesta $", tarifa * 0.8)
    elif cantidad > 30 and cantidad <= 40:
        total = tarifa * cantidad * 0.7
        print("Total gastado: $", tarifa * cantidad * 0.7, "en ", cantidad, "viajes\nCada viaje cuesta $", tarifa * 0.7)
    elif cantidad > 40:
        total = tarifa * cantidad * 0.6
        print("Total gastado: $", tarifa * cantidad * 0.6, "en ", cantidad, "viajes \nCada viaje cuesta $", tarifa * 0.6)
    return total


cantidad = int(input("Ingrese la cantidad de viajes realizados en el mes: "))
viajes(cantidad)

