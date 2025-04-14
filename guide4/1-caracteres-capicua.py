# CADENAS DE CARACTERES CAPICUA
'''
Desarrollar una función que determine si una cadena de caracteres es capicúa, sin
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita
verificar su funcionamiento.
'''
def es_capicua(texto):
    # Inicializamos dos índices: uno al principio y otro al final de la cadena
    inicio = 0
    final = len(texto) - 1

    # Recorremos la cadena desde ambos extremos hacia el centro
    while inicio < final:
        # Si los caracteres en las posiciones actuales no son iguales, no es capicúa
        if texto[inicio] != texto[final]:
            return False
        # Avanzamos el índice del principio y retrocedemos el del final
        inicio += 1
        final -= 1
    # Si terminamos el bucle sin encontrar diferencias, la cadena es capicúa
    return True

def main():
    # Solicitamos al usuario que ingrese una cadena de texto
    texto = input("Ingrese una cadena: ")
    # Llamamos a la función y mostramos el resultado
    if es_capicua(texto):
        print("La cadena es capicúa.")
    else:
        print("La cadena NO es capicúa.")

# Ejecutamos el programa principal
main()






