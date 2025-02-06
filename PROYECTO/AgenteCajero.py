import random
import time

class AgenteCajero:
    def __init__(self):
        self.boletas = {}
        self.estado = {}
        self.modelo = self.modelo_del_mundo
        self.reglas = self.definir_reglas()

    def actualizar_estado(self, estudiante):
        self.estado[estudiante.nombre] = {
            'boleta': estudiante.boleta
        }

    def modelo_del_mundo(self, estado, accion, percepcion):
        # Actualiza el estado basado en la acción y la percepción
        estado_actualizado = estado.copy()
        estado_actualizado.update(percepcion)
        return estado_actualizado

    def definir_reglas(self):
        # Define las reglas del agente
        return {
            'monto_correcto': lambda estado: estado['monto'] == 22,
            'monto_incorrecto': lambda estado: estado['monto'] != 22
        }

    def buscar_regla(self, estado):
        # Busca la regla adecuada basada en el estado
        if self.reglas['monto_correcto'](estado):
            return 'generar_boleta'
        elif self.reglas['monto_incorrecto'](estado):
            return 'rechazar_pago'

    def cobrar_matricula(self, estudiante):
        monto = 22  # Monto fijo de la matrícula
        estudiante.dinero -= monto
        percepcion = {'monto': monto}
        self.estado = self.modelo(self.estado, 'cobrar_matricula', percepcion)
        regla = self.buscar_regla(self.estado)
        if regla == 'generar_boleta':
            print("Generando boleta, por favor espere...")
            time.sleep(3)  # Simula un retraso de 3 segundos
            codigo_boleta = f"BOLETA-{random.randint(1000, 9999)}"
            self.boletas[estudiante.nombre] = codigo_boleta
            estudiante.boleta = codigo_boleta
            self.actualizar_estado(estudiante)
            print(f"Matricula cobrada a {estudiante.nombre}. Boleta: {codigo_boleta}")
        else:
            print("Error: El monto de la matrícula es incorrecto.")

    def entregar_boletas(self):
        return self.boletas