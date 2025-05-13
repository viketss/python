'''
Desarrollar un programa que utilice una función que reciba como parámetro una
cadena de caracteres conteniendo una dirección de correo electrónico y devuelva
una tupla con las distintas partes que componen dicha dirección. Ejemplo:
alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar
formatos de fecha inválidos y devolver una tupla vacía.
'''

def pedir_correo():
    correo = input("Ingrese su direccion de correo electronico: ")
    if "@" not in correo:
        tupla_correo = ()
        return tupla_correo
    else:
        usuario_dominio = correo.split("@")  
        dominio_extension = usuario_dominio[1].split(".")
        tupla_correo = (usuario_dominio[0], dominio_extension[0], dominio_extension[1])
        print(tupla_correo)


pedir_correo() 
