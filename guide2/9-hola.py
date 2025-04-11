
'''
Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7
que no sean múltiplos de 5. A y B se ingresar desde el teclado.
'''
# Ingresar valores de A y B desde el teclado
A = int(input("Ingrese el valor de A: "))
B = int(input("Ingrese el valor de B: "))

# Generar la lista por comprensión
resultado = [x for x in range(A, B + 1) if x % 7 == 0 and x % 5 != 0]

# Imprimir la lista generada
print("Lista generada:", resultado)