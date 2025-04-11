
'''
Resolver el siguiente problema, diseñando las funciones a utilizar:
Una clínica necesita un programa para atender a sus pacientes. Cada paciente que
ingresa se anuncia en la recepción indicando su número de afiliado (número entero
de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con
turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego
se solicita:
a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de
los pacientes atendidos por turno en el orden que llegaron a la clínica.
b. Realizar la búsqueda de un número de afiliado e informar cuántas veces fue
atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta
que se ingrese -1 como número de afiliado.
'''

def registrarPaciente():
    numAfiliado = int(input("Ingrese su numero de afiliado: "))
    urgencias = []
    turnos = []

    # hasta que el paciente ingrese -1
    while numAfiliado != -1:
        # numero de afiliado de 4 digitos
        while numAfiliado < 1000 or numAfiliado > 9999:
            numAfiliado = int(input("Numero de afiliado invalido. Ingreselo nuevamente: "))

        print('Ingreso exitoso. Numero de afiliado: ', numAfiliado)
        motivoConsulta(numAfiliado, urgencias, turnos)
        numAfiliado = int(input("Ingrese su numero de afiliado: "))

    return urgencias, turnos

def motivoConsulta(paciente, urgencias, turnos):

    print("Motivo de la consulta: ")
    motivo = int(input("0 para urgencia | 1 para turnos: "))

    if motivo == 0:
        print("Usted ingreso a la clinica por una emergencia.")
        urgencias.append(paciente)
    elif motivo == 1:
        print("Usted tiene un turno en la clinica.")
        turnos.append(paciente)
    else:
        print("Motivo de consulta invalido. 0 para urgencia | 1 para turnos: ")
    return urgencias, turnos

def mostrarListados(urgencias, turnos):
    print("\nPacientes atendidos por urgencia: ")
    for paciente in urgencias:
        print(paciente)

    print("\nPacientes atendidos por turno: ")
    for paciente in turnos:
        print(paciente)

def buscarAfiliado(urgencias, turnos):
    numero_afiliado = int(input("Ingrese el número de afiliado a buscar o -1 para finalizar: "))
    while numero_afiliado != -1:
        
        conteo_urgencias = urgencias.count(numero_afiliado)
        conteo_turnos = turnos.count(numero_afiliado)
        
        print(f"El afiliado {numero_afiliado} fue atendido {conteo_urgencias} veces por urgencia y {conteo_turnos} veces por turno.")

def main():
    urgencias, turnos = registrarPaciente()
    mostrarListados(urgencias, turnos)
    buscarAfiliado(urgencias, turnos)

main()