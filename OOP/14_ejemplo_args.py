def sumar(*args):
    if type(args[0]) is str:
        lista = []
        for i in args:
            for elem in i.split(','):
                if elem.isdigit():
                    lista.append(int(elem))
    else:
        lista = args
    for i in lista:
        print(i)

sumar('1,2,3,4')