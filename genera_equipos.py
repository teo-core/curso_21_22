
# def genera_equipos(personas):
#     equipos = []
#     rango = len(personas)
#     for i in range(rango//2):
#         for j in range(2):
#             aleatorio = rd.randrange(rango)
#             if j == 0:
#                 par1 = personas.pop(aleatorio)
#             else:
#                 par2 = personas.pop(aleatorio)
#             rango -= 1
#         equipos.append(par1+emparejamiento+par2+emparejamiento+personas.pop(0))

import random as rd
def genera_equipos(alumnos):
    personas = alumnos.copy()
    rd.shuffle(personas)
    equipos = []
    num_equipos = len(personas) // 2
    for i in range(num_equipos):
        eq = []
        eq.append(personas.pop())
        eq.append(personas.pop())
        equipos.append(eq)
    
    if len(personas) > 0:
        equipos[num_equipos - 1].append(personas.pop())

    return equipos
    


alumnos = [1,2,3,4,5,6,7,8,9]
for i in range(5):
    x = genera_equipos(alumnos)
    print(x)