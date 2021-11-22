import os

dic = {}
archivo = open('/home/teo/codigo/curso_21_22/viernes/programacion/python/funciones_miercoles.txt','r')

for line in archivo:
    x = line.split(',')
    a = x[0]
    b = x[1]
    dic[a]=b

print(dic)


# abre = os.open(ruta_archivo, os)

# n = len(abre)

# lee = os.read(abre,len(ruta_archivo))
# print(split)















# # def leer(ruta_archivo):
# #     lee = open(ruta_archivo)
# #     return lee

# with open(ruta_archivo,'r') as file:
#     for line in file:
#     text = line.split(',', 1)[0] # add nsplits = 1 for efficiency 
#     ... # do something with text


# # for line in abrir:
# #     key, value = line.strip()
# #     dic[key] = value

# # print(dic)

