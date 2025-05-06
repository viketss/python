'''
Escribir una función filtrar_palabras() que reciba una cadena de caracteres conte-
niendo una frase y un entero N, y devuelva otra cadena con las palabras que ten-
gan N o más caracteres de la cadena original. Escribir también un programa para

verificar el comportamiento de la misma. Hacer tres versiones de la función, para
cada uno de los siguientes casos:
a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filter
'''

def filtrar_palabras(frase, num):
    palabras = frase.split() # separar la frase en palabras
    palabras_filtradas = [] # almaceno palabras filtradas
    for palabra in palabras:
        if len(palabra) >= num:
            palabras_filtradas.append(palabra)
    return palabras_filtradas


frase = input("Ingrese una frase: ")
num = int(input("Ingrese un número: "))
filtradas = filtrar_palabras(frase, num)

print("Ahora con la funcion filter")
'''sintaxis → list(filter(<funcion>, <lista>)'''

filtradas_filter = list(filter(lambda palabra: len(palabra) >= num, frase.split()))
print("Palabras filtradas con filter:", filtradas_filter)
