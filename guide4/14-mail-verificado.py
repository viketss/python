'''
Se solicita crear un programa para leer direcciones de correo electrónico y verificar
si representan una dirección válida. Por ejemplo usuario@dominio.com.ar. Para que
una dirección sea considerada válida el nombre de usuario debe poseer solamente
caracteres alfanuméricos, la dirección contener un solo carácter @, el dominio debe
tener al menos un carácter y tiene que finalizar con .com o .com.ar.
Repetir el proceso de validación hasta ingresar una cadena vacía. Al finalizar mos-
trar un listado de todos los dominios, sin repetirlos y ordenados alfabéticamente,
recordando que las direcciones de mail no distinguen mayúsculas ni minúsculas.
'''

def verificarMail(email):
    # Verifico que solo haya un unico caracter @
    if (email.count('@') != 1):
        return False
    
    # Separo la direccion y el dominio a partir del caracter @
    direccion, dominio = email.split('@')

    # Reviso que la direccion y el dominio no esten vacios (es decir que ambas partes esten)
    if (not direccion or not dominio):
        return False

    # Verifico que el dominio contenga al menos un punto y que no empiece ni termine con un punto
    if ('.' not in dominio or dominio[0] == '.' or dominio[-1] == '.'):
        return False

    # Creo un texto con todos los caracteres validos
    caracteresValidos = 'abcdefghijklmnopqrstuvwxyz._-@'

    # Recorro cada caracter del email y verifico que sea valido
    for caracter in email:
        # Reviso si el caracter no esta en el listado de caracteres validos
        if (caracter.lower() not in caracteresValidos):
            False
    
    # Devuelvo True si se pasaron todas las validaciones anteriores
    return True
