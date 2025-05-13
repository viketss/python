'''
Escribir una función que reciba como parámetro una tupla conteniendo una fecha
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada
en formato extendido. La función debe contemplarse que el año se ingrese en dos
dígitos, los que serán interpretados según un año de corte definido dentro del
programa. Cualquier año mayor que éste se considerará del siglo pasado. Por
ejemplo, si el año de corte fuera 30, la función devuelve "12 de Octubre de 2030"
para (12,10,30). Pero si la tupla fuera (25, 12, 31) devolverá "25 de Diciembre de
1931". Si el año se ingresa en cuatro dígitos el año de corte no será tenido en
cuenta. Escribir también un programa para ingresar los datos, invocar a la función y
mostrar el resultado.
'''

# Ejercico 2
nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

def pedir_fecha():
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))
    tupla = (dia, mes, año)  # Guardamos la tupla en una variable llamada 'tupla'
    return tupla

def fecha_en_texto(tupla):
    dia, mes, año = tupla  # Desempaquetamos la tupla en variables
    corte = 30  # Año de corte

    # Corregir el año si es de dos dígitos
    if año < 100:
        if año <= corte:
            año += 2000
        else:
            año += 1900

    # Armar y devolver el string con f-string
    fecha_texto = f"{dia} de {nombres_meses[mes - 1]} de {año}"
    print(fecha_texto)

fecha = pedir_fecha()  
fecha_en_texto(fecha)  