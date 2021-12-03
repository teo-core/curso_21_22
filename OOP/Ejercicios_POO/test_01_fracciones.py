import unittest
from ejer_01_fracciones import Racional


class TestFracciones(unittest.TestCase):
    
    def test_init_con_dos_valores(self):
        frac = Racional(1,1)
        self.assertEqual(frac.get_numerador(), 1)
        self.assertEqual(frac.get_denominador(),1)

    def test_multiplicar(self):
        frac1 = Racional(1,2)
        frac2 = Racional(3,4)
        frac1.multiplicar(frac2)
        self.assertEqual(frac1.get_numerador(),3)
        self.assertEqual(frac1.get_denominador(),8)

    


