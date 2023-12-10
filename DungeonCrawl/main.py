from MapGrid import MapGrid

height = int(input("Introduce un  altura: "))
width = int(input("Introduce un ancho: "))


mg = MapGrid(height, width)
MapGrid.draw_grid(mg)
MapGrid.movePlayer(mg)



