class Base():
    datos = []


class Hijo1(Base):

    def __init__(self, elemento):
        self.datos.append(elemento)

    def datos_base(self):
        return super().datos


class Hijo2(Base):
 
    def __init__(self, elemento):
        self.datos.append(elemento)
    
    def __str__(self) -> str:
        return 'Soy el hijo 1'


h1 = Hijo1('Hijo1')
h2 = Hijo2('Hijo2')


print(h1.datos)
print(h2.datos)

