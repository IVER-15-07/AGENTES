class AgenteEstudiante:
    def __init__(self, nombre, dinero, semestre):
        self.nombre = nombre
        self.dinero = dinero
        self.semestre = semestre
        self.boleta = None
        self.materias_inscritas = []
        self.estado = {
            'con_boleta': False,
            'materias_lista': []
        }
        self.modelo = self.modelo_del_mundo
        self.reglas = self.definir_reglas()

    def actualizar_estado(self):
        self.estado = {
            'nombre': self.nombre,
            'dinero': self.dinero,
            'boleta': self.boleta,
            'materias_inscritas': self.materias_inscritas,
            'con_boleta': self.boleta is not None
        }

    def modelo_del_mundo(self, estado, accion, percepcion):
        # Actualiza el estado basado en la acción y la percepción
        estado_actualizado = estado.copy()
        estado_actualizado.update(percepcion)
        return estado_actualizado

    def definir_reglas(self):
        # Define las reglas del agente
        return {
            'tiene_boleta': lambda estado: estado['con_boleta'],
            'no_tiene_boleta': lambda estado: not estado['con_boleta']
        }

    def buscar_regla(self, estado):
        # Busca la regla adecuada basada en el estado
        if self.reglas['tiene_boleta'](estado):
            return 'inscribirse'
        elif self.reglas['no_tiene_boleta'](estado):
            return 'solicitar_boleta'

    def inscribirse(self, director):
        director.solicitar_boleta_y_materias(self)
        self.actualizar_estado()

    def mostrar_estado(self):
        print("\n=== Estado Actual del Estudiante ===")
        print(f"Nombre: {self.nombre}")
        print(f"Monto Total: {self.dinero}bs")
        print(f"Semestre: {self.semestre}")

    def solicitar_inscripciones(self, director):
        return director.gestionar_inscripcion()