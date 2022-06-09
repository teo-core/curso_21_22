"""
Cajero de cambio: devuelve y desglosa el cambio en billetes y monedas de forma "ideal"; 
es decir, con el menor número de
billetes y monedas posibles.

Pide un valor en euros y devuelve los billetes de 500, 200, 100, 50, 20, 10 y 5 euros, 
y las monedas de 2€, 1€, 50c, 20c, 10c, 5c, 2c y 1c. Ejemplo:

Valor en €uros:  175,50

Cambio: 1 billete de 100€
        1 billete de 50€
        2 billetes de 20€
        1 billete de 5€
        1 moneda de 50c
"""

def cambio_moneda(cantidad):
    monedas =[500,200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
    cambio = []
    for v in monedas:
        cociente = cantidad//v
        if cociente > 0:
            cambio.append(f'{cociente:.0f} de {v}€')
            resto = cantidad % v
            if resto == 0:
                break
            else:
                cantidad = resto
    return cambio

x = cambio_moneda(8654.78)
print(x)
