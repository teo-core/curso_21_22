# Variables locales y globales
v_global = 'Soy global'
v_contador = 0


def f1():
    v_contador = 100
    v_global ='Modificada'
    print(v_global)
    if x == 3: 
        pass
    


f1()
print(v_contador)
print(v_global)