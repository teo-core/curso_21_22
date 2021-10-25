import random

def genera_equipos(alumnos, miembros=2):
    random.shuffle(alumnos)
    equipos = []

    for i in range(0,len(alumnos),miembros):
        equipos.append(alumnos[i: i + miembros])

    return equipos



gente = [1,2,3,4,5,6,7,8,9]
for i in range(5):
    x = genera_equipos(gente,2)
    print(x)