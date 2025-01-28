from controllers.biblioteca_controller import BibliotecaController

def main():
    biblioteca = BibliotecaController()

    biblioteca.registrar_usuario("estudiante", "Juan Pérez", "U001")
    biblioteca.registrar_usuario("docente", "María López", "D001")
    biblioteca.agregar_libro("1984", "George Orwell", "123456789", "fisico")
    biblioteca.realizar_prestamo("U001", "123456789")

if __name__ == "__main__":
    main()
