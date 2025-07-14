'''
Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al
usuario y eliminarlos del conjunto mediante el método remove, mostrando el con-
tenido del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1.
Utilizar manejo de excepciones para evitar errores al intentar quitar elementos
inexistentes.
'''

numeros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(f"Conjunto inicial: {numeros}")

valor = int(input("Ingrese un número entre 0 y 9 para eliminar del conjunto (-1 para salir): "))

while valor != -1:
    try:
        if valor < 0 or valor > 9:
            print("Número fuera de rango. Debe ser entre 0 y 9.")
        else:
            numeros.remove(valor)
            print(f"Conjunto después de eliminar {valor}: {numeros}")
    except KeyError: # KeyError se lanza si el elemento no está en el conjunto
        print(f"El número {valor} no está en el conjunto.")
    
    # Solicitar un nuevo valor
    valor = int(input("Ingrese un número entre 0 y 9 para eliminar del conjunto (-1 para salir): "))



