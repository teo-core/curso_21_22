#Decorador para comprobar si los parámetros son enteros
def son_enteros(funcion):
    def envoltura(*args):
        for i in args:
            if not type(i) is int:
                raise Exception('Parámetros no enteros')
        return funcion(*args)
        #Hacer más cosas
    return envoltura
        
@son_enteros
def suma(*args):
    return sum(args)

#Multiplicación de números enteros
@son_enteros
def multiplicacion(a,b):
    return a*b

# resp = son_enteros(multiplicacion)
# print(resp(2,'a'))

#resp = multiplicacion(2,6)
resp = suma(1,2,3,4,'a')
print(resp)
