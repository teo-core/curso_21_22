class Persona():
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        

p1 = Persona('Alan', 22, '222222H')

print(p1.nombre, p1.edad, p1.dni)

p2 = Persona('--',0,'**')
p2.equipo = 'Betis'
print(p2.nombre, p2.edad, p2.dni)