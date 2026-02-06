# Integrantes:
# - Crespo John
# - Danna Rodriguez
# - Genesis Garboa
# -Alvarado Dayana
from ServicioUG import ServicioUniversitario

class CursoPresencial(ServicioUniversitario):
    """
       Curso presencial: puede tener costo adicional por materiales y
       una cuota por uso de instalaciones.
       """

    def __init__(self, codigo: str, nombre: str, duracion_horas: float,
                 costo_base: float, costo_materiales: float, cuota_infraestructura: float):
        super().__init__(codigo, nombre, duracion_horas, costo_base)
        self._costo_materiales = None
        self._cuota_infraestructura = None

        self.costo_materiales = costo_materiales
        self.cuota_infraestructura = cuota_infraestructura

    @property
    def costo_materiales(self) -> float:
        return self._costo_materiales

    @costo_materiales.setter
    def costo_materiales(self, value: float):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("costo_materiales debe ser >= 0.")
        self._costo_materiales = float(value)

    @property
    def cuota_infraestructura(self) -> float:
        return self._cuota_infraestructura

    @cuota_infraestructura.setter
    def cuota_infraestructura(self, value: float):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("cuota_infraestructura debe ser >= 0.")
        self._cuota_infraestructura = float(value)

    def calcular_costo(self) -> float:
        total = self.costo_base + self.costo_materiales + self.cuota_infraestructura
        return round(total, 2)

    def mostrar_info(self) -> str:
        return (f"Presencial | {self.codigo} - {self.nombre} | Costo total: ${self.calcular_costo():.2f}")