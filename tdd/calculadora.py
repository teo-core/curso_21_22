
def sumar(cadena):
    total = 0
    if str(cadena).startswith('//;\n'):
        partes = cadena.partition('\n')
        separador = partes[0][-1]
        cadena = partes[2].replace(separador, ',')

    cadena = cadena.replace('n',',')
    lista = cadena.split(',')
    longitud = len(lista)
    if cadena == '': #cadena vacía
        return 0

    for elem in lista:
        if not elem.isdigit():
            return "Error: Carácter no numérico"

    for i in lista:
        total += int(i)
    return total

# -----------------------------------------

# def mas_de_dos_numeros_da_error():
#     return sumar("1,2,3")

# def dos_numeros_devuelve_true():
#     return sumar('1,2')

def caracteres_no_numericos_devuelve_error():
    return sumar('a,c')

def cadena_vacia_devuelve_cero():
    return  sumar('')

def un_numero_devuelve_el_numero():
    return sumar('1')
def un_caracter_devuelve_el_numero():
    return sumar('a')

def dos_numeros_devuelve_suma():
    return sumar('2,3')

def numeros_ilimitados_devuelve_suma():
    return sumar('1,2,3,4')

def numeros_separados_por_n():
    return sumar('1n2n4n5,3')

def barra_barra_punto_coma_devuelve_suma():
    return sumar("//;\n1;2")

def valores_negativos_producen_error():
    return sumar("3,-6,15,-18,46,33") 
# ---------------------------
#print(mas_de_dos_numeros_da_error())

#print(dos_numeros_devuelve_true())

print(caracteres_no_numericos_devuelve_error())

print(cadena_vacia_devuelve_cero())

print(un_numero_devuelve_el_numero())

print(un_caracter_devuelve_el_numero())

print(dos_numeros_devuelve_suma())

print(numeros_ilimitados_devuelve_suma())

print(numeros_separados_por_n())

print(barra_barra_punto_coma_devuelve_suma())

print(valores_negativos_producen_error())