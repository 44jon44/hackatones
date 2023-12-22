from random import randint


class MapGrid:
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)
        self.walls = self.get_walls()
        self.playerw = 0
        self.playerh = 0

    def draw_grid(self):
        for i in range(int(self.height)):
            for j in range(int(self.width)):
                if (j, i) in self.walls and j != self.width and i != self.height:
                    print(" # ", end=" ")
                elif i == self.playerh and j == self.playerw:
                    print(" $ ", end=" ")
                elif i == self.height - 1 and j == self.width - 1:
                    print(" > ", end=" ")
                else:
                    print(" . ", end=" ")
            print()

    def get_walls(self):
        perc = float(input("Introduce el porcentaje de muros: "))
        if perc is None:
            perc = 0.3
        total = int(self.height) * int(self.width) / 2 * perc
        walls = set()

        for _ in range(int(total)):
            coordx = randint(0, self.width - 1)
            coordy = randint(1, self.height - 1)
            walls.add((coordx, coordy))

        return walls

    def movePlayer(self):

        while True:
            while True:
                mov = input("Which way?(l,r,u,d)or exit")
                if mov not in "l,r,u,d" and mov != "exit":
                    print("Incorrect. Only l,r,u,d")
                else:
                    break
            if mov == "l":
                if self.playerw - 1 < 0:
                    print("Invalid movement")
                elif (self.playerw - 1, self.playerh) in self.walls:
                    print("There´s a wall there...")
                else:
                    self.playerw = self.playerw - 1
            if mov == "r":
                if self.playerw + 1 >= self.width:
                    print("Invalid movement")
                elif (self.playerw + 1, self.playerh) in self.walls:
                    print("There´s a wall there...")
                else:
                    self.playerw = self.playerw + 1
            if mov == "u":
                if self.playerh - 1 < 0:
                    print("Invalid movement")
                elif (self.playerw, self.playerh - 1) in self.walls:
                    print("There´s a wall there...")
                else:
                    self.playerh = self.playerh - 1
            if mov == "d":
                if self.playerh + 1 >= self.height:
                    print("Invalid movement")
                elif (self.playerw, self.playerh + 1) in self.walls:
                    print("There´s a wall there...")
                else:
                    self.playerh = self.playerh + 1

            self.draw_grid()
            if self.playerw == self.width-1 and self.playerh == self.height-1:
                print("You made it to the end!")
                break
