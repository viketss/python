# NUMERO MAYOR
'''
Desarrollar una función que reciba tres números enteros positivos y devuelva el
mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en
caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar
también un programa para ingresar los tres valores, invocar a la función y mostrar
el máximo hallado, o un mensaje informativo si éste no existe.
'''
def numero_mayor(num1, num2, num3):
    # Verificar que los números sean positivos
    while num1 <= 0 or num2 <= 0 or num3 <= 0:
        print("Los números ingresados deben ser positivos.")
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        num3 = int(input("Ingrese el tercer número: "))

    # Determinar el mayor estricto
    if num1 > num2:
        if num1 > num3:
            print("El número mayor es:", num1)
            return num1
    if num2 > num1:
        if num2 > num3:
            print("El número mayor es:", num2)
            return num2
    if num3 > num1:
        if num3 > num2:
            print("El número mayor es:", num3)
            return num3

    # Si no hay un mayor estricto
    print("No hay un número mayor único.")
    return -1

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
numero_mayor(num1, num2, num3)
