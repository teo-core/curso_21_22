import random

def genera_equipos(alumnos, miembros=2):
    random.shuffle(alumnos)
    equipos = []

    for i in range(0,len(alumnos),miembros):
        equipos.append(alumnos[i: i + miembros])

    return equipos



gente = ['Fernando', 'Alan', 'Jose', 'Rafa','Víctor', 'Antonio','Alejandro', 'Raúl']
#for i in range(5):
x = genera_equipos(gente,2)
print(x)