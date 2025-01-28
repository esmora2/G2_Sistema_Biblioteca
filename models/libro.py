class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn})"


class LibroFisico(Libro):
    pass


class LibroDigital(Libro):
    pass
