import csv
import pprint

def leer_dict():
    csv_in = open('/home/teo/codigo/curso_21_22/csv/titanic.csv')
    lector_dict = csv.DictReader(csv_in)
    lista_dict = list(lector_dict)
    csv_in.close()
    return lista_dict


def procesar_csv_alan():
    pasajeros = leer_dict()
    mujeres = []
    hombres = []
    h_v = 0
    h_m = 0
    m_v = 0
    m_m = 0
    for p in pasajeros:
        if p['Sex'] == 'female' and p['Survived'] == '1':
            m_v +=1
        if p['Sex'] == 'female' and  p['Survived'] == '0':
            m_m +=1
        if p['Sex'] == 'male' and p['Survived'] == '1':
            h_v +=1
        if p['Sex'] == 'male' and  p['Survived'] == '0':
            h_m +=1         

    return (m_v,m_m,h_v,h_m)


pprint.pprint(procesar_csv_alan())