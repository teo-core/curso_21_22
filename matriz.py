# lista=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# for i in range(20):
#     x = lista
#     print(x)

# -------------------------
# columna = [('x'*20)]

# for i in range(20):
#     x = columna
#     print(x)

# -------------------------

# lista = [1,2,3,4,'A']
# lista2 = [5,6,7,8,'B']
# lista3 = [9,10,11,12,'C']
# lista4 = [13,14,15,16,'D']
         

# for i in range(5):
#     x = [lista,lista2,lista3,lista4] 
#     print(x)

# -----------------

import pprint
cols = 10
filas = 10
matriz = []

for i in range(filas):
    fila = []
    for j in range(cols):
        fila.append("x")
    matriz.append(fila)

# ------------
for i in range(filas):
    linea = ''
    for j in range(cols):
        linea += matriz[i][j]
    print(linea)

# Deberes para mañana
M = 1,2,3
    4,5,6
    7,8,9

H = 9,8,7
    6,5,4
    3,2,1

