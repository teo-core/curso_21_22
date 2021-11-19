import csv
import pprint

def leer_dict():
    csv_in = open('/home/teo/codigo/curso_21_22/csv/titanic.csv')
    lector_dict = csv.DictReader(csv_in)
    lista_dict = list(lector_dict)
    csv_in.close()
    return lista_dict



def procesar_csv():
    pasajeros = leer_dict()
    mujeres = []
    hombres = []
    h_v = 0
    h_m = 0
    m_v = 0
    m_m = 0
    for p in pasajeros:
        if p['Sex'] == 'female':
            mujeres.append(p['Survived'])
        else:
            hombres.append(p['Survived'])
    h_v = hombres.count('1')
    h_m = hombres.count('0')
    m_v = mujeres.count('1')
    m_m = mujeres.count('0')    

    return (h_m, h_v, m_m, m_v)
    
resultado = procesar_csv()
print(f'Hombres vivos: {resultado[1]} Hombres muertos: {resultado[0]}' )
print(f'Mujeres vivas: {resultado[3]} Mujeres muertas: {resultado[2]}' )






#pprint.pprint(leer_dict())