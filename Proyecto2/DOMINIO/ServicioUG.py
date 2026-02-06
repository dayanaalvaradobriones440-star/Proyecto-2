# Integrantes:
# - Crespo John
# - Danna Rodriguez
# - Genesis Garboa
# -Alvarado Dayana
from abc import ABC, abstractmethod

class ServicioUniversitario(ABC):
    """
      Superclase base para los servicios relacionados con la universidad/cursos.
      Todos los atributos son privados y se accede mediante properties.
      """

    def __init__(self, codigo: str, nombre: str, duracion_horas: float, costo_base: float):
        self._codigo = None
        self._nombre = None
        self._duracion_horas = None
        self._costo_base = None

        self.codigo = codigo
        self.nombre = nombre
        self.duracion_horas = duracion_horas
        self.costo_base = costo_base

    @property
    def codigo(self) -> str:
        return self._codigo

    @codigo.setter
    def codigo(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("codigo debe ser un string no vacío.")
        self._codigo = value.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("nombre debe ser un string no vacío.")
        self._nombre = value.strip()

    @property
    def duracion_horas(self) -> float:
        return self._duracion_horas

    @duracion_horas.setter
    def duracion_horas(self, value: float):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("duracion_horas debe ser un número positivo.")
        self._duracion_horas = float(value)

    @property
    def costo_base(self) -> float:
        return self._costo_base

    @costo_base.setter
    def costo_base(self, value: float):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("costo_base debe ser un número >= 0.")
        self._costo_base = float(value)

    @abstractmethod
    def calcular_costo(self) -> float:
        pass

    @abstractmethod
    def mostrar_info(self) -> str:
        pass

    def __str__(self) -> str:
        return f"{self.codigo} - {self.nombre} ({self.duracion_horas}h) - Base: ${self.costo_base:.2f}"