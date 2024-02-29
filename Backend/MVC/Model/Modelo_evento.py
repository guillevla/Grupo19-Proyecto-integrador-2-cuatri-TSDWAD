class Evento:
    def __init__(self, id_evento, nombre_evento, fecha_evento, id_sede):
        self._id_evento = id_evento
        self._nombre_evento = nombre_evento
        self._fecha_evento = fecha_evento
        self._id_sede = id_sede

    @property
    def id_evento(self):
        return self._id_evento

    @property
    def nombre_evento(self):
        return self._nombre_evento

    @nombre_evento.setter
    def nombre_evento(self, value):
        self._nombre_evento = value

    @property
    def fecha_evento(self):
        return self._fecha_evento

    @fecha_evento.setter
    def fecha_evento(self, value):
        self._fecha_evento = value

    @property
    def id_sede(self):
        return self._id_sede

    @id_sede.setter
    def id_sede(self, value):
        self._id_sede = value

    def mostrar_evento(self):
        print(f"ID Evento: {self.id_evento}")
        print(f"Nombre Evento: {self.nombre_evento}")
        print(f"Fecha Evento: {self.fecha_evento}")
        print(f"ID Sede: {self.id_sede}")

    def crear_evento():
        pass

    def mostrar_evento_por_id():
        pass

    def mostrar_eventos():
        pass

    def actualizar_evento():
        pass

    def eliminar_evento():
        pass

    def buscar_evento_por_nombre():
        pass
