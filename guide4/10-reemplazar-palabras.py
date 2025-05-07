'''
Desarrollar una función para reemplazar todas las apariciones de una palabra por
otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la
cantidad de reemplazos realizados. Tener en cuenta que sólo deben reemplazarse
palabras completas, y no fragmentos de palabras. Escribir también un programa
para verificar el comportamiento de la función.
'''

def reemplazarAparicionesPalabra(frase, palabraVieja, palabraNueva):
    palabras = frase.split()
    contador = 0
    for i in range(len(palabras)):
        if palabras[i] == palabraVieja:
            palabras[i] = palabraNueva
            contador += 1
    nueva_frase = ' '.join(palabras)
    return nueva_frase, contador

frase = input("Ingrese una frase: ")
palabraVieja = input("Ingrese la palabra a reemplazar: ")
palabraNueva = input("Por la palabra nueva: ")

reemplazo, cantidad = reemplazarAparicionesPalabra(frase, palabraVieja, palabraNueva)
print(f"Frase resultante: {reemplazo}")
print(f"Cantidad de reemplazos: {cantidad}")