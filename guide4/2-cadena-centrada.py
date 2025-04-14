# CADENA DE CARACTERES CENTRADA
'''
Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la
misma tiene 80 columnas.
'''

def cadenaCentrada():
    texto = input("Ingresa una cadena de caracteres o texto: ")
    anchoPantalla = 80
    # calcular espacios a la izquierda para centrar el texto
    espacioIzquierda = (anchoPantalla - len(texto)) // 2

    # imprimir con los espacios a la izquierda para centrarlo
    print(' ' * espacioIzquierda + texto)


cadenaCentrada()