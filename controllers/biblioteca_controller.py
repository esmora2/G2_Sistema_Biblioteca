from models.usuario import UsuarioFactory
from models.libro import Libro, LibroFisico, LibroDigital
from models.prestamo import Prestamo
from models.notificador import Notificador, UsuarioObservador
from views.interfaz import Interfaz

class BibliotecaController:
    def __init__(self):
        self.usuarios = []
        self.libros = []
        self.prestamos = []
        self.notificador = Notificador()

    def registrar_usuario(self, tipo, nombre, id_usuario):
        usuario = UsuarioFactory.crear_usuario(tipo, nombre, id_usuario)
        self.usuarios.append(usuario)
        self.notificador.agregar_observador(UsuarioObservador(nombre))
        Interfaz.mostrar_mensaje(f"Usuario registrado: {usuario}")

    def agregar_libro(self, titulo, autor, isbn, tipo):
        libro = LibroFisico(titulo, autor, isbn) if tipo.lower() == "fisico" else LibroDigital(titulo, autor, isbn)
        self.libros.append(libro)
        Interfaz.mostrar_mensaje(f"Libro agregado: {libro}")

    def realizar_prestamo(self, id_usuario, isbn):
        usuario = next((u for u in self.usuarios if u.id_usuario == id_usuario), None)
        libro = next((l for l in self.libros if l.isbn == isbn), None)

        if usuario and libro:
            prestamo = Prestamo(usuario, libro)
            self.prestamos.append(prestamo)
            self.notificador.notificar(f"El libro '{libro.titulo}' ha sido prestado.")
            Interfaz.mostrar_mensaje(f"Préstamo registrado: {prestamo}")
        else:
            Interfaz.mostrar_mensaje("Usuario o libro no encontrado.")
