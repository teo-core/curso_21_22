
# pedir fecha nacimiento
#    25/01/2000
# Naciste el día 25 de enero del año 2000

# 1.- Pedir el input de la fecha de nacimiento

# 2.- Dividir la fecha en dd, mm, aaa

# 3.- Componer el mensaje de salida
def nacimiento():
    meses =['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 
    'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']

    fecha = input('Dime cuando naciste (dd/mm/aaaa): ')
    partes = fecha.split('/')
    mes = int(partes[1]) - 1
    mensaje = 'Naciste el día ' + partes[0] + ' del mes ' + meses[mes] + ' del año ' + partes[2]
    return mensaje
    





def nacimiento_2():
    meses ={1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 
    8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}

    fecha = input('Dime cuando naciste (dd/mm/aaaa): ')
    partes = fecha.split('/')
    mensaje = 'Naciste el día ' + partes[0] + ' del mes ' + meses[int(partes[1])] + ' del año ' + partes[2]
    return mensaje

print(nacimiento_2())