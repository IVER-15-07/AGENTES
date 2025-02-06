from AgenteEstudiante import AgenteEstudiante
from AgenteCajero import AgenteCajero
from AgenteDirector import AgenteDirector
from AgenteResponsable import AgenteResponsable
from materias import obtener_materias_por_semestre
import time

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
    print(f"DINERO DEL ESTUDIANTE : {estudiante.dinero} \n TIEMPO : 1seg equivales 1dia \nTIEMPO DE TODO EL PROCESO : 3dias")
    print("=========================== DIA 1 ===============================")
    print("=== Agente Cajero ===")
    # Cobrar matrícula automáticamente
    cajero.cobrar_matricula(estudiante)
    time.sleep(1)  # Simula un retraso de 1 segundo
    

    print("\n========================= DIA 2 ===============================")
    print("=== Agente Responsable ===")
    materias = obtener_materias_por_semestre(semestre)
    responsable.habilitar_materias(materias)
    time.sleep(2)  # Simula un retraso de 1 segundo



    print("============================== DIA 3 ==============================")
    print("=== Agente Director ===")
    # Inscribir estudiante automáticamente
    if estudiante.boleta:  # Solo intentar inscribir si se generó una boleta
        estudiante.inscribirse(director)
    time.sleep(2)  # Simula un retraso de 1 segundo


    print("\nInscripciones actuales:")
    for materia, estudiantes in director.gestionar_inscripcion().items():
        print(f"Materia: {materia}, Estudiantes: {', '.join(estudiantes)}")

if __name__ == "__main__":
    main()