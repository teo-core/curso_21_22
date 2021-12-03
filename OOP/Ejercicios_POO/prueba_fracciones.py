from  ejer_01_fracciones import Racional

r = Racional(-12,-3)
print(f'Numerador: {r.get_numerador()}\nDenominador: {r.get_denominador()}')

try:
    r = Racional(1,0)
except:
    print("El denominador no puede ser cero")

