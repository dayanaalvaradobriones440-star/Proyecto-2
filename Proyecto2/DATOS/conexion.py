import sys
import pyodbc as bd
class Conexion:
    """
    Clase que permite abrir conexion a la BBDD y abrir cursor.
    """
    #_SERVIDOR = '192.168.110.137'
    #_SERVIDOR = '10.4.80.236'
    #_SERVIDOR = '10.4.48.239'
    #_SERVIDOR = '10.4.62.224'
    _SERVIDOR = '127.0.0.1'
    _BBDD = 'SAP'
    _USUARIO = 'admin_day'
    _PASSWORD = '1234'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        """
        Obtiene la conexion a la BBDD con los parametros de conexion pasados como constantes
        :return:
        """
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                           cls._SERVIDOR + ';DATABASE=' + cls._BBDD + ';UID=' + cls._USUARIO + ';PWD=' + cls._PASSWORD
                                           + ';TrustServerCertificate=yes')
                # log.debug(f'Conexión exitosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                # log.error(f'Ocurrió una excepción al obtener la conexión: {e}')
                print(e)
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        """
        Obtiene el cursor que
        :return:
        """
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                # log.debug(f'Se abrió correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                # log.error(f'Ocurrió una excepción al obtener el cursor: {e}')
                print(e)
                sys.exit()
        else:
            return cls._cursor


if __name__ == '__main__':
    print(Conexion.obtenerConexion())
    print(Conexion.obtenerCursor())