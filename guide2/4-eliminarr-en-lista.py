# ELIMINAR DE LA LISTA
'''
Eliminar de una lista de números enteros aquellos valores que se encuentren en
una segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista
resultante. La función debe modificar la lista original sin crear una copia modificada.
'''

def eliminar_de_lista(lista1, lista2):
    print('Lista original: ', lista1)
    print('Lista de valores a eliminar: ', lista2)

    for elemento in lista2:
        while elemento in lista1:
            lista1.remove(elemento)  # elimina el elemento de la lista1

    return lista1  # devuelve lista modificada

lista = [1, 2, 3, 3, 4, 5, 5, 1, 4, 7, 8]
valores_a_eliminar = [3, 5, 1]

lista_resultante = eliminar_de_lista(lista, valores_a_eliminar)

print('Lista resultante: ', lista_resultante)

