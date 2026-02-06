import sys

from PySide6.QtWidgets import QApplication

from SERVICIOS.estudiante_servicio import EstudianteServicio

app = QApplication()
vtn_principal = EstudianteServicio()
vtn_principal.show()
sys.exit(app.exec())
