def doble(numero):
    
    if type(numero) in [int,float, complex]:
        return numero * 2
    else:
        return None

print(doble(3))
print(doble('jojoj'))
print(doble(2.87887))
print(doble(2+8j))
print(doble([1,2,3]))
