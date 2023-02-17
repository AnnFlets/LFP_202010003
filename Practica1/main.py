#Se importan la clase Pila y Película
from Pila import Pila
from Pelicula import Pelicula

print("""
Curso: Lenguajes Formales y de Programación
Sección: B-
Nombre: Ana Lucia Fletes Ordóñez
Carné: 202010003
""")
input("Pulse enter para continuar...")

miPila = Pila()
menuPrincipal = True

while(menuPrincipal):
    try:
        menuSecundario = True
        print("\n=== MENÚ ==="
              "\n1 - Cargar archivos de entrada"
              "\n2 - Gestionar películas"
              "\n3 - Filtrado"
              "\n4 - Gráfica"
              "\n5 - Salir")
        opcionMenuPrincipal = int(input("Ingrese la opción a ejecutar:"))
        if opcionMenuPrincipal == 1:
            print("\n--- Cargar archivo de entrada ---")
            ruta = str(input("Ingrese la ruta del archivo de entrada: "))
            try:
                archivo = open(ruta, "r")
                for linea in archivo:
                    pelicula = linea.split(";")
                    nombrePelicula = pelicula[0]
                    actoresPelicula = []
                    for actor in pelicula[1].split(","):
                        actoresPelicula.append(actor.strip())
                    anioPelicula = pelicula[2]
                    generoPelicula = pelicula[3].replace("\n", "")
                    contador = 0
                    for peliculaGuardada in miPila.retornarPeliculas():
                        peliPila = peliculaGuardada.obtenerNombre().strip()
                        peliLeida = nombrePelicula.strip()
                        if peliPila.lower() == peliLeida.lower():
                            miPila.eliminarPelicula(contador)
                            break
                        contador = contador + 1
                    elementoPelicula = Pelicula(nombrePelicula.strip(), actoresPelicula, anioPelicula.strip(), generoPelicula.strip())
                    miPila.push(elementoPelicula)
                archivo.close()
                print("¡Archivo cargado con éxito!")
            except:
                print("[Error]: Archivo no encontrado")
        elif opcionMenuPrincipal == 2:
            while(menuSecundario):
                try:
                    print("\n--- Gestionar películas ---")
                    if miPila.tamanio() != 0:
                        print("1 - Mostrar películas"
                              "\n2 - Mostrar actores"
                              "\n3 - Regresar al menú principal")
                        opcionMenuSecundario = int(input("Ingrese la opción a ejecutar:"))
                        if opcionMenuSecundario == 1:
                            contador = 1
                            for pelicula in miPila.retornarPeliculas():
                                print("\nPELÍCULA #", contador)
                                print("Nombre:", pelicula.obtenerNombre())
                                print("Actores:")
                                for actor in pelicula.obtenerActores():
                                    print("\t- ", actor)
                                print("Año:", pelicula.obtenerAnio())
                                print("Género:", pelicula.obtenerGenero())
                                contador = contador + 1
                        elif opcionMenuSecundario == 2:
                            contador = 1
                            print("\n___ PELÍCULAS ___")
                            for pelicula in miPila.retornarPeliculas():
                                print("#", contador, "-", pelicula.obtenerNombre())
                                contador = contador + 1
                            try:
                                numeroPelicula = int(
                                    input("Ingrese el número correspondiente a la película a elegir:")) - 1
                                actoresPeliculaElegida = miPila.devolverPelicula(numeroPelicula).obtenerActores()
                                print("\n***", miPila.devolverPelicula(numeroPelicula).obtenerNombre())
                                print("\tActores:")
                                for actor in actoresPeliculaElegida:
                                    print("\t-", actor)
                            except:
                                print("[Error]: Opción inválida")
                        elif opcionMenuSecundario == 3:
                            print("--- Regresando al menú principal")
                            menuSecundario = False
                        else:
                            print("No ingresó una opción existente")
                    else:
                        print("No hay películas cargadas")
                        menuSecundario = False
                except:
                    print("[Error]: Opción inválida")
        elif opcionMenuPrincipal == 3:
            print("\n--- Filtrado ---")
        elif opcionMenuPrincipal == 4:
            print("\n--- Gráfica ---")
        elif opcionMenuPrincipal == 5:
            print("\n--- Salir ---"
                  "\nSaliendo del programa...")
            menuPrincipal = False
        else:
            print("No ingresó una opción existente")
    except:
        print("[Error]: Opción inválida")