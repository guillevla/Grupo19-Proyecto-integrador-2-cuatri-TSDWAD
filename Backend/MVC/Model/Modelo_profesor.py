class Profesor:
    def __init__(self, id_profesor, nombre_profesor, apellido_profesor, telefono_profesor, id_academia1):
        self._id_profesor = id_profesor
        self._nombre_profesor = nombre_profesor
        self._apellido_profesor = apellido_profesor
        self._telefono_profesor = telefono_profesor
        self._id_academia1 = id_academia1

    @property
    def id_profesor(self):
        return self._id_profesor

    @property
    def nombre_profesor(self):
        return self._nombre_profesor

    @nombre_profesor.setter
    def nombre_profesor(self, value):
        self._nombre_profesor = value

    @property
    def apellido_profesor(self):
        return self._apellido_profesor

    @apellido_profesor.setter
    def apellido_profesor(self, value):
        self._apellido_profesor = value

    @property
    def telefono_profesor(self):
        return self._telefono_profesor

    @telefono_profesor.setter
    def telefono_profesor(self, value):
        self._telefono_profesor = value

    @property
    def id_academia1(self):
        return self._id_academia1

    @id_academia1.setter
    def id_academia1(self, value):
        self._id_academia1 = value

    def mostrar_profesor(self):
        print(f"ID Profesor: {self.id_profesor}")
        print(f"Nombre: {self.nombre_profesor} {self.apellido_profesor}")
        print(f"Teléfono: {self.telefono_profesor}")
        print(f"ID Academia: {self.id_academia1}")


    def crear_profesor():
        pass

    def mostrar_profesor_por_id():
        pass

    def mostrar_profesores():
        pass

    def actualizar_profesor():
        pass

    def eliminar_profesor():
        pass

    def buscar_profesor_por_nombre():
        pass
