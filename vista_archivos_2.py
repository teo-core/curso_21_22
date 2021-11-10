import os
import settings

def clear():
    os.system('clear')

def buscar(ruta_de_busqueda, extension='.py'):
    """
    Busca en la carpeta seleccionada archivos que acaben en .py
    y la devuelve en una lista sin .py
    """
    final = len(extension)
    lista_archivos = []
    archivo = os.scandir(ruta_de_busqueda)
    for a in archivo:
        if a.name.endswith(extension):
            lista_archivos.append(a.name[:-final:])
    return lista_archivos

def agrupar(lista_archivos, miembros): 
    """
    Toma una lista de cadenas de texto y devuelve 
    agrupamientos de esas cadenas 
    """
    fila = '' 
    for i in range(0,len(lista_archivos),miembros):
        temp = lista_archivos[i: i + miembros]
        fila += ','.join(temp) + '\n'
    return fila[:-1:]

def escribir(cadena,archivo):
    """
    Recoge la cadena de texto y la guarda en un archivo de texto
    sustituyendo el contenido del archivo
    """
    nuevo = open(archivo,'w')
    nuevo.write(cadena)
    nuevo.close()




ruta = settings.RUTA_BASE + settings.CODIGO
ruta_salida = settings.RUTA_BASE + settings.CODIGO +settings.MI_CARPETA

clear()
x = buscar(ruta,'.py')
f = agrupar(x,5)
escribir(f,ruta_salida + '/funciones_miercoles.txt')















