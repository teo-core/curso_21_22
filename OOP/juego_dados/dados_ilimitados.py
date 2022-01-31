from random import randint, shuffle


LIMITE_PUNTOS = 100
NUM_JUGADORES = 4
CARAS_DE_DADO = 6

class Jugador():
    def __init__(self) -> None:
        self.__puntos = 0 
        self.__nombre =''
    
    @property
    def puntos(self):
        return self.__puntos

    @puntos.setter
    def puntos(self, ptos):
        self.__puntos += ptos

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom


class Partida():
    def __init__(self) -> None:
        self.__jugadores = []
        self.__crea_lista_jugadores()
        self.__barajar_jugadores()
    
    def __crea_lista_jugadores(self):
        for j in range(NUM_JUGADORES):
            jug = Jugador()
            jug.nombre = f'Jugador_{j}'
            self.__jugadores.append(jug)
    
    def jugar(self,fn_callback):
        seguir = True
        tiradas = 0 

        while seguir:
            tiradas += 1
            for jugador in self.__jugadores:
                dado = randint(1,CARAS_DE_DADO)
                jugador.puntos = dado
                fn_callback((tiradas, jugador.nombre, jugador.puntos))
                if jugador.puntos >= LIMITE_PUNTOS:
                    fn_callback( (f"Ganador: {jugador.nombre}",))
                    seguir = False
                    break

    def __barajar_jugadores(self):
        shuffle(self.__jugadores)


# -----------------------------------------
def imprimir(cadena):
    if len(cadena) == 1:
        resp = cadena[0]
    else:
        resp = (f'El jugador {cadena[1]} lleva {cadena[0]} tiradas y {cadena[2]} puntos')

    print(resp)

# ------------------------------------------
p = Partida()
p.jugar(imprimir)
                