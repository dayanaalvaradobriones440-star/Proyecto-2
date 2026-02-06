# Integrantes:
# - Crespo John
# - Danna Rodriguez
# - Genesis Garboa
# -Alvarado Dayana
from ServicioUG import ServicioUniversitario


class CursoVirtual(ServicioUniversitario):
    """
        Curso virtual: puede tener un descuento por modalidad y/o
        una tarifa por plataforma (hosting/licencias).
        """

    def __init__(self, codigo: str, nombre: str, duracion_horas: float,
                 costo_base: float, tarifa_plataforma: float, descuento_percent: float = 0.0):
        super().__init__(codigo, nombre, duracion_horas, costo_base)
        self._tarifa_plataforma = None
        self._descuento_percent = None

        self.tarifa_plataforma = tarifa_plataforma
        self.descuento_percent = descuento_percent

    @property
    def tarifa_plataforma(self) -> float:
        return self._tarifa_plataforma

    @tarifa_plataforma.setter
    def tarifa_plataforma(self, value: float):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("tarifa_plataforma debe ser >= 0.")
        self._tarifa_plataforma = float(value)

    @property
    def descuento_percent(self) -> float:
        return self._descuento_percent

    @descuento_percent.setter
    def descuento_percent(self, value: float):
        if not isinstance(value, (int, float)) or not (0 <= value <= 100):
            raise ValueError("descuento_percent debe estar entre 0 y 100.")
        self._descuento_percent = float(value)

    def calcular_costo(self) -> float:
        subtotal = self.costo_base + self.tarifa_plataforma
        descuento = subtotal * (self.descuento_percent / 100.0)
        total = subtotal - descuento
        return round(total, 2)

    def mostrar_info(self) -> str:
        return (f"Virtual | {self.codigo} - {self.nombre} | Costo: ${self.calcular_costo():.2f}")