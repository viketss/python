'''
Escribir una función que reciba como parámetro una cadena de caracteres en la que
las palabras se encuentran separadas por uno o más espacios. Devolver otra
cadena con las palabras ordenadas según su longitud, dejando un espacio entre
cada una. Los signos de puntuación no deben ser tenidos en cuenta al medir la
longitud de las palabras, pero deberán conservarse en la cadena final.
'''
def palabrasOrdenadasLongitud(cadena):
    palabras = cadena.split()
    palabras.sort(key=len)
    return ' '.join(palabras)

# programa principal
frase = input("Ingrese una frase: ")
fraseOrdenada = palabrasOrdenadasLongitud(frase)
print("Frase ordenada:", fraseOrdenada)




