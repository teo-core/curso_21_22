import unittest
from ej_02_punto import Punto, Rectangulo

class TestPunto(unittest.TestCase):
    def test_constructor_0_0_devuelve_0_0(self):
        p = Punto(0,0)
        self.assertEqual(p.x,0)
        self.assertEqual(p.y,0)


    def test_x_y_no_int_da_error(self):
        p = Punto('p','o')
        self.assertEqual(p.x,0)
        self.assertEqual(p.y,0)

    def test_x_y_complejo_no_int_da_error(self):
        p = Punto((1+2j),'o')
        self.assertEqual(p.x,0)
        self.assertEqual(p.y,0)

    def test_x_y_float_no_da_error(self):
        p = Punto(1.2,3.4)
        self.assertEqual(p.x,1.2)
        self.assertEqual(p.y,3.4)

class TestRectangulo(unittest.TestCase):
    def test_es_rectangulo(self):
        p1 = Punto(4,2)
        p2 = Punto(3,-1)
        r = Rectangulo(p1,p2)
        self.assertEqual(r.v1,Punto(4,2))
        self.assertEqual(r.v2,Punto(3,-1))
        self.assertEqual(r.v3,Punto(4,-1))
        self.assertEqual(r.v4, Punto(3,2))