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
                    actoresPelicula = pelicula[1].split(",")
                    anioPelicula = pelicula[2]
                    generoPelicula = pelicula[3].replace("\n", "")
                    contador = 0
                    for peliculaGuardada in miPila.retornarPeliculas():
                        if peliculaGuardada.obtenerNombre() == nombrePelicula:
                            miPila.eliminarPelicula(contador)
                            break
                        contador = contador + 1
                    elementoPelicula = Pelicula(nombrePelicula, actoresPelicula, anioPelicula, generoPelicula)
                    miPila.push(elementoPelicula)
                archivo.close()
                print("¡Archivo cargado con éxito!")
            except:
                print("[Error]: Archivo no encontrado")
        elif opcionMenuPrincipal == 2:
            print("\n--- Gestionar películas ---")
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