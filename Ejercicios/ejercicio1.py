from pprint  import pprint
import os 
import csv

def pedir_personas():
    seguir = True
    lista_personas = []

    while seguir:
        print('Introduzca datos. (N para terminar')
        nombre    = input('Nombre: ')
        apellido1 = input('Apellido1: ')
        fecha_nac = input('Fecha nacimiento: ')
        telefono  = input('Teléfono: ')
        mi_dic    = {'nombre': nombre, 'apellido1': apellido1, 'fecha_nac':fecha_nac, 'telefono': telefono}
        
        lista_personas.append(mi_dic)

        respuesta = input('¿Desea continuar s/n?')
        if respuesta.upper() == 'N':
            seguir = False
        os.system('clear')
    
    return lista_personas

    
def guardar_csv(contenido, destino):
    with open(destino, 'w',newline='') as f:
        escritor = csv.DictWriter(f,fieldnames=list(contenido[0].keys()))
        escritor.writeheader()
        escritor.writerows(contenido)

cont = pedir_personas()
ruta = '/home/teo/codigo/curso_21_22/Ejercicios/personas.csv'

guardar_csv(cont,ruta)
