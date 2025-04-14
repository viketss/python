
'''
Los números de claves de dos cajas fuertes están intercalados dentro de un número
entero llamado "clave maestra", cuya longitud no se conoce. Realizar un programa
para obtener ambas claves, donde la primera se construye con los dígitos ubicados
en posiciones impares de la clave maestra y la segunda con los dígitos ubicados en
posiciones pares. Los dígitos se numeran desde la izquierda. Ejemplo: Si clave
maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería 89.
'''

def obtenerClaves(claveMaestra):
    clave1 = '' # digitos en posiciones impares
    clave2 = '' # digitos en posiciones pares

    for pos, digito in enumerate(claveMaestra, start=1):
        if pos % 2 == 1: #impares
            clave1 += digito 
        else:
            clave2 += digito

    return clave1, clave2 

claveMaestra = input("Ingresa la clave maestra: ")
psw1, psw2 = obtenerClaves(claveMaestra)

print("Clave 1 (posiciones impares): ", psw1)
print("Clave 2 (posiciones pares): ", psw2)

