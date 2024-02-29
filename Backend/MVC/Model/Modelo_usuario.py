class Usuario:
    def __init__(self, id_usuario, nombre_usuario, apellido_usuario, email_usuario):
        self._id_usuario = id_usuario
        self._nombre_usuario = nombre_usuario
        self._apellido_usuario = apellido_usuario
        self._email_usuario = email_usuario

    @property
    def id_usuario(self):
        return self._id_usuario

    @property
    def nombre_usuario(self):
        return self._nombre_usuario

    @nombre_usuario.setter
    def nombre_usuario(self, value):
        self._nombre_usuario = value

    @property
    def apellido_usuario(self):
        return self._apellido_usuario

    @apellido_usuario.setter
    def apellido_usuario(self, value):
        self._apellido_usuario = value

    @property
    def email_usuario(self):
        return self._email_usuario

    @email_usuario.setter
    def email_usuario(self, value):
        self._email_usuario = value

    def mostrar_usuario(self):
        print(f"ID Usuario: {self.id_usuario}")
        print(f"Nombre: {self.nombre_usuario} {self.apellido_usuario}")
        print(f"Email: {self.email_usuario}")

    def crear_usuario():
        pass

    def mostrar_usuario_por_id():
        pass

    def mostrar_usuarios():
        pass

    def actualizar_usuario():
        pass

    def eliminar_usuario():
        pass

    def buscar_usuario_por_nombre():
        pass
