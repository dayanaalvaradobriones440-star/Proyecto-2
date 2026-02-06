class Estudiante:
    """
    Representa un estudiante/persona que puede inscribirse a cursos.
    """

    def __init__(self, cedula: str, nombre: str, apellido: str, tipo_curso: str, email: str):
        self._cedula = None
        self._nombre = None
        self._apellido = None
        self._tipo_curso = None
        self._email = None

        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.tipo_curso = tipo_curso
        self.email = email

    @property
    def cedula(self) -> str:
        return self._cedula

    @cedula.setter
    def cedula(self, value: str):
        if not isinstance(value, str) or len(value.strip()) != 10 or not value.isdigit():
            raise ValueError("La cédula debe ser un string de 10 dígitos.")
        self._cedula = value.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("El nombre debe ser un string no vacío.")
        self._nombre = value.strip()

    @property
    def apellido(self) -> str:
        return self._apellido

    @apellido.setter
    def apellido(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("El apellido debe ser un string no vacío.")
        self._apellido = value.strip()

    @property
    def tipo_curso(self) -> str:
        return self._tipo_curso

    @tipo_curso.setter
    def tipo_curso(self, value: str):
        if value == "Seleccionar":
            self._tipo_curso = None   # no asigna curso
        elif value not in ["Presencial", "Virtual"]:
            raise ValueError("El tipo de curso debe ser 'Presencial' o 'Virtual'.")
        else:
            self._tipo_curso = value

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("El correo no puede estar vacío.")
        correo = value.strip().lower()
        if not (correo.endswith("@ug.edu.ec") or correo.endswith(".com")):
            raise ValueError("El correo debe terminar en @ug.edu.ec o en .com.")
        self._email = correo

    def __str__(self) -> str:
        return f"{self.cedula} - {self.nombre} {self.apellido} | {self.tipo_curso} | {self.email}"
