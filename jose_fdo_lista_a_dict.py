from genericpath import isdir
import os
#from settings import RUTA_BASE, RUTA_CODIGO, MI_CARPETA

#nuevo_dir = os.chdir('/')



def clear():
    os.system('clear')

# Primero hay que abrir y leer del archivo de entrada una fila y la troceamos para tomar cada nombre de archivo
def func_leer_archivo(ruta, nom_archivo, modo_ap):
    lista_de_filas = []
    nuevo = open(ruta + nom_archivo, modo_ap)
    
    salida_lectura_archivo = nuevo.readlines()
    #lista_de_filas.append(salida_lectura_archivo)
    nuevo.close()
    return salida_lectura_archivo



clear()
x = func_leer_archivo(
    '/home/teo/codigo/curso_21_22/viernes/programacion/python/','funciones_miercoles.txt', 
    'r')
#print(x)

dic_salida = {}
for j in range(len(x)):
    for i in range(5):
        list_aux = x[i].split(',')
        dic_salida[(i+j)] = list_aux[i]

print(dic_salida)