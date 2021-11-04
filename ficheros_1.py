from pprint import pprint
archivo = 'listas.py'
listas = open(archivo)
# lineas = listas.readlines()
# for l in lineas:
#     pprint(l)

# listas.close()


# pprint(lineas)

for linea in listas:
    pprint(linea)
