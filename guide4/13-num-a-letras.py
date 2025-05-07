'''
Muchas aplicaciones financieras requieren que los números sean expresados tam-
bién en letras. Por ejemplo, el número 2153 puede escribirse como "dos mil ciento
cincuenta y tres". Escribir un programa que utilice una función para convertir un
número entero entre 0 y 1 billón (1.000.000.000.000) a letras. ¿En qué cambiaría
la función si también aceptara números negativos? ¿Y números con decimales?
'''

def convertir_a_letras(num):
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
    decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta",
               "sesenta", "setenta", "ochenta", "noventa"]
    centenas = ["", "cien", "doscientos", "trescientos", "cuatrocientos",
                "quinientos", "seiscientos", "setecientos", "ochocientos",
                "novecientos"]
    miles = ["mil"]

    if num == 0:
        return 'cero'

    if num < 0:
        return 'menos ' + convertir_a_letras(-num)

    letras = ''
    if num >= 1000:
        letras += unidades[num // 1000] + ' ' + miles[0] + ' '
        num %= 1000

    if num >= 100:
        letras += centenas[num // 100] + ' '
        num %= 100

    if num >= 20:
        letras += decenas[num // 10] + ' '
        num %= 10

    if num >= 1:
        letras += unidades[num] + ' '

    return letras.strip()

numero = int(input("Ingrese un número entero entre 0 y 1 billón: "))
print(convertir_a_letras(numero))




