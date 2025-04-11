# SISTEMA DE GESTION DE SOCIOS EN UN CLUB
'''
Resolver el siguiente problema, utilizando funciones:
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se

ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de car-
ga. Se solicita:

a. Informar para cada socio, cuántas veces ingresó al club. Cada socio debe
aparecer una sola vez en el informe.
b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus
ingresos. Mostrar los registros de entrada al club antes y después de
eliminarlo. Informar cuántos ingresos se eliminaron.
'''

def ingresarSocio():
    ingresosSocios = []
    numeroSocio = int(input("Ingresa tu numero de socio (5 digitos): "))

    while numeroSocio != 0:
        while numeroSocio < 10000 or numeroSocio > 99999:
            numeroSocio = int(input("Error, ingresa tu numero de socio nuevamente o 0 para finalizar: "))
        
        # si no se ingresan datos
        if numeroSocio == 0:
            return ingresosSocios
        
        ingresosSocios.append(numeroSocio)

        # finalizar carga
        numeroSocio = int(input("Ingresa tu numero de socio o 0 para finalizar: "))
    return ingresosSocios

def contarIngresos(ingresosSocios):
    conteo = []
    for socio in ingresosSocios:
        if socio not in conteo:
            conteo.append(socio)
    return [(socio, ingresosSocios.count(socio)) for socio in conteo]

def eliminarSocio(ingresosSocios, socio_a_eliminar):
    ingresos_previos = len(ingresosSocios)
    ingresosSocios[:] = [socio for socio in ingresosSocios if socio != socio_a_eliminar]
    ingresos_eliminados = ingresos_previos - len(ingresosSocios)
    return ingresos_eliminados

def mostrarIngresos(conteo):
    print("\nRegistro de ingresos por socio:")
    for socio, cantidad in conteo:
        print(f"Número de socio: {socio}, Ingresos: {cantidad}")

def main():
    ingresosSocios = ingresarSocio()
    # A - contar y mostrar los ingresos por socio
    conteo = contarIngresos(ingresosSocios)
    mostrarIngresos(conteo)

    # b. Solicitar un número de socio para eliminar
    socio_a_eliminar = int(input("\nIngresa el número de socio que se dio de baja: "))
    ingresos_eliminados = eliminarSocio(ingresosSocios, socio_a_eliminar)

    # Mostrar registros después de eliminar
    print(f"\nSe eliminaron {ingresos_eliminados} ingresos del socio {socio_a_eliminar}.")
    print("Registros de entrada al club después de eliminar:")
    mostrarIngresos(contarIngresos(ingresosSocios))

# Programa principal:
main()