class Sala:

    def __init__(self, numero, capacidad):
        self.__numero = numero
        self.__capacidad = capacidad

    def mostrar_datos(self):
        print(f"Numero: {self.__numero} - Capacidad: {self.__capacidad}")

    def hay_disponibilidad(self, entradas_vendidas):
        if entradas_vendidas < self.__capacidad:
            return "hay disponibilidad"
        else:  #si sacamos el else es lo mismo
            return "no hay capacidad"
        