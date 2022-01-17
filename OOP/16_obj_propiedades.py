from datetime import date

class Persona():
    def __init__(self,nombre, apellido, fecha_nacimiento) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    @property
    def fecha_nacimiento(self):
        return self.__fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self,fecha):
        self.__fecha_nacimiento= fecha



p=Persona('teo','sanchez','1/1/2022')
print(p.fecha_nacimiento)

p.fecha_nacimiento = '01/01/2000'
print(p.fecha_nacimiento)





