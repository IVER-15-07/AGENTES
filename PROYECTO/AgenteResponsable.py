class AgenteResponsable:
    def __init__(self, materias_disponibles):
        self.materias_disponibles = materias_disponibles  # Diccionario {materia: cupo}
        self.materias_habilitadas = set()
        self.estado = {}

    def actualizar_estado(self):
        self.estado = {
            'materias_disponibles': self.materias_disponibles,
            'materias_habilitadas': list(self.materias_habilitadas)
        }

    def habilitar_materias(self, materias):
        for materia in materias:
            if materia in self.materias_disponibles:
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