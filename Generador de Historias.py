import random

# Definir las listas iniciales de personajes, lugares y acciones
personajes = ["un caballero", "una princesa", "un dragon", "un mago", "un guerrero"]
lugares = ["en un castillo", "en el bosque", "en una cueva", "en la montaña", "en el rio"]
acciones = ["lucha contra", "encuentra", "explora", "descubre", "rescata"]

# Funcion para agregar un nuevo personaje
def agregarPersonaje():
    nuevoPersonaje = input("\nIngresa un nuevo personaje: ")
    personajes.append(nuevoPersonaje)

# Funcion para agregar un nuevo lugar
def agregarLugar():
    nuevoLugar = input("\nIngresa un nuevo lugar: ")
    lugares.append(nuevoLugar)

# Funcion para agregar una nueva accion
def agregarAccion():
    nuevaAccion = input("\nIngresa una nueva accion: ")
    acciones.append(nuevaAccion)

# Funcion para generar una historia aleatoria
def generarHistoria():
    personaje = random.choice(personajes)
    lugar = random.choice(lugares)
    accion = random.choice(acciones)
    historia = f"Habia una vez, {personaje} {accion} {lugar}."
    print("\nHistoria generada:")
    print(historia)

# Menu principal
def menu():
    opc = 1  # Se inicializa con un valor distinto a 0 para entrar en el while

    while(opc != 0):
        print("\n\t\t....Generador de historias....")
        print("\n\t\t\t.:MENU:.\n")
        print("\t1. Agregar un nuevo personaje")
        print("\t2. Agregar un nuevo lugar")
        print("\t3. Agregar una nueva accion")
        print("\t4. Generar historia")
        print("\t0. Salir")

        opc = int(input("\tDigite la opcion a realizar: "))

        if opc == 1:            #Opcion para añadir personaje nuevo
            agregarPersonaje()
        elif opc == 2:          #Opcion para añadir lugar nuevo
            agregarLugar()
        elif opc == 3:          #Opcion para añadir accion nueva
            agregarAccion()
        elif opc == 4:          #opcion para generar una historia aleatoria
            generarHistoria()
        elif(opc == 0):     #Opcion para salir de la aplicacion
            print("\n\t\tGracias por usar mi app!!!\n\n")
            print("\t.:FIN DEL PROGRAMA:.\n")
        else:
            print("\n\t\t.:OPCION INCORRECTA:.\n")      #Mostrar si la opcion es incorrecta

menu()
