from random import randint
import re
import numpy as np
print("Comienza el juego:")
tablero = np.zeros((3, 3), dtype=int)
patron_coordenadas = re.compile(r'^[0-2],[0-2]$')
players = ['\0', 'O', 'X']

class TicTac:
    def __init__(self):
        pass
    def mostrarTablero(self):
        line = " +----+ +----+ +----+ "
        print(line)
        print(" |   " + str(players[tablero[0][0]]) + " |   " + str(players[tablero[0][1]]) + "  |" + str(
            players[tablero[0][2]]) + "    |")
        print(line)
        print(" |   " + str(players[tablero[1][0]]) + " |   " + str(players[tablero[1][1]]) + "  |" + str(
            players[tablero[1][2]]) + "    |")
        print(line)
        print(" |   " + str(players[tablero[2][0]]) + " |   " + str(players[tablero[2][1]]) + "  |" + str(
            players[tablero[2][2]]) + "    |")
        print(line)

    def comprobarGanador(self):
        ganador = False
        if str(players[tablero[0][0]]) == str(players[tablero[0][1]]) == str(players[tablero[0][2]]):
            ganador = True
        if str(players[tablero[1][0]]) == str(players[tablero[1][1]]) == str(players[tablero[1][2]]):
            ganador = True
        if str(players[tablero[2][0]]) == str(players[tablero[2][1]]) == str(players[tablero[2][2]]):
            ganador = True
        ############################################
        if str(players[tablero[0][0]]) == str(players[tablero[1][0]]) == str(players[tablero[2][0]]):
            ganador = True
        if str(players[tablero[0][1]]) == str(players[tablero[1][1]]) == str(players[tablero[2][1]]):
            ganador = True
        if str(players[tablero[0][2]]) == str(players[tablero[1][2]]) == str(players[tablero[2][2]]):
            ganador = True
        ###########################################
        if str(players[tablero[0][0]]) == str(players[tablero[1][1]]) == str(players[tablero[2][2]]):
            ganador = True
        if str(players[tablero[0][2]]) == str(players[tablero[1][1]]) == str(players[tablero[2][0]]):
            ganador = True
        return ganador

    def juego(self):
        turno = 0
        contJ1 = 0
        contJ2 = 0
        firstPlayerIdx = 1 if randint(0, 1) == 0 else -1
        secondPlayerIdx = 1 if firstPlayerIdx == -1 else -1
        print("First Player: ", str(players[firstPlayerIdx]))
        print("Second Player: ", str(players[secondPlayerIdx]))

        for i in range(9):

            self.mostrarTablero()
            while True:
                if turno == 0:
                    selecc = input(f"First player, seleccione una casilla para poner: {str(players[firstPlayerIdx])}")
                    if patron_coordenadas.match(selecc):
                        fila, columna = selecc.split(',')
                        fila = int(fila)
                        columna = int(columna)
                        if tablero[fila][columna] == 0:
                            tablero[fila][columna] = firstPlayerIdx

                            turno = 1
                            break
                        else:
                            print("Casilla ya ocupada. Selecciona otra")

                    else:
                        print("mal Selecciona una casilla (X,Y)")
                else:
                    selecc = input(f"Second player, seleccione una casilla para poner: {str(players[secondPlayerIdx])}")
                    if patron_coordenadas.match(selecc):
                        fila, columna = selecc.split(',')
                        fila = int(fila)
                        columna = int(columna)
                        if tablero[fila][columna] == 0:
                            tablero[fila][columna] = secondPlayerIdx

                            turno = 0
                            break
                        else:
                            print("Casilla ya ocupada. Selecciona otra")

                    else:

                        print("mal Selecciona una casilla (X,Y)")
            if i >= 4:  # Chapuza pero funciona
                if turno == 1 and self.comprobarGanador():
                    print("GANADOR first player")
                    contJ1 = contJ1 + 1
                    print("El jugador 1 ha gando", contJ1, " partidas y el jugador2 ha ganado: ", contJ2, " partidas")
                    break
                if turno == 0 and self.comprobarGanador():
                    print("GANADOR second player")
                    contJ2 = contJ2 + 1
                    print("El jugador 1 ha gando", contJ1, " partidas y el jugador2 ha ganado: ", contJ2, " partidas")
                    break

        continuar = input("Quieres seguir jugando?Y/n")
        if continuar == "Y":
            self.juego()
        else:
            print("Has seleccionado Salir")


