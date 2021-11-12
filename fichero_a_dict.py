import os
import pprint

os.system('clear')

ruta = '/home/teo/codigo/curso_21_22/viernes/programacion/python/funciones_miercoles.txt'
dic_salida = {}

def modo1():
    clave = 0
    # Leer archivo
    with open(ruta) as archivo:
        for l in archivo:
            #Procesar fila a fila
            fila = l[:-1:].split(',')
            #Recorrer lista y llenar dict
            for nombre in fila:
                dic_salida[clave] = nombre
                clave += 1


def modo2():
    clave = 0
    texto = open(ruta,'r').readlines()
    for archivo in texto:
        dic_salida[clave] = archivo
        clave += 1
    
    return dic_salida



pprint.pprint(modo2())
