'''
Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y
lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En
qué cambiaría la función si el rango de valores fuese diferente?
'''

def entero_a_romano(num):
    if not (0 <= num <= 3999):
        return "Número fuera de rango (0-3999)"

    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
        (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"),
        (1, "I")
    ]

    resultado = ""
    for valor, simbolo in valores:
        while num >= valor:
            resultado += simbolo
            num -= valor
    return resultado


