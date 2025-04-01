# FUNCIONES LAMBDA
'''
Informar si un número es oblongo. Se dice que un número es oblongo cuando
se puede obtener multiplicando dos números naturales consecutivos. Por ejemplo
 6 es oblongo porque resulta de multiplicar 2 * 3.
'''
numero = 6
oblongo = lambda num: any(num == i * (i + 1) for i in range(1, int(num**0.5) + 1))

print(f"{numero} es oblongo: {oblongo(numero)}")

