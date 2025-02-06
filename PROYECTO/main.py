from AgenteEstudiante import AgenteEstudiante
from AgenteCajero import AgenteCajero
from AgenteDirector import AgenteDirector
from AgenteResponsable import AgenteResponsable

def main():
    materias_disponibles = {"MATEMATICAS": 5, "FISICA": 5, "QUIMICA": 5, "HISTORIA": 5, "LITERATURA": 5}
    responsable = AgenteResponsable(materias_disponibles)
    director = AgenteDirector(responsable)
    cajero = AgenteCajero()

    # Habilitar materias para el semestre
    print("\n-------------------")
    print("| AGENTE RESPONSABLE|")
    print("---------------------")
    
    materias_a_habilitar = input("Ingrese las materias a habilitar para el semestre, separadas por comas: ").split(',')
    responsable.habilitar_materias(materias_a_habilitar)

    while True:
        print("\nOpciones:")
        print("1. Inscribir estudiante")
        print("2. Ver inscripciones actuales")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del estudiante: ")
            estudiante = AgenteEstudiante(nombre)

            cajero.cobrar_matricula(estudiante)

            if estudiante.boleta:  # Solo intentar inscribir si se generó una boleta
                estudiante.inscribirse(director)

        elif opcion == '2':
            print("\n-----------------")
            print("|   DIRECTOR    |")
            print("-----------------")
            print("Inscripciones actuales:")
            for materia, estudiantes in director.gestionar_inscripcion().items():
                print(f"Materia: {materia}, Estudiantes: {', '.join(estudiantes)}")

        elif opcion == '3':
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()