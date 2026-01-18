from typing import List
from modelos.empleado import Empleado

class Sistemarrhh:
    def __init__(self):
        # Indicamos que la lista almacenará objetos tipo Empleado o sus hijos
        self.empleados: List[Empleado] = []

    def agregar_empleado(self, empleado: Empleado) -> None:
        self.empleados.append(empleado)
        print(f"Registro exitoso: {empleado.nombre}")

    def generar_reporte_pagos(self) -> None:
        print("\n--- REPORTE DE PAGOS ---")
        for emp in self.empleados:
            pago: float = emp.calcular_pago()
            print(f"{emp} -> Pago: ${pago:.2f}")