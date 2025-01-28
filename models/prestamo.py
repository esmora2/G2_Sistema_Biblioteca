class Prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro

    def __str__(self):
        return f"Préstamo: {self.libro.titulo} para {self.usuario.nombre}"
