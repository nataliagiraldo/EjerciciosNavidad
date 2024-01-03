def registrarPartida(jugadores : dict):
  
    idJ1 = input("Ingrese el codigo del jugador 1 ")
    categJ1 = jugadores[idJ1]['categoria']
    idJ2 = input("Ingrese el codigo del jugador 2 ")
    categJ2 = jugadores[idJ2]['categoria']
    

    if idJ1 and idJ2 in jugadores:
        if categJ1 == categJ2:
            categ = categJ1
            jugadoresEnCat = [jugador for jugador in jugadores.values() if jugador['categoria'] == categ]

            if len(jugadoresEnCat) >= 5:
                try: 

                    puntosJ1 = int(input("Ingrese la cantidad puntos positivos del jugador 1 en esta partida "))
                    puntosJ2 = int(input("Ingrese la cantidad puntos positivos del jugador 2 en esta partida "))
                    jugadores[idJ1]['partidas jugadas'] += 1
                    jugadores[idJ2]['partidas jugadas'] += 1
                    if puntosJ1>puntosJ2:
                        jugadores[idJ1]['partidas ganadas'] += 1
                        jugadores[idJ2]['partidas perdidas'] += 1
                        jugadores[idJ1]['puntos a favor'] += puntosJ1 - puntosJ2
                    elif puntosJ2>puntosJ1:
                        jugadores[idJ2]['partidas ganadas'] += 1
                        jugadores[idJ1]['partidas perdidas'] += 1
                        jugadores[idJ2]['puntos a favor'] += puntosJ2 - puntosJ1
                    elif puntosJ1 == puntosJ2:
                        if jugadores[idJ1]['total puntos']>jugadores[idJ2]['total puntos']:
                            jugadores[idJ1]['partidas ganadas'] += 1
                            jugadores[idJ2]['partidas perdidas'] += 1
                            jugadores[idJ1]['puntos a favor'] += puntosJ1 - puntosJ2
                        elif jugadores[idJ1]['total puntos']<jugadores[idJ2]['total puntos']:
                            jugadores[idJ2]['partidas ganadas'] += 1
                            jugadores[idJ1]['partidas perdidas'] += 1
                            jugadores[idJ2]['puntos a favor'] += puntosJ2 - puntosJ1
                        else:
                            print("ha habido empate")


                    jugadores[idJ1]['total puntos'] += jugadores[idJ1]['puntos a favor'] + (jugadores[idJ1]['partidas ganadas'] * 2)
                    jugadores[idJ2]['total puntos'] += jugadores[idJ2]['puntos a favor'] + (jugadores[idJ2]['partidas ganadas'] * 2)
                    

                except ValueError:
                    print("Error: ingrese un valor numerico ")
            else:
                print("Aun no hay suficientes jugadores registrados en la categoria para comenzar la partida")
        else:
            print("Los jugadores no pertenecen a la misma categoria ")
    else: 
        print("Los usuarios no se encuentran registrados")

def tablero(jugadores : dict):
    print("TABLERO")
    print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(
        "id", "nombre", "edad", "categoria" ,"partidas jugadas", "partidas ganadas",
        "partidas perdidas","puntos a favor","total puntos" 
    ))

    print("-" * 150)

    for jugadores, infoJugador in jugadores.items():
        print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(
            infoJugador["id"],
            infoJugador["nombre"],
            infoJugador["edad"],
            infoJugador["categoria"],
            infoJugador["partidas jugadas"],
            infoJugador["partidas ganadas"],
            infoJugador["partidas perdidas"],
            infoJugador["puntos a favor"],
            infoJugador["total puntos"]
        ))
    