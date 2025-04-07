# frutihorticola: naranjas
'''
Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso
para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y
cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón
caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso
de alguna naranja se encuentra fuera del rango indicado se la clasifica para
procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas
cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para
jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente
reparto. Simular el peso de cada unidad generando un número entero al azar entre
150 y 350.

Además, se desea saber cuántos camiones se necesitan para transportar la cose-
cha, considerando que la ocupación del camión no debe ser inferior al 80%; en

caso contrario el camión no serán despachado por su alto costo.
'''

import random 

def cosechar_naranjas(cantidad_naranjas):
    cajones = 0 #contador de cajones llenos
    naranjas_jugo = 0 #contador de naranjas para jugo
    sobrantes = 0 # contador de naranjas sobrantes

    # procesar cada naranja
    for i in range(cantidad_naranjas):
        peso = random.randint(150, 350) # peso random entre 150 y 350
        if 200 <= peso <= 300: #peso entre 200 y 300gr
            # cada cajon contiene 100 naranjas
            if cajones * 100 < cantidad_naranjas: #si se puede llenar un cajon
                cajones += 1 #llenamos un cajon
        else:
            naranjas_jugo += 1 #las naranjas fuera de rango se hacen jugo
    
    #calcular naranjas sobrantes
    total_naranjas = cantidad_naranjas - (cajones * 100) - naranjas_jugo
    if total_naranjas > 0:
        sobrantes = total_naranjas #contar sobrantes si hay

    return cajones, naranjas_jugo, sobrantes

def calcular_camiones(cajones, n_camiones):
    peso_total = cajones * 100 * 250 #promedio de 250gr por naranja
    peso_total_kg = peso_total / 1000

    #caclular cuanto camiones se necesitan
    camiones_necesarios = peso_total_kg / 500 # cada camion puede transportar 500kg
    camiones_necesarios = int(camiones_necesarios) + (1 if peso_total_kg % 500 > 0 else 0)  # Redondear para arriba

    #verificar si la ocupacion del camion es suficiente
    camiones_a_despachar = 0 
    if camiones_necesarios <= n_camiones and peso_total_kg >= 0.8 * camiones_necesarios * 500:
        camiones_a_despachar = camiones_necesarios  # Se pueden despachar los camiones

    return camiones_a_despachar

             
# PROGRAMA PRINCIPAL
cantidad_naranjas = int(input("Ingrese la cantidad de naranjas cosechadas: "))  
n_camiones = int(input("Ingrese la cantidad de camiones disponibles: "))  

# guardar resultados
cajones, naranjas_para_jugo, sobrantes = cosechar_naranjas(cantidad_naranjas)

print(f"Cajones llenos: {cajones}")
print(f"Naranjas para jugo: {naranjas_para_jugo}")
print(f"Sobrantes de naranjas: {sobrantes}")

# Calcular y mostrar cuántos camiones se necesitan
camiones_a_despachar = calcular_camiones(cajones, n_camiones)
if camiones_a_despachar > 0:
    print(f"Camiones a despachar: {camiones_a_despachar}")
else:
    print("No se despacharán camiones debido a baja ocupación o falta de camiones disponibles.")


