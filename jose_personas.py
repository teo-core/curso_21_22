from typing import Dict
import pprint

def func_llena_diccionario(dic :Dict):       
    entrada_usuario_k = input("Si ha finalizado pulse ENTER. \nSi desea continuar, por favor, introduzca clave a guardar: ")
    if entrada_usuario_k == '':
        print('cadena VACIA')
        return(False)
    entrada_usuario_v = input("Y ahora el valor para esa clave: ")
    dic[entrada_usuario_k] = entrada_usuario_v
    return(True)
    

datos_usuario = {}
datos_max = 20
no_hemos_terminado = True
no_hemos_terminado = func_llena_diccionario(datos_usuario)

for i in range(datos_max):
    print(f'No hemos termninado es:  {no_hemos_terminado}')
    if no_hemos_terminado:
        no_hemos_terminado = func_llena_diccionario(datos_usuario)
    else:
        break

pprint.pprint(datos_usuario)
for k,v in datos_usuario.items():
    pprint.pprint(f'{k}: {v}')
