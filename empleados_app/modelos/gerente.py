from modelos.empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre: str, id_empleado: str, salario_base: float, departamento: str):
        super().__init__(nombre, id_empleado, salario_base)
        self.departamento: str = departamento

    def calcular_pago(self) -> float:
        # POLIMORFISMO: tiene un bono del 20%
        return self.obtener_salario_base() * 1.20