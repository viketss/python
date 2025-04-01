# ELECTRODOMESTICOS

'''
Un comercio de electrodomésticos necesita para su línea de cajas un programa que
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
dos números enteros, correspondientes al total de la compra y al dinero recibido.
Informar cuántos billetes de cada denominación deben ser entregados como vuelto,
de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes
de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el
dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta
de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se
abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1
billete de $200, 1 billete de $100 y 3 billetes de $10.
'''

# SISTEMA DE VENTAS DE ELECTRODOMESTICOS
"""
Un comercio de electrodomésticos necesita para su línea de cajas un programa que
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
dos números enteros, correspondientes al total de la compra y al dinero recibido.
Informar cuántos billetes de cada denominación deben ser entregados como vuelto,
de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes
de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el
dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta
de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se
abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1
billete de $200, 1 billete de $100 y 3 billetes de $10.
"""
def calcularCambio(compra_total, dinero_recibido):
    """ Calcula el cambio que se le debe entregar al cliente """
    if dinero_recibido < compra_total:
        print("Error: El dinero recibido es insuficiente.")
        return None
    return dinero_recibido - compra_total

def calcularBilletes(cambio):
    """ Calcula la cantidad de billetes que se le debe entregar al cliente """
    if cambio is None:
        return

    billetes = [5000, 1000, 500, 200, 100, 50, 10]
    resultado = {}

    for billete in billetes:
        cantidad = cambio // billete
        if cantidad > 0:
            resultado[billete] = cantidad
        cambio %= billete

    if cambio != 0:
        print("Error: No se puede entregar el cambio exacto con las denominaciones disponibles.")
        return

    print("Cambio a entregar:")
    for billete, cantidad in resultado.items():
        print(f"Billetes de ${billete}: {cantidad}")

compra = int(input("Ingrese el total de la compra: "))
pago_cliente = int(input("Ingrese el dinero recibido del cliente: "))
cambioTotal = calcularCambio(compra, pago_cliente)

if cambioTotal is not None:
    print(f"El cambio es de: ${cambioTotal}")
    calcularBilletes(cambioTotal)
