class Persona:
    def __init__(self, nombre, apellido, fecha_nacimiento, telefono, direccion, sexo, email):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.direccion = direccion
        self.sexo = sexo
        self.email = email


    def get_Email(self):
        return self.email
    def set_Email(self, email):
        self.email=email
    def get_Nombre(self):
        return self.nombre

    def set_Nombre(self, nombre):
        self.nombre = nombre

    def get_Apellido(self):
        return self.apellido

    def set_Apellido(self, apellido):
        self.apellido = apellido

    def get_fechaNacimiento(self):
        return self.fecha_nacimiento

    def set_FechaNacimiento(self, fecha_nacimiento):
        self.fecha_nacimiento = fecha_nacimiento

    def get_Telefono(self):
        return self.telefono

    def set_Telefono(self, telefono):
        self.telefono = telefono

    def get_Direccion(self):
        return self.direccion

    def set_Direccion(self, direccion):
        self.direccion = direccion
    
    def get_Sexo(self):
        return self.sexo
    def set_Sexo(self, sexo):
        self.sexo = sexo

    
class Profesor(Persona):

    def __init__(self, id_profesor, nombre, apellido, fecha_nacimiento, telefono, direccion, sexo, email, academia):
        Persona.__init__(nombre, apellido, fecha_nacimiento,
                        telefono, direccion, sexo, email)
        self.id_profesor = id_profesor
        self.academia = academia

    def __str__(self):
        return "Profesor: "+ self.nombre + ", "+ self.apellido + " - Fecha de Nac: " + self.fecha_nacimiento + " - Telefono: " + self.telefono + " - Direccion: " + self.direccion + " - Email: " + self.email + " - Academia " + self.academia
    def get_Academia(self):
        return self.academia
    def set_Academia(self, academia):
        self.academia = academia

class Alumno(Persona):

    def __init__(self, id_alumno, nombre, apellido, fecha_nacimiento, telefono, direccion, sexo, email, danza):
        Persona.__init__( nombre, apellido, fecha_nacimiento,
                        telefono, direccion, sexo, email)
        self.id_alumno = id_alumno
        self.danza = danza

    def __str__(self):
        return "Alumno: "+ self.nombre + ", "+ self.apellido + " - Fecha de Nac: " + self.fecha_nacimiento + " - Telefono: " + self.telefono + " - Direccion: " + self.direccion + " - Email: " + self.email + " - Danza " + self.danza 
    def get_Danza(self):
        return self.danza

    def set_Danza(self, danza):
        self.danza = danza

    