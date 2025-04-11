
'''
Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con los
elementos de la primera que sean impares. El proceso deberá realizarse utilizando
la función filter(). Imprimir las dos listas por pantalla.
list(filter(<funcion>, <lista>)
'''
import random 

lista1 = [x for x in range(random.randint(1, 100))]
filtrada = list(filter(lambda x: x % 2 == 1, lista1))

print(filtrada)

