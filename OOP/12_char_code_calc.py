"""
Dada una cadena de texto, convertir cada letra a su código ASCII.
Con esto creamos un número que llamaremos total_1.
Cambiar todos los número '7' por '1' y a ese número le llamaremos total_2
Devolver total_1 - total_2

"""
def cambio(cadena):

    total_2 = []

    for i in cadena:
        tmp = str(ord(i))
        total_2.append(tmp)

    numero_1 = ''.join(total_2)
    numero_2 =  numero_1.replace('7','1')
    
    return int(numero_1) - int(numero_2)

print(cambio('ABC'))


#--------------------------------
