class Empleado:
    def __init__(self, nombre: str, id_empleado: str, salario_base: float):
        self.nombre: str = nombre
        self.id_empleado: str = id_empleado
        # ENCAPSULACIÓN: Atributo privado
        self.__salario_base: float = salario_base

    def obtener_salario_base(self) -> float:
        """Retorna un valor flotante"""
        return self.__salario_base

    def calcular_pago(self) -> float:
        """Método base para POLIMORFISMO"""
        return self.__salario_base

    def __str__(self) -> str:
        return f"ID: {self.id_empleado} | Nombre: {self.nombre}"
