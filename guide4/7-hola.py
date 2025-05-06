'''
Escribir una función para eliminar una subcadena de una cadena de caracteres, a
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resul-
tante. Escribir también un programa para verificar el comportamiento de la misma.
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
'''

def eliminarSubcadena(cadena, posicion, longitud):
    subcadena = cadena[posicion:posicion+longitud]
    cadena = cadena.replace(subcadena, '')
    return cadena



frase = input("Ingrese una frase: ")
posicion = int(input("Ingrese la posicion de inicio: "))
longitud = int(input("Ingrese la longitud de la subcadena a eliminar: "))
eliminar = eliminarSubcadena(frase, posicion, longitud)
print("Frase resultante:", eliminar)
