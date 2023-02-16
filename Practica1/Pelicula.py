class Pelicula:
    def __init__(self, nombre, actores, anio, genero):
        self.nombre = nombre
        self.actores = actores
        self.anio = anio
        self.genero = genero

    def obtenerNombre(self):
        return self.nombre

    def obtenerActores(self):
        return self.actores

    def obtenerAnio(self):
        return self.anio

    def obtenerGenero(self):
        return self.genero