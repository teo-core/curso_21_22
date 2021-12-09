class Batidora():
    __motor = 0
    suscriptores = []
    def encender(self):
        self.__motor = 100
        print('Encendiendo')

    def apagar(self):
        self.__motor = 0
        print('Apagando')

    def acelerar(self):
        self.__motor *= 1.1
        print('Acelerando')
        for s in self.suscriptores:
            s(self.__motor)


#######################################

def muestra_velocidad(vel):
    print(f'La velocidad de la batidora es {vel}')

def otra_funcion(vel):
    if vel > 120:
        print(f'Velocidad excesiva: {vel}')

b = Batidora()
b.suscriptores.append(muestra_velocidad)
b.suscriptores.append(otra_funcion)
# ------------------------------
b.encender()
b.acelerar()
b.acelerar()
b.acelerar()
b.apagar()


