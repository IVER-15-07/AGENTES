class AgenteEstudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.boleta = None
        self.materias_inscritas = []
        self.estado = {}

    def actualizar_estado(self):
        self.estado = {
            'nombre': self.nombre,
            'boleta': self.boleta,
            'materias_inscritas': self.materias_inscritas
        }

    def inscribirse(self, director):
        print("\n-----------------")
        print("|   DIRECTOR    |")
        print("-----------------")
        director.solicitar_boleta_y_materias(self)
        self.actualizar_estado()

    def solicitar_inscripciones(self, director):
        return director.gestionar_inscripcion()