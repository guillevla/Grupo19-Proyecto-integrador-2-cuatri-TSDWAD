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

#Crear danza - INSERT
    def registrarDanza(self, id_danza, nombre, tipo_danza, sub_tipo_danza):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor() #Crea un objeto de cursor, que se utiliza para ejecutar comandos SQL en la base de datos.
                sentenciaSQL= "INSERT INTO Danza (id_danza, nombre, tipo_danza, sub_tipo_danza) VALUES(%s,%s,%s,%s)" #Define una sentencia SQL de inserción que utiliza marcadores de posición %s para evitar posibles ataques de inyección de SQL.
                data= (id_danza, nombre, tipo_danza, sub_tipo_danza) # Crea una tupla llamada data con los valores que se insertarán en la tabla.
                cursor.execute(sentenciaSQL,data) #Ejecuta la sentencia SQL con los datos proporcionados
                self.conexion.commit()
            except Exception as e:
                print("No se pudo registrar Danza")
            finally:
                if self.conexion.is_connected():
                    cursor.close()
                    self.conexion.close()   

#Consultar danza - SELECT
    def consultarDanza(self, id_danza):
            if self.conexion.is_connected():
                try:
                    cursor = self.conexion.cursor()
                    sentenciaSQL= "SELECT * from Danza where id_danza="+id_danza
                    cursor.execute(sentenciaSQL)
                    listadoDanza = cursor.fetchall()
                    return listadoDanza
                except:
                    print("No se pudo consultar a la base de datos")
                finally:
                    if self.conexion.is_connected():
                        cursor.close()
                        self.conexion.close() 

#Modificar danza - UPDATE
def modificarDanza(self, id_danza, nombre, tipo_danza, sub_tipo_danza):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL= "UPDATE Danza SET nombre="+nombre+", tipo_danza="+tipo_danza+", sub_tipo_danza="+sub_tipo_danza+" WHERE id_profesor="+id_danza
                cursor.execute(sentenciaSQL)
                self.conexion.commit()
            except:
                print("No se pudo modificar los datos de la danza") 
            finally:
                    if self.conexion.is_connected():
                        cursor.close()
                        self.conexion.close() 

#EliminarDanza- DELETE
def eliminarDanza(self,id_danza):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE from Danza where id_danza="+id_danza
                cursor.execute(sentenciaSQL)
                self.conexion.commit()                
            except:
                print("No se pudo eliminar Danza")
            finally:
                    if self.conexion.is_connected():
                        cursor.close()
                        self.conexion.close() 