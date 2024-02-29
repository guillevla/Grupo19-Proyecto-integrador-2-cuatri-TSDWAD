from Model.claseusuario import *
from  Model.Modelo_profesor import *

#Crear profesor 
def crearUsuarioProfesor(self, id_profesor, nombre, apellido, fecha_nacimiento, telefono, direccion, sexo, email, id_academia, password):
    nuevoProfesor= Profesor(self, id_profesor, nombre, apellido, fecha_nacimiento, telefono, direccion, sexo, email, id_academia, password)
    conexion=Conectar
    conexion.registrarProfesor(Profesor)   

 # modificarProfesor()
def modificarUsuarioProfesor(self, profesor: Profesor):
    conexion = Conectar()
    conexion.modificarProfesor(profesor.get_idprofesor, profesor.get_nombre, profesor.get_apellido, profesor.get_fechanacimiento, profesor.get_telefono, profesor.get_direccion, profesor.get_sexo, profesor.get_email, profesor.get_idacademia, profesor.get_password)                             

# buscarprofesor()
def buscarProfesor(self, id_profesor):
    conexion=Conectar()
    profesor:profesor=conexion.consultarProfesor(id_profesor)
    if(profesor):
        print("Profesor/a encontrado: " + profesor.__str__)
        return profesor
    else:
        print("No existe un Profesor/a registrado")
    

def existeProfesor(self, id_profesor):
    conexion=Conectar()
    profesor=conexion.consultarProfesor(id_profesor)
    if(profesor):
        return True
    else:
        return False

#eliminarProfesor
def eliminarProfesor(self, id_profesor):
    conexion=Conectar()
    conexion.eliminarProfesor(id_profesor)
