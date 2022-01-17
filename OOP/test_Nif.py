import unittest
from Num_17_Ejercicio_Nif import Nif

class TestNif(unittest.TestCase):
    def test_clase_existe(self):
        nif = Nif()
        self.assertNotEqual(nif,None)
    

    