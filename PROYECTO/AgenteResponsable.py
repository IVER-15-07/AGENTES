from materias import materias_por_nivel

class AgenteResponsable:
    def __init__(self):
        self.materias_disponibles = {materia: 5 for nivel in materias_por_nivel.values() for materia in nivel}
        self.materias_habilitadas = set()
        self.estado = {
            'materias_disponibles': self.materias_disponibles,
            'materias_habilitadas': list(self.materias_habilitadas)
        }
        self.modelo = self.modelo_del_mundo
        self.reglas = self.definir_reglas()

    def actualizar_estado(self):
        self.estado = {
            'materias_disponibles': self.materias_disponibles,
            'materias_habilitadas': list(self.materias_habilitadas)
        }

    def modelo_del_mundo(self, estado, accion, percepcion):
        # Actualiza el estado basado en la acción y la percepción
        estado_actualizado = estado.copy()
        estado_actualizado.update(percepcion)
        return estado_actualizado

    def definir_reglas(self):
        # Define las reglas del agente
        return {
            'materia_disponible': lambda estado, materia: materia in estado['materias_disponibles'],
            'materia_no_disponible': lambda estado, materia: materia not in estado['materias_disponibles']
        }

    def buscar_regla(self, estado, materia):
        # Busca la regla adecuada basada en el estado
        if self.reglas['materia_disponible'](estado, materia):
            return 'habilitar'
        elif self.reglas['materia_no_disponible'](estado, materia):
            return 'rechazar'

    def habilitar_materias(self, materias):
        for materia in materias:
            percepcion = {'materia': materia}
            self.estado = self.modelo(self.estado, 'habilitar_materias', percepcion)
            regla = self.buscar_regla(self.estado, materia)
            if regla == 'habilitar':
                self.materias_habilitadas.add(materia)
                print(f"Responsable: La materia {materia} ha sido habilitada.")
            else:
                print(f"Responsable: La materia {materia} no está disponible para habilitar.")
        self.actualizar_estado()

    def verificar_habilitacion(self, materia):
        return materia in self.materias_habilitadas

    def cerrar_materias(self):
        materias_cerradas = []
        for materia, cupo in self.materias_disponibles.items():
            if cupo <= 4:
                materias_cerradas.append(materia)

        for materia in materias_cerradas:
            del self.materias_disponibles[materia]
            print(f"Responsable: La materia {materia} ha sido cerrada por alcanzar el cupo máximo de 4 estudiantes")
        self.actualizar_estado()