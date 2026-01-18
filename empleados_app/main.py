from modelos.empleado import Empleado
from modelos.desarrollador import Desarrollador
from modelos.gerente import Gerente
# Importación corregida: carpeta.nombre_archivo
from servicios.sistema_rrhh import Sistemarrhh

def inicio() -> None:
    # Creamos la instancia
    sistema: Sistemarrhh = Sistemarrhh()

    # Creación de objetos con los datos de tus imágenes
    dev: Empleado = Desarrollador("Carlos Avila", "D-505", 2500.0, "Python")
    boss: Empleado = Gerente("LASCANO SANCHEZ", "G-101", 4000.0, "IT")

    # Registro y reporte
    sistema.agregar_empleado(dev)
    sistema.agregar_empleado(boss)
    sistema.generar_reporte_pagos()

if __name__ == "__main__":
    inicio()
