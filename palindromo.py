def limpiar(cadena):
    aux = cadena.lower()
    aux = aux.replace(" ","")
    aux = aux.replace(".","")
    aux = aux.replace(",","")
    aux = aux.replace(";","")
    aux = aux.replace(":","")
    aux = aux.replace("á","a")
    aux = aux.replace("é","e")
    aux = aux.replace("í","i")
    aux = aux.replace("ó","o")
    aux = aux.replace("ú","u")
    return aux

print(limpiar('No subas, abusón'))  #nosubasabuson 
print(limpiar('Sometamos o matemos'))   #sometamosomatemos



def palindromo(cadena):
    aux = limpiar(cadena)
    return aux == aux[::-1]


# s = input('dame una cadena: ')
# print(palindromo(s))

print(palindromo('ana'))   #true
print(palindromo('hola'))  #false
print(palindromo('canac')) #true
print(palindromo('abba'))  #true
print(palindromo('Ana'))   #true
print(palindromo('No subas, abusón'))   #true
print(palindromo('Sometamos o matemos'))   #true
