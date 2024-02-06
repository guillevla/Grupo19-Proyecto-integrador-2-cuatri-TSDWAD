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

#Crear academia - INSERT
    def registrar(self, id_academia, nombre, direccion, email, telefono):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor() #Crea un objeto de cursor, que se utiliza para ejecutar comandos SQL en la base de datos.
                sentenciaSQL= "INSERT INTO Academia (id_academia, nombre, direccion, email, telefono) VALUES(%s,%s,%s,%s,%s)" #Define una sentencia SQL de inserción que utiliza marcadores de posición %s para evitar posibles ataques de inyección de SQL.
                data= (id_academia, nombre, direccion, email, telefono) # Crea una tupla llamada data con los valores que se insertarán en la tabla.
                cursor.execute(sentenciaSQL,data) #Ejecuta la sentencia SQL con los datos proporcionados
                self.conexion.commit()
            except Exception as e:
                print("No se pudo registrar la Academia")
            finally:
                if self.conexion.is_connected():
                    cursor.close()
                    self.conexion.close()   

#Consultar Academia - SELECT
    def consultarAcademia(self, id_academia):
            if self.conexion.is_connected():
                try:
                    cursor = self.conexion.cursor()
                    sentenciaSQL= "SELECT * from Academia where id_academia="+id_academia
                    cursor.execute(sentenciaSQL)
                    listadoAcademia = cursor.fetchall()
                    return listadoAcademia
                except:
                    print("No se pudo consultar a la base de datos")
                finally:
                    if self.conexion.is_connected():
                        cursor.close()
                        self.conexion.close() 

#Modificar Academia - UPDATE
def modificarAcademia(self, id_academia, nombre, direccion, email, telefono):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL= "UPDATE Academia SET nombre="+nombre+", direccion="+direccion+", email="+email+", telefono="+telefono+" WHERE id_academia="+id_academia
                cursor.execute(sentenciaSQL)
                self.conexion.commit()
            except:
                print("No se pudo modificar los datos de la Academia") 
            finally:
                    if self.conexion.is_connected():
                        cursor.close()
                        self.conexion.close() 

#Eliminar Academia- DELETE
def eliminarAcademia(self,id_academia):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE from Academia where id_academia="+id_academia
                cursor.execute(sentenciaSQL)
                self.conexion.commit()                
            except:
                print("No se pudo eliminar la Academia")
            finally:
                    if self.conexion.is_connected():
                        cursor.close()
                        self.conexion.close() 