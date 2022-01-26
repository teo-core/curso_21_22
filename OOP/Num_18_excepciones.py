def dividir(a,b):
    # 1.- comprobar que b no sea 0
    # 2.- dividir y controlar el error

    # if b == 0:
    #     return None
    # else:
    #     return a/b

    resultado = None
    try:
        #lista de instrucciones
        resultado = a/b
    except (ZeroDivisionError,TypeError) as e:
        #Instrucciones si hay error
        print("Se ha producido un error en la división.")
        print(type(e).__name__)
        print(e)
    # except TypeError:
    #     print('Solo se pueden dividir datos numéricos')
    else:
        print("Esta es la parte 'else'")
    finally:
        print('Esto es el finally')

    return resultado



print(dividir(9,'c'))