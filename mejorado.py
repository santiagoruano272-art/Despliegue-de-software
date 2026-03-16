#Algoritmo mejorado
# =====================================================
# SISTEMA DE RECOMENDACIÓN - CineMax 
# =====================================================


# =====================================================
# 1. RECOMENDACIÓN SEGÚN GÉNERO FAVORITO
# =====================================================

def sistema_varios_usuarios():

    # VARIABLES DE ENTRADA
    usuarios = {
        "Ana": {"Accion":5, "Comedia":2, "Drama":1, "CienciaFiccion":4, "Terror":1},
        "Luis": {"Accion":1, "Comedia":5, "Drama":2, "CienciaFiccion":1, "Terror":2},
        "Marta": {"Accion":2, "Comedia":1, "Drama":5, "CienciaFiccion":2, "Terror":1},
        "Juan": {"Accion":4, "Comedia":2, "Drama":1, "CienciaFiccion":5, "Terror":1},
        "Sara": {"Accion":1, "Comedia":3, "Drama":2, "CienciaFiccion":1, "Terror":5}
    }

    peliculas = {
        "Accion":"Misión Imposible",
        "Comedia":"Son como niños",
        "Drama":"En busca de la felicidad",
        "CienciaFiccion":"Interestelar",
        "Terror":"El conjuro"
    }

    print("\n===== RECOMENDACIONES =====\n")

    for usuario, calificaciones in usuarios.items():

        # VARIABLE INTERMEDIA
        genero_favorito = max(calificaciones, key=calificaciones.get)

        # VARIABLE DE SALIDA
        pelicula_recomendada = peliculas[genero_favorito]

        print("Usuario:", usuario)
        print("Género favorito:", genero_favorito)
        print("Película recomendada:", pelicula_recomendada)
        print("--------------------------------")


# =====================================================
# 2. RECOMENDACIÓN DE PRODUCTOS (TIPO AMAZON)
# =====================================================

def recomendacion_productos():

    # VARIABLES DE ENTRADA
    productos = {
        "Celular": "Audifonos",
        "Portatil": "Mouse",
        "Televisor": "Barra de sonido",
        "Libro": "Lampara de lectura",
        "Consola": "Control adicional"
    }

    producto = input("Ingrese el producto comprado: ")

    # VARIABLE INTERMEDIA
    producto_existe = producto in productos

    if producto_existe:

        # VARIABLE DE SALIDA
        recomendacion = productos[producto]

        print("Producto comprado:", producto)
        print("Producto recomendado:", recomendacion)

    else:
        print("No tenemos una recomendación para ese producto.")


# =====================================================
# 3. RECOMENDACIÓN POR USUARIOS SIMILARES
# =====================================================

def recomendacion_por_similitud():

    # VARIABLES DE ENTRADA
    usuarios = {

        "Ana": {"Pelicula1":True, "Pelicula2":True, "Pelicula3":False, "Pelicula4":False},
        "Juan": {"Pelicula1":True, "Pelicula2":True, "Pelicula3":True, "Pelicula4":False},
        "Luis": {"Pelicula1":False, "Pelicula2":True, "Pelicula3":False, "Pelicula4":True}
    }

    print("\n===== RECOMENDACIÓN POR SIMILITUD =====\n")

    def calcular_similitud(usuario1, usuario2):

        # VARIABLE INTERMEDIA
        puntos = 0

        for pelicula in usuario1:
            if usuario1[pelicula] == usuario2[pelicula]:
                puntos += 1

        return puntos


    # VARIABLES INTERMEDIAS
    similitud_juan = calcular_similitud(usuarios["Ana"], usuarios["Juan"])
    similitud_luis = calcular_similitud(usuarios["Ana"], usuarios["Luis"])

    if similitud_juan > similitud_luis:
        usuario_parecido = "Juan"
    else:
        usuario_parecido = "Luis"

    print("Usuario más parecido a Ana:", usuario_parecido)

    # VARIABLES DE SALIDA
    for pelicula, vista in usuarios[usuario_parecido].items():

        if vista and not usuarios["Ana"][pelicula]:

            print("Película recomendada para Ana:", pelicula)


# =====================================================
# MENÚ PRINCIPAL
# =====================================================

def menu():

    while True:

        print("\n===== MENÚ DEL SISTEMA =====")
        print("1. Recomendación por género")
        print("2. Recomendación de productos")
        print("3. Recomendación por similitud")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sistema_varios_usuarios()

        elif opcion == "2":
            recomendacion_productos()

        elif opcion == "3":
            recomendacion_por_similitud()

        elif opcion == "4":
            print("Programa finalizado")
            break

        else:
            print("Opción inválida")


menu()