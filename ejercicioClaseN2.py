class Producto:
    def __init__(self, tipo, precio, genero):
        self.tipo = tipo
        self.precio = precio
        self.genero = genero

    def mostrarProducto(self):
        pass

class Pelicula(Producto):
    def __init__(self, tipo, precio, genero, trama, actores):
        super().__init__(tipo, precio, genero)
        self.trama = trama
        self.actores = actores

    def mostrarProducto(self):
        print(f'Tipo: {self.tipo}')
        print(f'Precio: {self.precio}')
        print(f'Genero: {self.genero}')
        print(f'Trama: {self.trama}')
        print(f'Actores: {self.actores}')

class Libro(Producto):
    def __init__(self, tipo, precio, genero, cantidad, autor):
        super().__init__(tipo, precio, genero)
        self.cantidad = cantidad
        self.autor = autor

    def mostrarProducto(self):
        print(f'Tipo: {self.tipo}')
        print(f'Precio: {self.precio}')
        print(f'Genero: {self.genero}')
        print(f'Cantidad: {self.cantidad}')
        print(f'Autor: {self.autor}')

class Disco(Producto):
    def __init__(self, tipo, precio, genero, cant_canciones, compositor):
        super().__init__(tipo, precio, genero)
        self.cant_canciones = cant_canciones
        self.compositor = compositor

    def mostrarProducto(self):
        print(f'Tipo: {self.tipo}')
        print(f'Precio: {self.precio}')
        print(f'Genero: {self.genero}')
        print(f'Cantidad de canciones: {self.cant_canciones}')
        print(f'Compositor: {self.compositor}')


pelicula1 = Pelicula("Película", 1500, "", "Comedia", "Eddie Murphi")
pelicula2 = Pelicula("Película", 2000, "", "Acción", "Mel Gibson")
pelicula3 = Pelicula("Película", 3500, "", "Romance", "Margot Robbie")

libro1 = Libro("Libro", 7000, "", 200, "Cristina Bajo")
libro2 = Libro("Libro", 4500, "", 500, "Jogre Cuadradro")
libro3 = Libro("Libro", 6500, "", 1000, "Enrique Pinti")

disco1 = Disco("Música", 5000, "Románticos", 10, "Enrique Iglesias")
disco2 = Disco("Música", 4000, "Folclore", 12, "Rally Barrionuevo")
disco3 = Disco("Música", 3500, "POP", 11, "Tini Stoessel")
