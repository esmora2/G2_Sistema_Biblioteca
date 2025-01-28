class Observador:
    def actualizar(self, mensaje):
        raise NotImplementedError


class UsuarioObservador(Observador):
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, mensaje):
        print(f"Notificación para {self.nombre}: {mensaje}")


class Notificador:
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def notificar(self, mensaje):
        for observador in self.observadores:
            observador.actualizar(mensaje)
