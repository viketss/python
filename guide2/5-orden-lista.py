#ORDEN DE LISTA
'''
Escribir una función que reciba una lista como parámetro y devuelva True si la lista
está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
además un programa para verificar el comportamiento de la función.
'''

def ordenada_ascendente(lista):
    '''
    Verifica si la lista está ordenada en forma ascendente.
    '''
    return lista == sorted(lista)  # Compara la lista original con su versión ordenada

# Programa para verificar el comportamiento de la función
milista = [1, 2, 3, 4, 5, 6]
print(ordenada_ascendente(milista))  

otralista = [6, 5, 4, 3, 2, 1]
print(ordenada_ascendente(otralista))  

lista_mixta = [1, 2, 3, 2]
print(ordenada_ascendente(lista_mixta)) 

lista_cadenas = ['a', 'b', 'c']
print(ordenada_ascendente(lista_cadenas))  

lista_cadenas_desc = ['b', 'a']
print(ordenada_ascendente(lista_cadenas_desc))  

