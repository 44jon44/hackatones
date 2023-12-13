import markdown2
from GOL import Gol

gol = Gol()
for i in range(gol.gameTurns):
    gol.draw_grid()
    gol.nextTurn()
    gol.clear()
    gol.wait()
