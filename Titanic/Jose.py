import os
import csv
ruta = '/home/teo/codigo/curso_21_22/csv/'

def leer_dict():
    csv_in = open(ruta + 'titanic.csv')
    lector_dict = csv.DictReader(csv_in)
    lista_dict = list(lector_dict)
    csv_in.close()
    return lista_dict


muertos = 0
supervivientes = 0
lista_diccionarios = leer_dict()
for diccionario in lista_diccionarios:
    if diccionario['Survived'] == '1':
        supervivientes += 1
    else:
        muertos += 1

print('Numero de muertos = ' + str(muertos))
print('Numero de supervivientes = ' + str(supervivientes))