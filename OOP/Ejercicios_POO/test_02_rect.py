import unittest
from ej_02_punto import Punto, Rectangulo


class TestRectangulo(unittest.TestCase):
    def test_es_rectangulo(self):
        p1 = Punto(4,2)
        p2 = Punto(3,-1)
        r = Rectangulo(p1,p2)
        self.assertEqual(r.v1,Punto(4,2))
        self.assertEqual(r.v2,Punto(3,-1))
        self.assertEqual(r.v3,Punto(4,-1))
        self.assertEqual(r.v4, Punto(3,2))