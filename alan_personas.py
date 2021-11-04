# Hacer una función que le pida al usuario datos: DNI, nombre,...etc.
# Tal cual se pide, realiza los imputs que se determinen en orden y recibiendo cualquier resultado.
def Introduce():
    # Podría hacer un bucle de veces por cada usuario que quiera meter
    Nombre = input('Introduzca su nombre: ')
    Apellido = input('Introduzca sus apellidos: ')
    Dni = input('Introduzca su DNI: ')
    Edad = input('Introduzca su edad: ')
    Sexo = input('Introduzca su sexo: ')
    Pregun = input('¿Quiere ver el diccionario, y o n?:  ')
    import pprint
    dicci = {}

    Nombre
    dicci['Nombre'] = Nombre
    Apellido
    dicci['Apellido'] = Apellido
    Dni
    dicci['Dni'] = Dni
    Edad
    dicci['Edad'] = Edad
    Sexo
    dicci['Sexo'] = Sexo
    if Pregun == str('y'):
        pprint.pprint(dicci)
        print('Ususario registrado con éxito')
    else:
        print('Ususario registrado con éxito')

Introduce()