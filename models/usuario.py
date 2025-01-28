class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario

    def __str__(self):
        return f"{self.__class__.__name__}: {self.nombre} (ID: {self.id_usuario})"


class Estudiante(Usuario):
    pass


class Docente(Usuario):
    pass


class Administrador(Usuario):
    pass


class UsuarioFactory:
    @staticmethod
    def crear_usuario(tipo, nombre, id_usuario):
        if tipo.lower() == "estudiante":
            return Estudiante(nombre, id_usuario)
        elif tipo.lower() == "docente":
            return Docente(nombre, id_usuario)
        elif tipo.lower() == "administrador":
            return Administrador(nombre, id_usuario)
        else:
            raise ValueError("Tipo de usuario no reconocido")
