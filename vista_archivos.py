import os
import settings

os.system('clear')

lista_archivos = []
archivo_salida = "salida.txt"
ruta_salida = settings.RUTA_BASE + settings.CODIGO +settings.MI_CARPETA
miembros = 5
fila = ''

# Buscar los archivos
archivo = os.scandir(settings.RUTA_BASE + settings.CODIGO)
for a in archivo:
    if a.name.endswith('.py'):
        lista_archivos.append(a.name[:-3:])

# Agruparlos de 5 en 5 
nuevo = open(ruta_salida + '/lista_py.txt','w')
for i in range(0,len(lista_archivos),miembros):
    temp = lista_archivos[i: i + miembros]
    fila = ','.join(temp) + '\n'
    nuevo.write(fila)

# Guardar archivos en el fichero


#nuevo.write(fila)
nuevo.close()
