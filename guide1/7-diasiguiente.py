# DIA SIGUIENTE
'''
Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones
ni agregados, desarrollar programas que permitan:
a. Sumar N días a una fecha.
b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.
'''
def diasiguiente(dia, mes, año):
    # Días en cada mes (enero a diciembre)
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Verificar si el año es bisiesto
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        dias_por_mes[1] = 29  # Si es bisiesto, febrero tiene 29 días (posicion 1)
    
    dia += 1  # Sumar un día al día actual
    # Comprobar si el día excede el número de días del mes actual
    if dia > dias_por_mes[mes - 1]:  
        dia = 1  # Reiniciar el día a 1
        mes += 1  # Pasar al siguiente mes
        # Comprobar si el mes excede diciembre
        if mes > 12:  
            mes = 1  # Reiniciar el mes a enero
            año += 1  # Incrementar el año en 1
    
    return dia, mes, año  # Devolver el nuevo día, mes y año

def sumar_dias(dia, mes, año, cantdias):
    # Sumar N días a la fecha dada
    for i in range(cantdias):  # Repetir cant-dias veces
        dia, mes, año = diasiguiente(dia, mes, año)  # Calcular el día siguiente
    return dia, mes, año  # Devolver la nueva fecha

def dias_entre_fechas(dia1, mes1, año1, dia2, mes2, año2):
    # Calcular la cantidad de días entre dos fechas
    dias_contados = 0  # Inicializar el contador de días
    # Mientras las dos fechas no sean iguales
    while (dia1, mes1, año1) != (dia2, mes2, año2):
        dia1, mes1, año1 = diasiguiente(dia1, mes1, año1)  # Calcular el día siguiente
        dias_contados += 1  # Incrementar el contador de días
    return dias_contados  # Devolver la cantidad de días contados

# Ejemplo de uso
# Sumar N días a una fecha
dia = int(input("Ingresar el dia: "))
mes = int(input("Ingresar el mes: "))
año = int(input("Ingresar el año: "))
print(f'Fecha actual: {dia}/{mes}/{año}')

num_dias = int(input('ingresar dias a sumar: '))
nueva_fecha = sumar_dias(dia, mes, año, num_dias)  # Llamar a la función para sumar días
print(f"Fecha después de sumar {num_dias} días: {nueva_fecha}")  # Imprimir la nueva fecha

# Calcular días entre dos fechas
dia1, mes1, año1 = 1, 1, 2023  # Primera fecha
dia2, mes2, año2 = 1, 2, 2023  # Segunda fecha
dias = dias_entre_fechas(dia1, mes1, año1, dia2, mes2, año2)  # Llamar a la función para contar días
print(f"Días entre {dia1}/{mes1}/{año1} y {dia2}/{mes2}/{año2}: {dias}")  # Imprimir la cantidad de días