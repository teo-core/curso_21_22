matriz1 = [[1,2,3],
           [4,5,6],
           [7,8,9]]

matriz2 = [[9,8,7],
           [6,5,4],
           [3,2,1]]

resultado = [[0,0,0],
             [0,0,0],
             [0,0,0]]        


for i in range(len(matriz1)):
    for j in range(len(matriz2[0])):
        for k in range(len(matriz2)):
            resultado[i][j] += matriz1[i][k] * matriz2[k][j]

import pprint
pprint.pprint(resultado)