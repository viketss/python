# LISTAS POR COMPRENSION
'''
Utilizar la técnica de listas por comprensión para construir una lista con todos los
números impares comprendidos entre 100 y 200.
'''
'''
<lista> = [<expresion> for <elemento> in <secuencia>]
'''

lista = [x for x in range(100, 200 + 1) if x % 2 == 1]
print(lista)


