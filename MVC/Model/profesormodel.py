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

#Crear profesor - INSERT
    def registrar(self, id_profesor, nombre, apellido, fecha_nacimiento, telefono, direccion, sexo, email, academia):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor() #Crea un objeto de cursor, que se utiliza para ejecutar comandos SQL en la base de datos.
                sentenciaSQL= "INSERT INTO Profesor (id_profesor, nombre, apellido, fecha_nacimiento, telefono, direccion, sexo, email, academia) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)" #Define una sentencia SQL de inserción que utiliza marcadores de posición %s para evitar posibles ataques de inyección de SQL.
                data= (id_profesor, nombre, apellido, fecha_nacimiento, telefono, direccion, sexo, email, academia) # Crea una tupla llamada data con los valores que se insertarán en la tabla.
                cursor.execute(sentenciaSQL,data) #Ejecuta la sentencia SQL con los datos proporcionados
                self.conexion.commit()
            except Exception as e:
                print("No se pudo registrar Profesor/a")
            finally:
                if self.conexion.is_connected():
                    cursor.close()
                    self.conexion.close()   

#Consultar Profesor - SELECT
    def consultarProfesor(self, id_profesor):
            if self.conexion.is_connected():
                try:
                    cursor = self.conexion.cursor()
                    sentenciaSQL= "SELECT * from Profesor where id_profesor="+id_profesor
                    cursor.execute(sentenciaSQL)
                    listadoProfesor = cursor.fetchall()
                    return listadoProfesor
                except:
                    print("No se pudo consultar a la base de datos")
                finally:
                    if self.conexion.is_connected():
                        cursor.close()
                        self.conexion.close() 

#Modificar Academia - UPDATE
def modificarAcademia(self, id_profesor, nombre, apellido, fecha_nacimiento, telefono, direccion, sexo, email, academia):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL= "UPDATE Profesor SET nombre="+nombre+", apellido="+apellido+", fecha_nacimiento="+fecha_nacimiento+", telefono="+telefono+" direccion="+direccion+", sexo="+sexo+", email="+email+", academia="+academia+" WHERE id_profesor="+id_profesor
                cursor.execute(sentenciaSQL)
                self.conexion.commit()
            except:
                print("No se pudo modificar los datos del Profesor/a") 
            finally:
                    if self.conexion.is_connected():
                        cursor.close()
                        self.conexion.close() 

#Eliminar Profesor- DELETE
def eliminarAcademia(self,id_profesor):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE from Profesor where id_profesor="+id_profesor
                cursor.execute(sentenciaSQL)
                self.conexion.commit()                
            except:
                print("No se pudo eliminar Profesor/a")
            finally:
                    if self.conexion.is_connected():
                        cursor.close()
                        self.conexion.close() 