class Nif():
    dic_letras = {
        0 : 'T',7 : 'F',1 : 'R' ,8 : 'P',2 : 'W',9 : 'D',3 :'A',10:'X',
        4 : 'G',11 : 'B',5 : 'M',12 : 'N',6 : 'Y',13 : 'J',14 : 'Z',
        21 : 'K',15 : 'S',22 : 'E',16 : 'Q',17 : 'V' ,18 : 'H',19 : 'L',20 : 'C'
    }
    def __init__(self,numero=0, letra=' '):
        self.__numero = numero
        
        if numero:
            self.__letra = self.__calcula_letra()
        else:
            self.__letra = ' '
    
    def __str__(self) -> str:
        return f'{self.__numero}-{self.__letra}'

    @property
    def numero(self):
        return self.__numero

    @numero.setter
    def numero(self, numero):
        self.__numero = numero
        self.__letra = self.__calcula_letra()
    
    @property
    def letra(self):
        return self.__letra

    def __calcula_letra(self):
        resto = self.__numero % 23
        return self.dic_letras[resto]



