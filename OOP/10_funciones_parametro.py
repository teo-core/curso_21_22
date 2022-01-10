def sumar(a,b):
    return a + b

def restar(a,b):
    return a - b

def calcular(operacion, a, b):
    #hacer cosas
    
    total = operacion(a,b)

    #hacer mas cosas
    return total

print(calcular(restar,1,2))