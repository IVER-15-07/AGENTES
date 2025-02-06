import random
import time

class AgenteCajero:
    def __init__(self):
        self.boletas = {}

    def cobrar_matricula(self, estudiante):
        print("\n-----------------")
        print("|    CAJERO     |")
        print("-----------------")
        while True:
            try:
                monto = float(input(f"Ingrese el monto de la matrícula para {estudiante.nombre} (debe ser 14 Bs): "))
                if monto != 14:
                    print("Error: El monto de la matrícula debe ser 14 Bs.")
                else:
                    break
            except ValueError:
                print("Monto inválido. Por favor, ingrese un número.")

        print("Generando boleta, por favor espere...")
        time.sleep(3)  # Simula un retraso de 3 segundos
        codigo_boleta = f"BOLETA-{random.randint(1000, 9999)}"
        self.boletas[estudiante.nombre] = codigo_boleta
        estudiante.boleta = codigo_boleta
        print(f"Matricula cobrada a {estudiante.nombre}. Boleta: {codigo_boleta}")

    def entregar_boletas(self):
        return self.boletas