class Academia:
    def __init__(self, id_academia, nombre_academia, direccion_academia, email_academia, telefono_academia, id_ciudad):
        self._id_academia = id_academia
        self._nombre_academia = nombre_academia
        self._direccion_academia = direccion_academia
        self._email_academia = email_academia
        self._telefono_academia = telefono_academia
        self._id_ciudad = id_ciudad

    @property
    def id_academia(self):
        return self._id_academia

    @property
    def nombre_academia(self):
        return self._nombre_academia

    @nombre_academia.setter
    def nombre_academia(self, value):
        self._nombre_academia = value

    @property
    def direccion_academia(self):
        return self._direccion_academia

    @direccion_academia.setter
    def direccion_academia(self, value):
        self._direccion_academia = value

    @property
    def email_academia(self):
        return self._email_academia

    @email_academia.setter
    def email_academia(self, value):
        self._email_academia = value

    @property
    def telefono_academia(self):
        return self._telefono_academia

    @telefono_academia.setter
    def telefono_academia(self, value):
        self._telefono_academia = value

    @property
    def id_ciudad(self):
        return self._id_ciudad

    @id_ciudad.setter
    def id_ciudad(self, value):
        self._id_ciudad = value

    def mostrar_academia(self):
        print(f"ID Academia: {self.id_academia}")
        print(f"Nombre: {self.nombre_academia}")
        print(f"Dirección: {self.direccion_academia}")
        print(f"Email: {self.email_academia}")
        print(f"Teléfono: {self.telefono_academia}")
        print(f"ID Ciudad: {self.id_ciudad}")

    def crear_academia():
        pass

    def mostrar_academia_por_id():
        pass

    def mostrar_academias():
        pass

    def actualizar_academia():
        pass

    def eliminar_academia():
        pass

    def buscar_academia_por_nombre():
        pass
