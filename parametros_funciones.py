def funcion(p1, p2, p3=0,*args, **kwargs):
    print(p1, p2, p3)
    print(args)
    print(kwargs)

funcion(1,2,98,0,9,8,7,6,5,4,3,2,1,nombre='teo',dia='viernes')