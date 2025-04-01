# NUMERO TRIANGULAR
'''
Informar si un número es triangular. Un número se define como triangular si
puede expresarse como la suma de un grupo de números naturales consecuti-
vos comenzando desde 1. Por ejemplo 10 es un número triangular porque se
obtiene sumando 1+2+3+4.
'''
triangular = lambda num: any(num == sum(range(1, i + 1)) for i in range(1, num + 1))
numero = int(input("Ingrese un número: "))
print(f"{numero} es triangular: {triangular(numero)}")
