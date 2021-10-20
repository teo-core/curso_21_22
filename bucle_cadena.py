cadena = 'Hola caracola'
# for i in range(len(cadena)):
#     print(cadena[i].upper())

# ------------------------------
print('----------------------------------')
salida = ''
inversa = ''

for x in cadena:
    if x == ' ':
        break
    salida += x.upper()
    inversa = x.upper() + inversa
print(salida)
print(inversa)