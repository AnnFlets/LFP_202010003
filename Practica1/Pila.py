class Pila:
    def __init__(self):
        self.peliculas = []

    def push(self, pelicula):
        self.peliculas.append(pelicula)

    def retornarPeliculas(self):
        return self.peliculas

    def eliminarPelicula(self, posicion):
        self.peliculas.pop(posicion)

    def devolverPelicula(self, posicion):
        return self.peliculas[posicion]

    def devolverActoresPeliculas(self):
        actores = []
        for pelicula in self.peliculas:
            for actor in pelicula.obtenerActores():
                if len(actores) != 0:
                    contador = 0
                    actorVerificar = actor
                    for actorPeli in actores:
                        if actorVerificar == actorPeli:
                            contador = contador + 1
                    if contador == 0:
                        actores.append(actor)
                else:
                    actores.append(actor)
        return actores
    def tamanio(self):
        return len(self.peliculas)
    