class Punto():
    x = 0
    y = 0
    def __init__(self,x,y) -> None:
        self.set_x(x)
        self.set_y(y)

    def set_x(self,valor):
        if type(valor) in [int,float]:
            self.x = valor
        
    def set_y(self,valor):
        if type(valor) in [int,float]:
            self.y = valor


class Rectangulo():
    v1 = v2 = v3 = v4 = Punto(0,0)
    def __init__(self, p1, p2) -> None:
        self.v1 = p1
        self.v2 = p2
        self.v3 = Punto(p1.x,p2.y)
        self.v4 = Punto(p2.x, p1,y)


