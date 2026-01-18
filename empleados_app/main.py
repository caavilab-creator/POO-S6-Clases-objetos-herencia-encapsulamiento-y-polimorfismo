from modelos.empleado import Empleado
from modelos.desarrollador import Desarrollador
from modelos.gerente import Gerente
from servicios.sistema_gestion import SistemaGestion

def inicio() -> None:
    sistema: SistemaGestion = SistemaGestion()

    # Creación de objetos con sus tipos correspondientes
    dev: Empleado = Desarrollador("Carlos Avila", "D-505", 2500.0, "Python")
    boss: Empleado = Gerente("LASCANO SANCHEZ", "G-101", 4000.0, "IT")

    sistema.agregar_empleado(dev)
    sistema.agregar_empleado(boss)
    sistema.generar_reporte_pagos()

if __name__ == "__main__":
    inicio()