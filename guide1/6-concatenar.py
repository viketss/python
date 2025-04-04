# CONCATENAR PARAMETROS
# copilot: disable

def concatenar (num1, num2):
    lista = []
    lista.append(num1)
    lista.append(num2)
    return lista

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
print(concatenar(num1, num2))