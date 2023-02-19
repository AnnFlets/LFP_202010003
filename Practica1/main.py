#Se importan la clase Pila, Película y Utilidades
from Pila import Pila
from Pelicula import Pelicula
from Utilidades import Utilidades

import os

print("""
Curso: Lenguajes Formales y de Programación
Sección: B-
Nombre: Ana Lucia Fletes Ordóñez
Carné: 202010003
""")
input("Pulse enter para continuar...")

miPila = Pila()
utilidad = Utilidades()
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
            while (menuSecundario):
                try:
                    print("\n--- Filtrado ---")
                    if miPila.tamanio() != 0:
                        print("1 - Filtrado por actor"
                              "\n2 - Filtrado por año"
                              "\n3 - Filtrado por género"
                              "\n4 - Salir")
                        opcionMenuSecundario = int(input("Ingrese la opción a ejecutar:"))
                        if opcionMenuSecundario == 1:
                            print("\n___ Filtrado por actor ___")
                            for actorMostrar in miPila.devolverActoresPeliculas():
                                print("* " + actorMostrar)
                            actorFiltro = input("Ingrese el nombre del actor a buscar:")
                            if utilidad.comprobarEntero(actorFiltro) or utilidad.comprobarDecimal(actorFiltro):
                                print("No debe ingresar valores numéricos")
                            else:
                                print("\nActor:", actorFiltro)
                                print("Resultado:")
                                contador = 0
                                for pelicula in miPila.retornarPeliculas():
                                    for actor in pelicula.obtenerActores():
                                        if actorFiltro.lower() == actor.lower():
                                            print("\t*", pelicula.obtenerNombre())
                                            contador = contador + 1
                                if contador == 0:
                                    print("No hay películas")
                        elif opcionMenuSecundario == 2:
                            print("\n___ Filtrado por año ___")
                            anioFiltro = int(input("Ingrese el año a buscar:"))
                            print("\nAño:", anioFiltro)
                            print("Resultado:")
                            contador = 0
                            for pelicula in miPila.retornarPeliculas():
                                if anioFiltro == int(pelicula.obtenerAnio()):
                                    print("\t*", pelicula.obtenerNombre(), "-", pelicula.obtenerGenero())
                                    contador = contador + 1
                            if contador == 0:
                                print("No hay películas")
                        elif opcionMenuSecundario == 3:
                            print("\n___ Filtrado por género ___")
                            generoFiltro = input("Ingrese el género a buscar:")
                            if utilidad.comprobarEntero(generoFiltro) or utilidad.comprobarDecimal(generoFiltro):
                                print("No debe ingresar valores numéricos")
                            else:
                                print("\nGénero:", generoFiltro)
                                print("Resultado:")
                                contador = 0
                                for pelicula in miPila.retornarPeliculas():
                                    if generoFiltro.lower() == pelicula.obtenerGenero().lower():
                                        print("\t*", pelicula.obtenerNombre())
                                        contador = contador + 1
                                if contador == 0:
                                    print("No hay películas")
                        elif opcionMenuSecundario == 4:
                            print("--- Regresando al menú principal")
                            menuSecundario = False
                        else:
                            print("No ingresó una opción existente")
                    else:
                        print("No hay películas cargadas")
                        menuSecundario = False
                except:
                    print("[Error]: Opción inválida")
        elif opcionMenuPrincipal == 4:
            print("\n--- Gráfica ---")
            if miPila.tamanio() != 0:
                file = open("grafica.dot", "w")
                file.write("digraph {\n")
                file.write("rankdir = TB\n")
                nodosEntrePeliculas = ""
                nodosEntreActores = ""
                for p in range(miPila.tamanio() - 1):
                    nodosEntrePeliculas += "nodoPelicula" + str(p) + " -> " + "nodoPelicula" + str(p+1) + " [style=invis]\n"
                for a in range(len(miPila.devolverActoresPeliculas()) - 1):
                    nodosEntreActores += "nodoActor" + str(a) + " -> " + "nodoActor" + str(a+1) + " [style=invis]\n"
                file.write(nodosEntrePeliculas)
                file.write(nodosEntreActores)
                actoresGrafica = miPila.devolverActoresPeliculas()
                contador = 0
                nodosActores = ""
                for actorGraph in actoresGrafica:
                    nodosActores += "nodoActor" + str(contador) + "[label=\"" + str(actorGraph) + "\" fillcolor=\"#A0B3F2\" shape=box style=filled width=3]\n"
                    contador = contador + 1
                peliculasGrafica = miPila.retornarPeliculas()
                contador = 0
                nodosPeliculas = ""
                edgePeliActor = ""
                for peliculaGraph in peliculasGrafica:
                    origen = "origen" + str(contador)
                    nodosPeliculas += str("nodoPelicula" + str(contador) + "[label=<"
                    "<TABLE BORDER='0' CELLBORDER='1' CELLSPACING='0'>"
                    "<TR>"
                    "<TD COLSPAN='2' bgcolor='#A0E9F2' PORT='" + origen + "'>" + str(peliculaGraph.obtenerNombre()) + "</TD>"
                    "</TR>"
                    "<TR>"
                    "<TD>" + str(peliculaGraph.obtenerAnio()) + "</TD>"
                    "<TD>" + str(peliculaGraph.obtenerGenero()) + "</TD>"
                    "</TR>"
                    "</TABLE>> shape=none]\n")
                    for actorPeliGraph in peliculaGraph.obtenerActores():
                        for actorGuardadoGraph in actoresGrafica:
                            if actorGuardadoGraph == actorPeliGraph:
                                edgePeliActor += str("nodoPelicula" + str(peliculasGrafica.index(peliculaGraph)) +
                                                     ":origen" + str(peliculasGrafica.index(peliculaGraph)) + " -> " +
                                                     "nodoActor" + str(actoresGrafica.index(actorGuardadoGraph)) +
                                                     "[constraint = false]\n")
                    contador = contador + 1
                file.write(nodosPeliculas)
                file.write(nodosActores)
                file.write(edgePeliActor)
                file.write("}")
                file.close()
                os.system("dot.exe -Tpdf grafica.dot -o  graficoPeliculas.pdf")
                print("¡Gráfico generado con éxito!")
            else:
                print("No hay películas cargadas")
        elif opcionMenuPrincipal == 5:
            print("\n--- Salir ---"
                  "\nSaliendo del programa...")
            menuPrincipal = False
        else:
            print("No ingresó una opción existente")
    except:
        print("[Error]: Opción inválida")