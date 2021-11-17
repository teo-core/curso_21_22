import os
import csv

ruta = '/home/teo/codigo/curso_21_22/csv/'

def leer_archivo():
    csv_in = open(ruta + 'titanic.csv') 
    lector = csv.DictReader(csv_in)
    lista = list(lector)
    csv_in.close()
    return lista
    

supervivientes = 0
muertos = 0

lista_titanic = leer_archivo()
for persona in lista_titanic:
    if persona['Survived'] == '1':
        supervivientes += 1
    else:
        muertos += 1
    
v = supervivientes
m = muertos
print('Sobrevivieron:',(v))
print('Murieron:',(m))