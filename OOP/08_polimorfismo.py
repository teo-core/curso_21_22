class Spain():

    def __str__(self) -> str:
        return 'España'

    def capital(self):
        print('La capital de España es Madrid')
    
    def idioma(self):
        print('El idioma oficial es el castellano')


class Portugal():

    def __str__(self) -> str:
        return 'Portugal'

    def capital(self):
        print('La capital de Portugal es Lisboa')
    
    def idioma(self):
        print('El idioma oficial es el portugués')


class Francia():

    def __str__(self) -> str:
        return 'Francia'

    def capital(self):
        print('La capital de Francia es París')
    
    def idioma(self):
        print('El idioma oficial es el francés')


class Aduana():
    def pasar(self, origen, destino):
        print(f'Antes estaba en {origen}')
        print(f'Ahora estoy en {destino}')
        origen.capital()
        origen.idioma()
        print('-------------------')
        destino.capital()
        destino.idioma()


esp = Spain()
por = Portugal()
fra = Francia()

paises = [esp, por]

# print(por)
# for p in paises:
#     p.capital()
#     p.idioma()

aduana = Aduana()

aduana.pasar(esp,fra)
print('*************************')
aduana.pasar(fra,por)
print('*************************')
aduana.pasar(por,esp)