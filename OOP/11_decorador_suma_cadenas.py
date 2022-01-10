def decorador_suma(funcion_que_suma):
    def envoltura(*args):
        if not type(args) == tuple:
            lista = tuple(args)
            return funcion_que_suma(lista) 
        else:
            return funcion_que_suma(args)   
    return envoltura




@decorador_suma
def sumar(*args):
    return sum(args)

print(sumar(1,2,3,4,5,6))