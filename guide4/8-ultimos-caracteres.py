'''
Desarrollar una función que devuelva una subcadena con los últimos N caracteres
de una cadena dada. La cadena y el valor de N se pasan como parámetros.
'''

def ultimosCaracteres(cadena, numCaracteres):
    subcadena = cadena[-numCaracteres:]  # index negativo para hacer los ultimos N caracteres
    return subcadena

frase = input("Ingrese la frase: ")
caracteres = int(input("Ingrese los últimos caracteres deseados: "))
ultimo = ultimosCaracteres(frase, caracteres)

print(ultimo)