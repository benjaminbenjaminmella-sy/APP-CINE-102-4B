from pelicula import Pelicula
from funcion import Funcion
from sala import Sala
from cliente_premium import ClientePremium

def main():
    pass

pelicula1 = Pelicula("La sociedad de los poetas muertos", "drama", 150)

print(pelicula1.mostrar_datos())

funcion1 = Funcion("03-09-2026", "21:00", 8.500)

funcion1.mostrar_datos()

print(funcion1.es_funcion_nocturna())

sala1 = Sala(7, 10)

sala1.mostrar_datos()

print(sala1.hay_disponibilidad(95))

cliente_pro = ClientePremium("Eric", "e@gmail.com", 39, 20, 2000)

print(cliente_pro.calcular_precio(7000))


if __name__ == "__main__":
    main()