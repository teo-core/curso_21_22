from pprint import pprint
ruta = '/home/teo/codigo/curso_21_22/viernes/programacion/python/funciones_miercoles.txt'

listas = open(ruta)
lineas = listas.readline()



def diccionary():
    diccionario_total = {}

    for lineas in listas:
        if lineas == ' ':
            break
        archivos = lineas.split(',')
        diccionario_total = dict(archivos)
        
    return diccionario_total


pprint(diccionary())



# print(ruta)