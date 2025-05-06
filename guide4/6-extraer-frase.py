'''Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena
como valor de retorno. Escribir también un programa para verificar el comporta-
miento de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356-7890
extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres,
resultando la subcadena "4356-7890". Escribir una función para cada uno de los si-
guientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
'''
def extraerSubcadena(cadena, posicion, longitud):
    subcadena = cadena[posicion:posicion+longitud] # rebanada desde la posicion hasta la longitud
    return subcadena

def extraerSubcadenaSinRebanadas(cadena, posicion, longitud):
    subcadena = ''
    for i in range(posicion, posicion + longitud):
        subcadena += cadena[i]
    return subcadena

# con rebanadas
frase = input("Ingrese una frase: ")
posicion = int(input("Ingrese la posicion de inicio: "))
longitud = int(input("Ingrese la longitud de la subcadena a extraer: "))

subcadena = extraerSubcadena(frase, posicion, longitud)
print("Subcadena extraida:", subcadena)

# sin rebanadas
sinrebanadas = extraerSubcadenaSinRebanadas(frase, posicion, longitud)
print("Subcadena extraida sin rebanadas:", sinrebanadas)