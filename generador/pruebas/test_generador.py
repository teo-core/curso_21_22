import unittest
from generador import Generador

class TestGenerador(unittest.TestCase):
    esqueleto = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            ##_##
        </body>
        </html>
    """
    def test_get_esqueleto(self):
        g = Generador()
        resp = g.generar_pagina([])
        self.assertEqual(resp,self.esqueleto)
