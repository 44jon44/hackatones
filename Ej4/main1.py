from TictacToe import TicTac
from MapGrid import MapGrid
import configparser
from GOL import Gol

config = configparser.ConfigParser()
config.read('config.ini')


while True:
    conf = input("1: Tic Tac Toe\n2: Dungeon Crawl\n3: Game of life\ns: Salir\nIngrese su elección: ")

    if conf == '1':
        t = TicTac()
        t.juego()

    elif conf == '2':
        mg = MapGrid(config['Dungeon Crawl']['height'], config['Dungeon Crawl']['width'])
        MapGrid.draw_grid(mg)
        MapGrid.movePlayer(mg)

    elif conf == '3':
        gol = Gol()
        for i in range(gol.gameTurns):
            gol.draw_grid()
            gol.nextTurn()
            gol.clear()
            gol.wait()

    elif conf == 's':
        print("Saliendo del programa...")
        break

    else:
        print("Entrada no válida. Por favor, elija una opción válida.")


