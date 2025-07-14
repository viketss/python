'''
Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras
repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras
ordenadas según su longitud. Los signos de puntuación no deben afectar el
proceso.
'''

frase = input("Ingrese una frase: ")

# Definir los signos de puntuación manualmente
puntuacion = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# Eliminar signos de puntuación
frase_sin_puntuacion = ''.join(c for c in frase if c not in puntuacion)

# Separar en palabras y eliminar repetidas usando un conjunto
palabras = set(frase_sin_puntuacion.lower().split())

# Ordenar las palabras por longitud
palabras_ordenadas = sorted(palabras, key=len)

print("Palabras ordenadas por longitud:")
for palabra in palabras_ordenadas:
    print(palabra)