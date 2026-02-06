import pyodbc

from DATOS.conexion import Conexion
from DOMINIO.Estudiante_UG import Estudiante


class EstudianteDAO:
    _INSERT = ("INSERT INTO Estudiantes (nombres, apellidos, cedula, tipo_curso, email) "
               "VALUES (?, ?, ?, ?, ?)")

    _SELECT = ("SELECT idEstudiante, nombres, apellidos, cedula, tipo_curso, email "
               "FROM Estudiantes WHERE cedula = ?")

    _UPDATE = ("UPDATE Estudiantes SET nombres = ?, apellidos = ?, tipo_curso = ?, email = ? "
               "WHERE cedula = ?")

    _DELETE = ("DELETE FROM Estudiantes WHERE cedula = ?")

    @classmethod
    def insertar(cls, estudiante: Estudiante):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (estudiante.nombre, estudiante.apellido, estudiante.cedula,
                         estudiante.tipo_curso, estudiante.email)
                cursor.execute(cls._INSERT, datos)
                Conexion.obtenerConexion().commit()
                if cursor.rowcount == 1:
                    return {"ejecuto": True, "mensaje": "Estudiante guardado con éxito"}
                return {"ejecuto": False, "mensaje": "No se insertó ningún registro"}
        except Exception as e:
            print("Error en inserción:", e)
            return {"ejecuto": False, "mensaje": f"Error al guardar estudiante: {e}"}

    @classmethod
    def seleccionar(cls, cedula: str):
        try:
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECT, (cedula,))
                registro = cursor.fetchone()
                if registro:
                    return Estudiante(
                        cedula=registro[3],
                        nombre=registro[1],
                        apellido=registro[2],
                        tipo_curso=registro[4],
                        email=registro[5] if registro[5] else ""
                    )
                return None
        except Exception as e:
            print("Error en selección:", e)
            return None

    @classmethod
    def actualizar(cls, estudiante: Estudiante):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (estudiante.nombre, estudiante.apellido,
                         estudiante.tipo_curso, estudiante.email, estudiante.cedula)
                cursor.execute(cls._UPDATE, datos)
                Conexion.obtenerConexion().commit()
                if cursor.rowcount == 1:
                    return {"ejecuto": True, "mensaje": "Estudiante actualizado con éxito"}
                return {"ejecuto": False, "mensaje": "No se actualizó ningún registro"}
        except Exception as e:
            print("Error en actualización:", e)
            return {"ejecuto": False, "mensaje": f"Error al actualizar estudiante: {e}"}

    @classmethod
    def eliminar(cls, cedula: str):
        try:
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._DELETE, (cedula,))
                Conexion.obtenerConexion().commit()
                if cursor.rowcount == 1:
                    return {"ejecuto": True, "mensaje": "Estudiante eliminado con éxito"}
                return {"ejecuto": False, "mensaje": "No se eliminó ningún registro"}
        except Exception as e:
            print("Error en eliminación:", e)
            return {"ejecuto": False, "mensaje": f"Error al eliminar estudiante: {e}"}
