from materias import obtener_materias_por_semestre

class AgenteDirector:
    def __init__(self, responsable):
        self.inscripciones = {}
        self.responsable = responsable
        self.estado = {}
        self.modelo = self.modelo_del_mundo
        self.reglas = self.definir_reglas()

    def actualizar_estado(self, estudiante, materias):
        self.estado[estudiante.nombre] = {
            'boleta': estudiante.boleta,
            'materias': materias
        }

    def modelo_del_mundo(self, estado, accion, percepcion):
        # Actualiza el estado basado en la acción y la percepción
        estado_actualizado = estado.copy()
        estado_actualizado.update(percepcion)
        return estado_actualizado

    def definir_reglas(self):
        # Define las reglas del agente
        return {
            'boleta_correcta': lambda estado: estado['boleta'] == estado['boleta_ingresada'],
            'boleta_incorrecta': lambda estado: estado['boleta'] != estado['boleta_ingresada']
        }

    def buscar_regla(self, estado):
        # Busca la regla adecuada basada en el estado
        if self.reglas['boleta_correcta'](estado):
            return 'inscribir'
        elif self.reglas['boleta_incorrecta'](estado):
            return 'rechazar'

    def solicitar_boleta_y_materias(self, estudiante):
        percepcion = {'boleta_ingresada': estudiante.boleta}
        # Asegúrate de que 'boleta' esté en el estado inicial
        if 'boleta' not in self.estado:
            self.estado['boleta'] = None  # O algún valor predeterminado
        self.estado = self.modelo(self.estado, 'solicitar_boleta', percepcion)
        

         # Mensajes de depuración
        print(f"Estado actual: {self.estado}")
        print(f"Boleta ingresada: {estudiante.boleta}")
        regla = self.buscar_regla(self.estado)

        print(f"Regla seleccionada: {regla}")
        print(f"Boleta correcta: {self.reglas['boleta_correcta'](self.estado)}")

        if regla == 'inscribir':
            materias = obtener_materias_por_semestre(estudiante.semestre)
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