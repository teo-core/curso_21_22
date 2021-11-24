import os
import pprint

class Coche():
    matricula = None
    num_puertas = None
    color = None
    motor_en_marcha = False

    def __init__(self, matr, puertas, col):
        self.matricula = matr
        self.num_puertas = puertas
        self.color = col
        

    def __str__(self):
        return f'Matricula: {self.matricula}\nNúmero de puertas: {self.num_puertas}\nColor: {self.color}'
        
    def arrancar(self):
        self.motor_en_marcha = True

    def apagar(self):
        self.motor_en_marcha = False


    


os.system('clear')
bmw = Coche('9090-KKK',3,'Azul')

print(bmw.color)
print(bmw.num_puertas)
print(bmw.matricula)


print(bmw)

bmw.arrancar()
print('Motor: ', bmw.motor_en_marcha)

bmw.color = 'Verde'
bmw.matricula = '1234-llk'
bmw.num_puertas = 2
bmw.precio = 20000
bmw.marca = 'BMW'
bmw.modelo = 'Panda'



print(bmw.color)
print(bmw.num_puertas)
print(bmw.matricula)
print(bmw.precio)
# pprint.pprint(dir(bmw))
# pprint.pprint(bmw.__class__)
# pprint.pprint(bmw.__dict__)
print(bmw)
bmw.apagar()
print('Motor: ', bmw.motor_en_marcha)

