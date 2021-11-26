class Vehiculo():
    marca = None
    _modelo = None
    __numero_serie = None
    __estado = 'Parado'
    __velocidad = 0

    def __init__(self, marca, modelo, numero_serie) -> None:
        self.marca = marca
        self._modelo = modelo
        self.__numero_serie = numero_serie

    def get_num_serie(self):
        return self.__numero_serie
    
    def get_estado(self):
        if(self.__estado == 'Moviéndose'):
            return self.__estado + f' a {self.__velocidad} Km/h.'
        else:
            return self.__estado

    def moverse(self, velocidad_inicial):
        self.acelerar(velocidad_inicial)
        print('acelerando...')
        self.__estado = 'Moviéndose'

    def pararse(self, velocidad_final):
        self.acelerar(velocidad_final)
        print('parando....')
        self.__estado = 'Parado'

    def acelerar(self, nueva_velocidad):
        self.__velocidad = nueva_velocidad




class Coche(Vehiculo):
    __matricula = None
    __numero_ruedas = 4

    def __init__(self, matricula, marca, modelo, numero_serie) -> None:
        super().__init__(marca, modelo, numero_serie)
        self.__matricula = matricula
    
    def get_matricula(self):
        return self.__matricula

        


    

c = Coche('1234-JKL', 'Renault', '4L','1234KKK')
   
print(f'Vehículo matrícula {c.get_matricula()} marca {c.marca} y modelo {c._modelo}, con número de serie {c.get_num_serie()}')




"""
Modificadres de acceso:
- Público
- Protegido
- Privado

"""

# v = Vehiculo('Mercedes','slk 100','123456HGTRD988')

# print(f'Vehículo marca {v.marca} y modelo {v._modelo}, con número de serie {v.get_num_serie()}')
# print(f'El vehículo está {v.get_estado()}')
# v.moverse(10)
# print(f'El vehículo está {v.get_estado()}')
# v.pararse(1)
# print(f'El vehículo está {v.get_estado()}')

