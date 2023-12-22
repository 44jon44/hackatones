import configparser
import sys
from random import randint
from os import system, name
import time


class Gol:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        DEFAULT_CELL_WIDTH = int(config['Game of Life']['DEFAULT_CELL_WIDTH'])
        DEFAULT_CELL_HEIGHT = int(config['Game of Life']['DEFAULT_CELL_HEIGHT'])
        DEFAULT_INIT_ALIVE_CELLS_NUM = int(config['Game of Life']['DEFAULT_INIT_ALIVE_CELLS_NUM'])
        DEFAULT_GAME_TURNS = int(config['Game of Life']['DEFAULT_GAME_TURNS'])
        ALIVE = config['Game of Life']['ALIVE']
        DEAD = config['Game of Life']['DEAD']
        while True:
            width = input("Introduce un ancho o def para ancho por defecto: ")
            if width.isdigit():
                break
            elif width.lower() == "def":
                width = DEFAULT_CELL_WIDTH
                break
            else:
                print("Valor incorrecto. Introducuce un numero o 'def'")
        while True:
            height = input("Introduce un alto o def para alto por defecto: ")
            if height.isdigit():
                break
            elif height.lower() == "def":
                height = DEFAULT_CELL_HEIGHT
                break
            else:
                print("Valor incorrecto. Introducuce un numero o 'def'")
        while True:
            initAlive = input("Introduce un numero de celulas vivas o def para valor por defecto: ")
            if initAlive.isdigit():
                break
            elif initAlive.lower() == "def":
                initAlive = DEFAULT_INIT_ALIVE_CELLS_NUM
                break
            else:
                print("Valor incorrecto. Introducuce un numero o 'def'")
        while True:
            gameTurns = input("Introduce un numero de turnos o def para turnos por defecto: ")
            if gameTurns.isdigit():
                break
            elif gameTurns.lower() == "def":
                gameTurns = DEFAULT_GAME_TURNS
                break
            else:
                print("Valor incorrecto. Introducuce un numero o 'def'")
        self.width = width
        self.height = height
        self.initAlive = initAlive
        self.gameTurns = int(gameTurns)
        self.aliveCoor = self.setInitAlive()
        self.cellAlive = ALIVE
        self.cellDead = DEAD

    def draw_grid(self):
        for i in range(int(self.height)):
            for j in range(int(self.width)):
                if (j, i) in self.aliveCoor:
                    print(self.cellAlive, end=" ")
                else:
                    print(self.cellDead, end=" ")
            print()

    def setInitAlive(self):
        aliveCoord = set()
        while len(aliveCoord) < int(self.initAlive):
            coordx = randint(0, int(self.width) - 1)
            coordy = randint(0, int(self.height) - 1)
            aliveCoord.add((coordx, coordy))

        return aliveCoord

    def nextTurn(self):
        for i in range(int(self.height)):
            for j in range(int(self.width)):
                if (j, i) in self.aliveCoor:
                    if self.getNeighbours(j, i) > 3:
                        self.aliveCoor.remove((j, i))
                    elif self.getNeighbours(j, i) <= 1:
                        self.aliveCoor.remove((j, i))
                else:
                    if self.getNeighbours(j, i) == 3:
                        self.aliveCoor.add((j, i))

    def getNeighbours(self, j, i):
        numVivas = 0
        if (j - 1, i - 1) in self.aliveCoor and 0 <= j < self.width and 0 <= i < self.height:
            numVivas = numVivas + 1
        if (j - 1, i) in self.aliveCoor and 0 <= j < self.width and 0 <= i < self.height:
            numVivas = numVivas + 1
        if (j, i - 1) in self.aliveCoor and 0 <= j < self.width and 0 <= i < self.height:
            numVivas = numVivas + 1
        if (j - 1, i + 1) in self.aliveCoor and 0 <= j < self.width and 0 <= i < self.height:
            numVivas = numVivas + 1
        if (j + 1, i - 1) in self.aliveCoor and 0 <= j < self.width and 0 <= i < self.height:
            numVivas = numVivas + 1
        if (j + 1, i) in self.aliveCoor and 0 <= j < self.width and 0 <= i < self.height:
            numVivas = numVivas + 1
        if (j, i + 1) in self.aliveCoor and 0 <= j < self.width and 0 <= i < self.height:
            numVivas = numVivas + 1
        if (j + 1, i + 1) in self.aliveCoor and 0 <= j < self.width and 0 <= i < self.height:
            numVivas = numVivas + 1
        return numVivas

    def clear(self):
        print("Attempting to clear the screen...")
        if sys.stdin.isatty():
            print("\033c", end='', flush=True)
            print("Screen cleared successfully.")
        else:
            print("Non-interactive environment. Printing newlines instead.")
            print('\n' * 4)

    def wait(self):
        time.sleep(3)
