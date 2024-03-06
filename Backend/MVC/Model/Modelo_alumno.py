class Alumno:
    def __init__(self, id_alumno, nombre_alumno, apellido_alumno, direccion_alumno, email_alumno, telefono_alumno, id_academia2, id_ciudad):
        self._id_alumno = id_alumno
        self._nombre_alumno = nombre_alumno
        self._apellido_alumno = apellido_alumno
        self._direccion_alumno = direccion_alumno
        self._email_alumno = email_alumno
        self._telefono_alumno = telefono_alumno
        self._id_academia2 = id_academia2
        self._id_ciudad = id_ciudad

    @property
    def id_alumno(self):
        return self._id_alumno

    @property
    def nombre_alumno(self):
        return self._nombre_alumno

    @nombre_alumno.setter
    def nombre_alumno(self, value):
        self._nombre_alumno = value

    @property
    def apellido_alumno(self):
        return self._apellido_alumno

    @apellido_alumno.setter
    def apellido_alumno(self, value):
        self._apellido_alumno = value

    @property
    def direccion_alumno(self):
        return self._direccion_alumno

    @direccion_alumno.setter
    def direccion_alumno(self, value):
        self._direccion_alumno = value

    @property
    def email_alumno(self):
        return self._email_alumno

    @email_alumno.setter
    def email_alumno(self, value):
        self._email_alumno = value

    @property
    def telefono_alumno(self):
        return self._telefono_alumno

    @telefono_alumno.setter
    def telefono_alumno(self, value):
        self._telefono_alumno = value

    @property
    def id_academia2(self):
        return self._id_academia2

    @id_academia2.setter
    def id_academia2(self, value):
        self._id_academia2 = value

    @property
    def id_ciudad(self):
        return self._id_ciudad

    @id_ciudad.setter
    def id_ciudad(self, value):
        self._id_ciudad = value

    def mostrar_alumno(self):
        print(f"ID Alumno: {self.id_alumno}")
        print(f"Nombre: {self.nombre_alumno} {self.apellido_alumno}")
        print(f"Dirección: {self.direccion_alumno}")
        print(f"Email: {self.email_alumno}")
        print(f"Teléfono: {self.telefono_alumno}")
        print(f"ID Academia: {self.id_academia2}")
        print(f"ID Ciudad: {self.id_ciudad}")


    def crear_alumno():
        pass

    def mostrar_alumno_por_id():
        pass

    def mostrar_alumnos():
        pass

    def actualizar_alumno():
        pass

    def eliminar_alumno():
        pass

    def buscar_alumno_por_nombre():
        pass