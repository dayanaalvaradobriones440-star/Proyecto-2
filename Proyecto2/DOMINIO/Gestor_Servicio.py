# Integrantes:
# - Crespo John
# - Danna Rodriguez
# - Genesis Garboa
# -Alvarado Dayana
from typing import List

from DOMINIO.ServicioUG import ServicioUniversitario


class GestorServicios:
    """
       Clase que contiene operaciones sobre listas de ServiciosUniversitarios.
       Aquí residirán los métodos polimórficos requeridos.
       """
    def __init__(self, servicios: List[ServicioUniversitario] = None):
        self.servicios = servicios if servicios else []

    def agregar_servicio(self, servicio: ServicioUniversitario):
        self.servicios.append(servicio)

    def sumar_costos(self) -> float:
        total = sum(s.calcular_costo() for s in self.servicios)
        return round(total, 2)

    def generar_reporte(self) -> str:
        return "\n".join(s.mostrar_info() for s in self.servicios)

    def filtrar_por_rango(self, minimo: float, maximo: float):
        return [s for s in self.servicios if minimo <= s.calcular_costo() <= maximo]