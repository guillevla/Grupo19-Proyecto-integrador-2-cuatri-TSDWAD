class Ciudad:
    def __init__(self, id_ciudad, nombre_ciudad):
        self._id_ciudad = id_ciudad
        self._nombre_ciudad = nombre_ciudad

    @property
    def id_ciudad(self):
        return self._id_ciudad

    @property
    def nombre_ciudad(self):
        return self._nombre_ciudad

    @nombre_ciudad.setter
    def nombre_ciudad(self, value):
        self._nombre_ciudad = value

    def mostrar_ciudad(self):
        print(f"ID Ciudad: {self.id_ciudad}")
        print(f"Nombre Ciudad: {self.nombre_ciudad}")

    def crear_ciudad():
        pass

    def mostrar_ciudad_por_id():
        pass

    def mostrar_ciudades():
        pass

    def actualizar_ciudad():
        pass

    def eliminar_ciudad():
        pass

    def buscar_ciudad_por_nombre():
        pass
