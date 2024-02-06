import mysql.connector
class Conectar():
    def __init__(self) -> None:
        try:
            self.conexion = mysql.connector.connect(
                host = 'localhost',
                port = 3306,
                user = 'root',
                password = '',
                db = 'danza'

            )
        except mysql.connector.Error as descripcionError:
            print("¡No se conectó!",descripcionError)