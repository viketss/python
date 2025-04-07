# IMPRIMIR CALENDARIO
'''
La siguiente función permite averiguar el día de la semana para una fecha determi-
nada. La fecha se suministra en forma de tres parámetros enteros y la función de-
vuelve 0 para domingo, 1 para lunes, 2 para martes, etc. Escribir un programa para
imprimir por pantalla el calendario de un mes completo, correspondiente a un mes
y año cualquiera basándose en la función suministrada. Considerar que la semana
comienza en domingo.
def diadelasemana(dia,mes,año):
if mes < 3:
mes = mes + 10
año = año – 1
else:
mes = mes – 2
siglo = año // 100
año2 = año % 100
diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
if diasem < 0:
diasem = diasem + 7
return diasem
'''

def diadelasemana(dia, mes, año):
    # Ajustar el mes y el año para el cálculo
    if mes < 3:
        mes = mes + 10  # Para enero y febrero, se ajusta el mes
        año = año - 1   # Se decrementa el año
    else:
        mes = mes - 2   # Para otros meses, se ajusta el mes

    # Calcular el siglo y el año dentro del siglo
    siglo = año // 100  # Obtener el siglo
    año2 = año % 100    # Obtener el año dentro del siglo

    # Fórmula para calcular el día de la semana
    diasem = (((26 * mes - 2) // 10) + dia + año2 + (año2 // 4) + (siglo // 4) - (2 * siglo)) % 7

    # Ajustar el resultado si es negativo
    if diasem < 0:
        diasem = diasem + 7  # Asegurarse de que el resultado sea positivo

    return diasem  # Devolver el día de la semana (0=domingo, 1=lunes, ...)

def imprimir_calendario(mes, año):
    # Días en cada mes (considerando febrero como 28 días)
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Ajustar para años bisiestos
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        dias_por_mes[1] = 29  # Febrero tiene 29 días en un año bisiesto

    # Imprimir el encabezado del calendario
    print(f"Calendario de {mes}/{año}")
    print("Dom Lun Mar Mié Jue Vie Sáb")

    # Obtener el día de la semana del primer día del mes
    dia_semana = diadelasemana(1, mes, año)

    # Imprimir espacios en blanco para alinear el primer día del mes
    for _ in range(dia_semana):
        print("    ", end="")  # Espacios para los días anteriores

    # Imprimir los días del mes
    for dia in range(1, dias_por_mes[mes - 1] + 1):
        print(f"{dia:2d} ", end="")  # Imprimir el día con un ancho de 2 caracteres
        dia_semana += 1  # Incrementar el día de la semana
        if dia_semana % 7 == 0:  # Si se llega al final de la semana
            print()  # Saltar a la siguiente línea

    print()  # Asegurarse de que haya un salto de línea al final

# Ejemplo de uso
mes = 3  # Mes de marzo
año = 2023  # Año 2023
imprimir_calendario(mes, año)  # Llamar a la función para imprimir el calendario