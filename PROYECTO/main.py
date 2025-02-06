from AgenteEstudiante import AgenteEstudiante
from AgenteCajero import AgenteCajero
from AgenteDirector import AgenteDirector
from AgenteResponsable import AgenteResponsable
from materias import obtener_materias_por_semestre

def main():
    responsable = AgenteResponsable()
    director = AgenteDirector(responsable)
    cajero = AgenteCajero()

    print("\nIngrese los datos del estudiante en el siguiente formato:")
    print("Nombre, Dinero, Semestre")
    entrada = input("Datos del estudiante: ")
    nombre, dinero, semestre = entrada.split(', ')
    dinero = float(dinero)

    estudiante = AgenteEstudiante(nombre, dinero, semestre)

    # Habilitar materias automáticamente
    materias = obtener_materias_por_semestre(semestre)
    responsable.habilitar_materias(materias)

    # Cobrar matrícula automáticamente
    cajero.cobrar_matricula(estudiante)

    # Inscribir estudiante automáticamente
    if estudiante.boleta:  # Solo intentar inscribir si se generó una boleta
        estudiante.inscribirse(director)

    print("\nInscripciones actuales:")
    for materia, estudiantes in director.gestionar_inscripcion().items():
        print(f"Materia: {materia}, Estudiantes: {', '.join(estudiantes)}")

if __name__ == "__main__":
    main()