import re
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox

from DATOS.EstudianteDAO import EstudianteDAO
from DOMINIO.Estudiante_UG import Estudiante
from UI.vtnPrincipal import Ui_vtnPrincipal


class EstudianteServicio(QMainWindow):
    """
    Clase que maneja la lógica de la ventana principal para gestionar estudiantes.
    """

    def __init__(self):
        super().__init__()
        self.ui = Ui_vtnPrincipal()
        self.ui.setupUi(self)

        # Botones conectados a métodos
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.btnEliminar.clicked.connect(self.eliminar)
        self.ui.btnBuscar.clicked.connect(self.buscar)
        self.ui.btnActualizar.clicked.connect(self.actualizar)

        # Validadores para campos numéricos
        self.ui.txtBuscar_Cedula.setValidator(QIntValidator())
        self.ui.txtCedula.setValidator(QIntValidator())

    def guardar(self):
        nombre = self.ui.txtNombre.text()
        cedula = self.ui.txtCedula.text()
        apellido = self.ui.txtApellido.text()
        email = self.ui.txtCorreo.text()
        tipo_curso = self.ui.cbTipo_Curso.currentText()

        regex_email = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

        if nombre == "" or not nombre.replace(" ", "").isalpha():
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un Nombre válido")
        elif apellido == "" or not apellido.replace(" ", "").isalpha():
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un Apellido válido")
        elif cedula == "" or len(cedula) != 10:
            QMessageBox.warning(self, "Advertencia", "Debe ingresar una Cédula válida de 10 dígitos")
        elif tipo_curso in ["Seleccionar", "Selecionar"]:
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar un tipo de curso")
        elif email == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un correo electrónico")
        elif not re.match(regex_email, email.lower()):
            QMessageBox.warning(self, "Advertencia", "Formato de correo inválido (ejemplo@dominio.com)")
        elif not (email.lower().endswith("@ug.edu.ec") or email.lower().endswith(".com")):
            QMessageBox.warning(self, "Advertencia", "El correo debe terminar en @ug.edu.ec o en .com")
        else:
            estudiante = Estudiante(cedula=cedula, nombre=nombre, apellido=apellido,
                                    tipo_curso=tipo_curso, email=email)
            respuesta_dic = EstudianteDAO.insertar(estudiante)
            if respuesta_dic["ejecuto"]:
                print(estudiante)
                self.ui.statusbar.showMessage("Se guardó el estudiante", 1500)
                self.limpiar()
            else:
                QMessageBox.critical(self, "Error", "Error al guardar estudiante.")

    def buscar(self):
        cedula = self.ui.txtBuscar_Cedula.text().zfill(10)
        if len(cedula) != 10:
            QMessageBox.warning(self, "Advertencia", "Debe ingresar una Cédula válida de 10 dígitos")
        else:
            estudiante = EstudianteDAO.seleccionar(cedula)
            if estudiante:
                self.ui.txtNombre.setText(estudiante.nombre)
                self.ui.txtCedula.setText(estudiante.cedula)
                self.ui.txtApellido.setText(estudiante.apellido)
                self.ui.txtCorreo.setText(estudiante.email)
                self.ui.cbTipo_Curso.setCurrentText(estudiante.tipo_curso)
                print(estudiante)
            else:
                QMessageBox.warning(self, "Advertencia", "No existe estudiante registrado con esa cédula.")

    def limpiar(self):
        self.ui.txtNombre.clear()
        self.ui.txtCedula.clear()
        self.ui.txtApellido.clear()
        self.ui.txtCorreo.clear()
        self.ui.cbTipo_Curso.setCurrentText("Seleccionar")
        self.ui.txtBuscar_Cedula.clear()

    def eliminar(self):
        cedula = self.ui.txtCedula.text()
        if len(cedula) != 10:
            QMessageBox.warning(self, "Advertencia", "Debe ingresar una Cédula válida de 10 dígitos")
        else:
            if QMessageBox.question(self, "Confirmar", "¿Está seguro de eliminar?") == QMessageBox.Yes:
                respuesta_dic = EstudianteDAO.eliminar(cedula)
                if respuesta_dic["ejecuto"]:
                    self.ui.statusbar.showMessage("Estudiante eliminado", 1500)
                    self.limpiar()
                else:
                    QMessageBox.critical(self, "Error", "Error al eliminar estudiante")
            else:
                print("Acción cancelada")

    def actualizar(self):
        nombre = self.ui.txtNombre.text()
        cedula = self.ui.txtCedula.text()
        apellido = self.ui.txtApellido.text()
        email = self.ui.txtCorreo.text()
        tipo_curso = self.ui.cbTipo_Curso.currentText()

        regex_email = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

        if nombre == "" or not nombre.replace(" ", "").isalpha():
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un Nombre válido")
        elif apellido == "" or not apellido.replace(" ", "").isalpha():
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un Apellido válido")
        elif cedula == "" or len(cedula) != 10:
            QMessageBox.warning(self, "Advertencia", "Debe ingresar una Cédula válida de 10 dígitos")
        elif tipo_curso not in ["Presencial", "Virtual"]:
            QMessageBox.warning(self, "Advertencia", "Debe seleccionar un tipo de curso válido")

        elif email == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar un correo electrónico")
        elif not re.match(regex_email, email.lower()):
            QMessageBox.warning(self, "Advertencia", "Formato de correo inválido (ejemplo@dominio.com)")
        elif not (email.lower().endswith("@ug.edu.ec") or email.lower().endswith(".com")):
            QMessageBox.warning(self, "Advertencia", "El correo debe terminar en @ug.edu.ec o en .com")
        else:
            estudiante = Estudiante(cedula=cedula, nombre=nombre, apellido=apellido,
                                    tipo_curso=tipo_curso, email=email)
            respuesta_dic = EstudianteDAO.actualizar(estudiante)
            if respuesta_dic["ejecuto"]:
                print(estudiante)
                self.ui.statusbar.showMessage("Estudiante actualizado", 1500)
                self.limpiar()
            else:
                QMessageBox.critical(self, "Error", "Error al actualizar estudiante.")
