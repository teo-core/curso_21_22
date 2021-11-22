import os
import csv

os.system('clear')
ruta = '/home/teo/codigo/curso_21_22/csv/'


def leer_dict():
    csv_in = open(ruta + 'titanic.csv')

    lector_dict = csv.DictReader(csv_in)
    lista_dict = list(lector_dict)
    csv_in.close()

    return lista_dict


def crear_archivo(pasajeros):
    
    lista_personas = []
    for p in pasajeros:
        if p['Age'] != '' and 20 <= float(p['Age']) <=30 and int(p["Survived"]) == 1:
            persona = {}
            persona['Nombre'] = p['Name']
            persona['Clase'] = p['Pclass']
            persona['Sexo'] = p['Sex']
            lista_personas.append(persona)
            print(lista_personas)
    
    with open(ruta + 'titanic_filtrado.csv', 'w') as salida:
        escritor = csv.writer(salida)
        escritor.writerow(lista_personas[0].keys())
        for seleccionado in lista_personas:
            escritor.writerow(seleccionado.values())



lista_dicionario = leer_dict()
crear_archivo(lista_dicionario)

