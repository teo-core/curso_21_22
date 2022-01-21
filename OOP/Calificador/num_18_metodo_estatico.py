"""
Crear una clase Calificaciones.
Tendrá un método init que admitirá como entrada una lista de forma ['Raul',9.2,5,4.5,7,9.1]
Tendra un método 'calificar' que nos devolverá ['Raul', 'Notable']

"""

class Calificaciones():
    def __init__(self,alumno_notas=[]) -> None:

        if alumno_notas:
            self.nombre = alumno_notas[0]
            self.notas = alumno_notas[1:]
            self.calificacion = self.calcula_calificacion()
        else:
            self.nombre = ''
            self.notas = []
            self.calificacion = ''
    
    def __str__(self) -> str:
        return f'Alumno: {self.nombre} tiene la calificación {self.calificacion}'

    def calcula_calificacion(self):
        calificacion = ''

        if self.notas:
            nota_media = sum(self.notas)/len(self.notas)
            if nota_media < 5:
                calificacion = 'SUSPENSO'
            elif nota_media < 7:
                calificacion = 'BIEN'
            elif nota_media < 9:
                calificacion = 'NOTABLE'
            else:
                calificacion = 'SOBRESALIENTE'
            
        else:
            calificacion = None
        
        return calificacion