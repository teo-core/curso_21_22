from pprint import pprint

def func_dame_matriz_ascendente(filas,columnas):
    M = []
    elementoM = 0
    for i in range(filas):
        filaM = []     
        for j in range(columnas):
            elementoM += 1
            filaM.append(elementoM)
        M.append(filaM)
    print('la matriz ascendente es:')
    print(M)
    return(M)

def func_dame_matriz_descendente(filas,columnas):
    H = []
    elementoH = filas * columnas
    for i in range(filas):
        filaH = []     
        for j in range(columnas):
            filaH.append(elementoH)
            elementoH -= 1
        H.append(filaH)
    print('la matriz descendente es:')
    print(H)
    return(H)

def func_dame_columna(col,H):
    v_aux = []
    for i in range(len(H)):
        v_aux.append(H[i][col])
    return(v_aux)

def func_multiplica_vectores(v1,v2):
    elem = 0
    for c in range(len(v1)):
        elem += v1[c] * v2[c]
    return(elem)


# matriz_M = [[1,2],[3,4]]
# matriz_H = [[4,3],[2,1]]
filas = 3
columnas = 3
matriz_M = func_dame_matriz_ascendente(filas,columnas)
matriz_H = func_dame_matriz_descendente(filas,columnas)
producto_MxH = []
for f in range(len(matriz_M[0])):
    fila_aux = []
    for i in range(len(matriz_H[0])):
        lista_aux = func_dame_columna(i,matriz_H)
        fila_de_M = matriz_M[f]
        elem_matriz_prod = func_multiplica_vectores(fila_de_M,lista_aux)
        fila_aux.append(elem_matriz_prod)
    producto_MxH.append(fila_aux)
    print('la columna es:')
    print(fila_aux)

pprint(producto_MxH)