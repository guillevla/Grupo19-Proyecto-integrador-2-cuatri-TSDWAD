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

#Crear alumno - INSERT
    def registrarAlumno(self, id_alumno, nombre, apellido, fecha_nacimiento, telefono, direccion, sexo, email, danza):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor() #Crea un objeto de cursor, que se utiliza para ejecutar comandos SQL en la base de datos.
                sentenciaSQL= "INSERT INTO Alumno (id_alumno, nombre, apellido, fecha_nacimiento, telefono, direccion, sexo, email, danza) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)" #Define una sentencia SQL de inserción que utiliza marcadores de posición %s para evitar posibles ataques de inyección de SQL.
                data= (id_alumno, nombre, apellido, fecha_nacimiento, telefono, direccion, sexo, email, danza) # Crea una tupla llamada data con los valores que se insertarán en la tabla.
                cursor.execute(sentenciaSQL,data) #Ejecuta la sentencia SQL con los datos proporcionados
                self.conexion.commit()
            except Exception as e:
                print("No se pudo registrar Alumno/a")
            finally:
                if self.conexion.is_connected():
                    cursor.close()
                    self.conexion.close()   

#Consultar Alumno - SELECT
    def consultarAlumno(self, id_alumno):
            if self.conexion.is_connected():
                try:
                    cursor = self.conexion.cursor()
                    sentenciaSQL= "SELECT * from Profesor where id_alumno="+id_alumno
                    cursor.execute(sentenciaSQL)
                    listadoAlumno = cursor.fetchall()
                    return listadoAlumno
                except:
                    print("No se pudo consultar a la base de datos")
                finally:
                    if self.conexion.is_connected():
                        cursor.close()
                        self.conexion.close() 

#Modificar alumno - UPDATE
def modificarAlumno(self, id_alumno, nombre, apellido, fecha_nacimiento, telefono, direccion, sexo, email, danza):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL= "UPDATE Alumno SET nombre="+nombre+", apellido="+apellido+", fecha_nacimiento="+fecha_nacimiento+", telefono="+telefono+" direccion="+direccion+", sexo="+sexo+", email="+email+", danza="+danza+" WHERE id_profesor="+id_alumno
                cursor.execute(sentenciaSQL)
                self.conexion.commit()
            except:
                print("No se pudo modificar los datos del Alumno/a") 
            finally:
                    if self.conexion.is_connected():
                        cursor.close()
                        self.conexion.close() 

#Eliminar Alumno- DELETE
def eliminarAlumno(self,id_alumno):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sentenciaSQL = "DELETE from Profesor where id_alumno="+id_alumno
                cursor.execute(sentenciaSQL)
                self.conexion.commit()                
            except:
                print("No se pudo eliminar Alumno/a")
            finally:
                    if self.conexion.is_connected():
                        cursor.close()
                        self.conexion.close() 