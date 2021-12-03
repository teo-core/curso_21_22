class Racional():
    # Constructor que admita numerador y denominador
    # Constructor sin parámetros
    # Métodos getters y setters
    # Suma, Resta, Multiplicación y División

    def __init__(self, numerador = 0, denominador =1) -> None:
        self.__numerador = numerador
        self.set_denominador(denominador)


    def get_numerador(self):
        return self.__numerador

    def set_numerador(self, valor):
        self.__numerador = valor


    def get_denominador(self):
        return self.__denominador


    def set_denominador(self, valor):
        if valor == 0:
            raise ValueError('ERROR: El denominador no puede ser cero')
        
        self.__denominador = valor


    def multiplicar(self,valor):
        num = self.get_numerador() * valor.get_numerador()
        den = self.get_denominador() * valor.get_denominador()
        self.set_numerador(num)
        self.set_denominador(den)

