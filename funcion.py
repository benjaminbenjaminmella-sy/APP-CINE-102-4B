class Funcion:

    def __init__(self, fecha, hora, precio):
        self.__fecha = fecha
        self.__hora = hora
        self.__precio = precio

    def mostrar_datos(self):
        print(f"Fecha: {self.__fecha} - Hora: {self.__hora} - Precio: {self.__precio}")

    def es_funcion_nocturna(self):
        hora = int(self.__hora.split(":")[0])
        return hora >= 20
    