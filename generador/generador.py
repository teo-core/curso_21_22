import os
import csv

class Generador():
    __MARCADOR ='##_##'
    __lista = None
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

    def __generar_tabla(self):       
        if self.__lista:
            tabla = '<table width="80%"><tr>'
            cabecera = list((self.__lista[0]).keys())
            for c in cabecera:
                tabla += f'<td>{c}</td>'
            tabla += '</tr>'
        

        for fila in self.__lista:
            tabla += '<tr>'
            for col in list(fila.values()):
                tabla += f'<td>{col}</td>'
            tabla += '</tr>'
        
        tabla += '</table>'

        return tabla

    def generar_pagina(self,lista):
        self.__lista = lista
        vacio = self.__generar_esqueleto()
        
        pag = self.__generar_tabla()
        completa= vacio.replace(self.__MARCADOR,pag)
        return completa

        


# -----------------------
def leer_dict():
    csv_in = open('/home/teo/codigo/curso_21_22/generador/annual-enterprise-survey-2020.csv')
    lector_dict = csv.DictReader(csv_in)

    lista_dict = list(lector_dict)

    csv_in.close()
    return lista_dict

elementos = leer_dict()
g = Generador()
pagina = g.generar_pagina(elementos)

with open('/home/teo/codigo/curso_21_22/generador/tabla_2.html','w') as arch:
    arch.write(pagina)

