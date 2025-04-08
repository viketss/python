# INTERCALAR ELEMENTOS CON REBANADAS
'''
Intercalar los elementos de una lista entre los elementos de otra. La intercalación
deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará
una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3]
y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden
tener distintas longitudes.
'''

def intercalarElementos(lista1, lista2):
    #longitud de ambas listas
    longitud_lista1 = len(lista1)
    longitud_lista2 = len(lista2)
    
    # cantidad de intercalaciones posibles, de acuerdo a la lista mas corta
    intercalaciones = min(longitud_lista1, longitud_lista2)

    for i in range(intercalaciones):
        # inserta el elemento de lista2 en la posición correcta de lista1
        lista1.insert(2 * i + 1, lista2[i])  # insertar elemento individualmente

    if longitud_lista2 > longitud_lista1:
        lista1.extend(lista2[intercalaciones:])  # insertar sobrantes de lista2 al final de lista1


# Programa principal
lista1 = [1, 5, 8, 9, 2]
lista2 = [2, 5, 7, 4, 9]

print('Listas base: \n', lista1, '\n', lista2)

intercalarElementos(lista1, lista2)
print('Lista 1 despues de intercalar: ', lista1)


