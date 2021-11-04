import os 
os.system('clear')

ruta = os.getcwd()
print(ruta)

contenido = os.scandir(ruta)
for f in contenido:
    print(f.name)

