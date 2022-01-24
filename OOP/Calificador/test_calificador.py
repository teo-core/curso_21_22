from num_18_metodo_estatico import Calificaciones
import unittest as ut

class TestCalificaciones(ut.TestCase):
    def test_existencia(self):
        cal = Calificaciones()
        self.assertNotEqual(cal, None)

    def test_constructor_vacio_propiedades_vacias(self):
        cal = Calificaciones()
        self.assertEqual(cal.alumno, '')
        self.assertEqual(cal.notas, [])

    def test_constructor_recibe_valores_establece_props(self):
        cal = Calificaciones(['Raul',9.2,5,4.5,7,9.1])
        self.assertEqual(cal.alumno, 'Raul')
        self.assertEqual(cal.notas, [9.2,5,4.5,7,9.1])

    def test_metodo_str_devuelve_alumno_calificacion(self):
        cal = Calificaciones(['Raul',9.2,5,4.5,7,9.1])
        cadena = cal.__str__()
        self.assertEqual(cadena,'Alumno: Raul tiene la calificación BIEN')

    def test_calcula_calificacion_vacio_devuelve_None(self):
        cal = Calificaciones()
        self.assertEqual(cal.calcula_calificacion(),None)
        
    def test_calcula_calificacion_no_vacio_devuelve_calificacion(self):
        cal = Calificaciones(['Raul',9.2,5,4.5,7,9.1])
        self.assertEqual(cal.calcula_calificacion(),'BIEN')
        self.assertEqual(cal.calificacion,'BIEN')

    # def test_alumno_no_inicializado_asignar_nombre_calif(self):
    #     cal = Calificaciones()
    #     cal.set_alumno(['Pedro',9.7])
    #     self.assertEqual(cal.nombre,'Pedro')
    #     self.assertEqual(cal.notas,[9.7])
    #     self.assertEqual(cal.calificacion,'SOBRESALIENTE')

    def test_asigna_valores_alumno_nulo(self):
        cal = Calificaciones()
        cal.nombre = 'Paco'
        self.assertEqual(cal.nombre,'Paco')

    
    def test_asigna_notas(self):
        cal = Calificaciones()
        cal.notas = [5,6,7,8,9,10]

        self.assertEqual(cal.notas,[5,6,7,8,9,10])
        self.assertEqual(cal.calificacion,'NOTABLE')    

    def test_validar_notas_incorrectas(self):
        lista_notas = [1,22]
        self.assertEqual(Calificaciones.valida_notas(lista_notas),False)

    def test_validar_notas_incorrectas_cadena(self):
        lista_notas = [1,'hola']
        self.assertEqual(Calificaciones.valida_notas(lista_notas),False)

    def test_validar_notas_correctas(self):
        lista_notas = [5,6.2,7,8,9,10]
        self.assertEqual(Calificaciones.valida_notas(lista_notas),True)