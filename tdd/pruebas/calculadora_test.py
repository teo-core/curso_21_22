import unittest
import calculadora

class CalculadoraTest(unittest.TestCase):
    def test_caracteres_no_numericos_devuelve_error(self):
        respuesta = calculadora.sumar('a,b')
        self.assertEqual(respuesta,"Error: Carácter no numérico")