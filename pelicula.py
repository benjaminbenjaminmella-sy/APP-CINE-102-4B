class Pelicula:

    def __init__(self, titulo, genero, duracion):
        self.__titulo = titulo
        self.__genero = genero
        self.__duracion = duracion

    def mostrar_datos(self):
        return f"Peliculas: {self.__titulo} - Genero: {self.__genero} - Duracion: {self.__duracion}"
    