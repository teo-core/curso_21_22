def lee_fichero(nombre):
    try:
        f = open(nombre)
    except Exception as e:
        print(f'Error abriendo el archivo: {type(e).__name__}')
    else:
        datos = f.read()
        print(datos)

#lee_fichero('hola.txt')


def lee_fichero_2(nombre):
    try:
        raise FileNotFoundError('Este es un error provocado')
    except FileNotFoundError as e:
        print(f'Error abriendo el archivo: {type(e).__name__}')
        print(e)

lee_fichero_2('')