import pprint

d = {}
d1 = dict([
    ('clave1', 1),
    ('clave2', 2),
    ('clave3', 3),
    ('clave4', 4)
    ])


d1['fruta'] = ['manzana','pera','uva']
print(d1['fruta'])

v1 = d1['fruta']
v1.append('platano')
v1.append('sandia')
d1['fruta'] = v1

print(d1['fruta'])
pprint.pprint(d1)

# Borrar elemento
del(d1['clave1'])
pprint.pprint(d1)

# Obtener todas las claves

claves = d1.keys()
pprint.pprint(claves)

# Obtener todos los valores

valores = d1.values()
pprint.pprint(valores)

# Iterar sobre un diccionario
for k in d1:
    print(k,d1[k])

for k,v in d1.items():
    print(f'clave: {k} valor: {v}')

#Limpiar en diccionario

#d1.clear()
#print(d1)

# Elementos del diccionario
print(d1.items())

# Extraer elementos del diccionario

#elem = d1.pop('fruta')
d1['ultimo'] = 'FIN'
print(d1)
elem = d1.popitem()
print(elem)
print(d1)

