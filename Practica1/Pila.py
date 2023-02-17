class Pila:
    def __init__(self):
        self.peliculas = []

    def estaVacia(self):
        return self.peliculas == []

    def push(self, pelicula):
        self.peliculas.append(pelicula)

    def pop(self):
        return self.peliculas.pop()

    def retornarPeliculas(self):
        return self.peliculas

    def eliminarPelicula(self, posicion):
        self.peliculas.pop(posicion)

    def devolverPelicula(self, posicion):
        return self.peliculas[posicion]

    def tamanio(self):
        return len(self.peliculas)