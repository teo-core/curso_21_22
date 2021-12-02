class Pajaro():
    def __str__(self) -> str:
        return 'Pájaro'    
    def cantar(self):
        print('Los pájaros tienen cantos diferentes')

class Gorrion(Pajaro):
    def __str__(self) -> str:
        return 'Gorrión'
    def cantar(self, con_padre=False):
        if con_padre:
            super().cantar()
        print('Gorrión pio, pio')


class Gallo(Pajaro):
    def __str__(self) -> str:
        return 'Gallo'    
    def cantar(self,con_padre=False):
        if con_padre:
            super().cantar()
        print('Gallo kikirikíiii')


# g = Gorrion()
# g.cantar()

# gallo = Gallo()
# gallo.cantar(True)

class CoroPajaros():
    def __init__(self, lista_pajaros) -> None:
        self.coro = lista_pajaros
    
    def cantar(self):
        titulo = True
        for p in self.coro:
            # p.cantar(titulo)
            # titulo = False
            if issubclass(p.__class__ ,Pajaro):
                print(f'Este es un pájaro: {p}')
            else:
                print(f'Esto NO es un pájaro: {p}')


        # for p in range(len(self.coro)):
        #     if p == 0:
        #         self.coro[p].cantar(True)
        #     else:
        #         self.coro[p].cantar()



lista_pajaros = [Gallo(),'p',1,'l'] #[Gallo(),Gallo(),Gorrion()]
c = CoroPajaros(lista_pajaros)
c.cantar()


