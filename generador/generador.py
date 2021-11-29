class Generador():
    __esqueleto = """
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
    def __generar_esqueleto(self):
        return self.__esqueleto

    def __generar_tabla(self,lista):
        pass

    def generar_pagina(self, lista):
        if not lista:
            return self.__generar_esqueleto()

        
