from modelos.empleado import Empleado

class Desarrollador(Empleado):
    def __init__(self, nombre: str, id_empleado: str, salario_base: float, lenguaje: str):
        super().__init__(nombre, id_empleado, salario_base)
        self.lenguaje: str = lenguaje

    def calcular_pago(self) -> float:
        # POLIMORFISMO: Suma de float (número decimal) + int (número entero) resulta en float (número decimal)
        bono_tech: float = 400.0
        return self.obtener_salario_base() + bono_tech