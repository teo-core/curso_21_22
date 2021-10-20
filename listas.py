# ceros = ['hola'] * 5
# x=ceros[2]
# print(x)
# print(ceros)

# v1 = [1,2]
# v2 = [7,8]
# total = 0

# for i in range(len(v1)):
#     total += v1[i] * v2[i]

# print(total)

origen = [1,2,3,4,5,'Jose', 'Alan', 'Fernando']
numeros = []
alumnos =[]

for x in origen:
    if type(x) == str:
        alumnos.append(x)
    else:
        numeros.append(x)
        
print(origen)
print(alumnos)
print(numeros)



