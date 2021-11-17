import pprint
import os
# import csv 
import pandas as pd

os.system('clear')

ruta = "/home/teo/codigo/curso_21_22/csv/"

def contador():
    df = pd.read_csv(ruta + 'titanic.csv')
    survived = df['Survived']

    vivos = 0
    muertos = 0

    for s in survived:
        if s == 1:
            vivos += 1
        else:
            muertos += 1
    return vivos,muertos

v,m = contador()
print('Vivieron:')
print(v)
print('Murieron:')
print(m)
