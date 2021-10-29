import pprint

frase = """
El glam metal, también conocido como hair metal, es un subgénero musical del heavy metal que combina aspectos sonoros del heavy metal tradicional, hard rock, punk y del pop, con la apariencia visual del glam rock. Influidos mayormente por las bandas estadounidenses de hard rock de los años setenta, los primeros artistas del glam aparecieron a finales de la misma década y principios de la siguiente en los clubes nocturnos del Sunset Strip en Los Ángeles, Estados Unidos. 
"""
def cuenta_palabras(frase):
    palabras = frase.split(' ')
    dic_palabras = {}
    for p in palabras:
        if p in dic_palabras:
            dic_palabras[p] += 1
        else:
            dic_palabras[p] = 1
    
    return dic_palabras


pprint.pprint(cuenta_palabras(frase))