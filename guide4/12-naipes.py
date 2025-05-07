'''
Escribir un programa para crear una lista por comprensión con los naipes de la ba-
raja española. La lista debe contener cadenas de caracteres. Ejemplo: ["1 Oros", "2
Oros"... ]. Imprimir la lista por pantalla.
'''

naipes = [str(i)+" "+j for i in range(1,11) for j in ["Oros","Copas","Espadas","Bastos"]]
print(naipes)

