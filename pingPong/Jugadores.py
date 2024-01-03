def registroJugador(jugadores : dict)->dict:   
    try:
        id=input("Ingrese el id del jugador ")

        if id in jugadores:
            print("Error: El ID ya esta registrado")
            return jugadores
        nombre = input("Ingrese el nombre del jugador ")
        edad = int(input("ingrese la edad del usuario "))
        pJ = 0
        pG = 0
        pP = 0
        pA = 0
        tP = 0
        
    except ValueError:
        print("Error: Ingrese un valor numérico válido para la edad")
        return jugadores
    jugador = {
        "id" : id,
        "nombre": nombre,
        "edad" : edad,
        "partidas jugadas" : pJ,
        "partidas ganadas" : pG,
        "partidas perdidas" : pP,
        "puntos a favor" : pA,
        "total puntos" : tP
    }
    if edad in range(15, 17):
        jugador["categoria"] = "Novato"
    elif edad in range(17, 21):
        jugador["categoria"] = "Intermedio"
    else:
        jugador["categoria"] = "Avanzado"
    jugadores[id] = jugador
    return jugadores

def compararJugadores(jugador):
    (jugador['total puntos'], jugador['puntos a favor'])

def ganadorCategoria(jugadores: dict):
    puntajesN = []
    puntajesI = []
    puntajesA = []
    for idJugador, jugador in jugadores.items():
        categoria = jugador['categoria']
        if categoria == "Novato":
            puntajesN.append(jugador)
        elif categoria == "Intermedio":
            puntajesI.append(jugador)
        elif categoria == "Avanzado":
            puntajesA.append(jugador)

    def imprimirGanadorCategoria(categoria, puntajes):
        if puntajes:
            print(f"\nGanador en la categoría {categoria}:")
            print("{:<20} {:<20} {:<20}".format("id", "nombre", "total puntos"))
            print("-" * 60)
            ganador = puntajes[0]
            print("{:<20} {:<20} {:<20}".format(ganador["id"], ganador["nombre"], ganador["total puntos"]))
        else:
            print(f"No hay jugadores registrados en la categoría {categoria}.")

    puntajesN.sort(key=compararJugadores, reverse=True)
    puntajesI.sort(key=compararJugadores, reverse=True)
    puntajesA.sort(key=compararJugadores, reverse=True)

    imprimirGanadorCategoria("Novato", puntajesN)
    imprimirGanadorCategoria("Intermedio", puntajesI)
    imprimirGanadorCategoria("Avanzado", puntajesA)
