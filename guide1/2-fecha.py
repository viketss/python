# FECHA 
"""
Desarrollar una función que reciba tres números enteros positivos correspondientes
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe
tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos.
Devolver True o False según la fecha sea correcta o no. Realizar también un
programa para verificar el comportamiento de la función.
"""

def fecha(dia, mes, año):
    if mes < 1 or mes > 12:
        return False

    if dia < 1 or dia > 31:
        return False

    if mes in [4, 6, 9, 11] and dia > 30:
        return False

    if mes == 2:
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            if dia > 29:
                return False
        else:
            if dia > 28:
                return False

    return True

dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))
print(fecha(dia, mes, año))