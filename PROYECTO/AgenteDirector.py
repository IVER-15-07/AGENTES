class AgenteDirector:
    def __init__(self, responsable):
        self.inscripciones = {}
        self.responsable = responsable
        self.estado = {}

    def actualizar_estado(self, estudiante, materias):
        self.estado[estudiante.nombre] = {
            'boleta': estudiante.boleta,
            'materias': materias
        }

    def solicitar_boleta_y_materias(self, estudiante):
        boleta_ingresada = input(f"Ingrese la boleta de pago para {estudiante.nombre}: ")
        if boleta_ingresada == estudiante.boleta:
            materias = input(f"Ingrese las materias para {estudiante.nombre} separadas por comas: ").split(',')
            self.actualizar_estado(estudiante, materias)
            self.inscribir(estudiante, materias)
        else:
            print(f"Boleta incorrecta. {estudiante.nombre} no puede inscribirse.")

    def inscribir(self, estudiante, materias):
        if estudiante.boleta:
            for materia in materias:
                if self.responsable.verificar_habilitacion(materia):
                    if materia not in self.inscripciones:
                        self.inscripciones[materia] = []
                    self.inscripciones[materia].append(estudiante.nombre)
                    estudiante.materias_inscritas.append(materia)
                    print(f"{estudiante.nombre} inscrito en la materia: {materia}")
                else:
                    print(f"Responsable: La materia {materia} no está habilitada.")
        else:
            print(f"{estudiante.nombre} no tiene boleta de pago.")

    def gestionar_inscripcion(self):
        return self.inscripciones