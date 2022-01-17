import unittest
from NIF import Nif

class TestNif(unittest.TestCase):
    def test_clase_existe(self):
        nif = Nif()
        self.assertNotEqual(nif,None)

    def test_constructor_num_cero_letra_blanco(self):
        nif = Nif()
        self.assertEqual(nif.numero,0)
        self.assertEqual(nif.letra,' ')
    
    def test_numero_calcula_letra(self):
        nif = Nif(20000000)
        self.assertCountEqual(nif.letra,'M')
        nif = Nif(29435060)
        self.assertCountEqual(nif.letra,'M')
        nif = Nif(75541171)
        self.assertCountEqual(nif.letra,'V')   

    def test_numero_setter_calcula_letra(self)   :
        nif = Nif()
        nif.numero = 20000000
        self.assertEqual(nif.letra,'M')
    
    def test_print_dni(self):
        nif = Nif()
        nif.numero = 20000000
        self.assertEqual(nif.__str__(),'20000000-M')


