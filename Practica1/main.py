#Se importan la clase Pila, Película y Utilidades
from Pila import Pila
from Pelicula import Pelicula
from Utilidades import Utilidades

#Se importa Graphviz
import graphviz


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
                            actorFiltro = input("Ingrese el actor a buscar:")
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
                grafico = graphviz.Digraph(format="png")
                actoresGrafica = miPila.devolverActoresPeliculas()
                contador = 0
                for actorGraph in actoresGrafica:
                    grafico.node("nodoActor" + str(contador), str(actorGraph), shape="box", style='filled', fillcolor='#A0B3F2')
                    contador = contador + 1
                peliculasGrafica = miPila.retornarPeliculas()
                contador = 0
                for peliculaGraph in peliculasGrafica:
                    origen = "origen" + str(contador)
                    grafico.node("nodoPelicula" + str(contador), "<" +
                                "<TABLE BORDER='0' CELLBORDER='1' CELLSPACING='0'>" +
                                  "<TR>" +
                                    "<TD COLSPAN='2' bgcolor='#A0E9F2' PORT='" + origen + "'>" + str(peliculaGraph.obtenerNombre()) + "</TD>" +
                                  "</TR>" +
                                  "<TR>" +
                                    "<TD>" + str(peliculaGraph.obtenerAnio()) + "</TD>" +
                                    "<TD>" + str(peliculaGraph.obtenerGenero()) + "</TD>" +
                                  "</TR>" +
                                "</TABLE>>", shape="none")
                    for actorPeliGraph in peliculaGraph.obtenerActores():
                        for actorGuardadoGraph in actoresGrafica:
                            if actorGuardadoGraph == actorPeliGraph:
                                grafico.edge("nodoPelicula" + str(peliculasGrafica.index(peliculaGraph)) + ":origen" + str(peliculasGrafica.index(peliculaGraph)), "nodoActor" + str(actoresGrafica.index(actorGuardadoGraph)))
                    contador = contador + 1
                print(grafico.source)

                """
                file = open('graphviz.dot', 'w')
                file.write(grafico.source)
                file.close()
                grafico.render(directory='grafico').replace('\\', '/')
                graphviz.render('dot', 'png', 'graphviz.dot')
                """
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