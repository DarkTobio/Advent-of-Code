#ADVENT OF CODE [3 - 1_2]

# PROBLEMA (3-1)

forest = ['...#...###......##.#..#.....##.',
'..#.#.#....#.##.#......#.#....#',
'......#.....#......#....#...##.',
'...#.....##.#..#........##.....',
'...##...##...#...#....###....#.',
'...##...##.......#....#...#.#..',
'..............##..#..#........#',
'#.#....#.........#...##.#.#.#.#',
'.#..##......#.#......#...#....#',
'#....#..#.#.....#..#...#...#...',
'#.#.#.....##.....#.........#...',
'......###..#....#..#..#.#....#.',
'##.####...#.............#.##..#',
'....#....#..#......#.......#...',
'...#.......#.#..#.........##.#.',
'......#.#.....###.###..###..#..',
'##..##.......#.#.....#..#....#.',
'..##.#..#....#.............##.#',
'....#.#.#..#..#........##....#.',
'.....####..#..#.###..#....##..#',
'#.#.......#...##.##.##..#....#.',
'.#..#..##...####.#......#..#...',
'#...##.......#...####......##..',
'...#.####....#.#...###.#.#...#.',
'....#...........#.##.##.#......',
'.....##...#.######.#..#....#..#',
'.#....#...##....#..######....#.',
'...#.....#...#####.##...#..#.#.',
'.....#...##........##.##.##.###',
'#.#..#....##....#......#....#.#',
'......##...#.........#....#.#..',
'###..#..##......##.#####.###.##',
'#.....#..##.##....#...........#',
'##..#.#..##..#.#.....#......#..',
'.#.##.#..#.#....##..#..#....#..',
'.#......##..##.#...#..#.......#',
'#....##.##..###..###......##.#.',
'....###..##.......#.###.#....#.',
'..##........#........##.....#..',
'.#..#.....#...####.##...##.....',
'....#.#.#.....#.##..##.....#..#',
'..............#.....#...#.....#',
'.#.....#......###...........#.#',
'.....#.#......#.##..#..........',
'.#......###............#.#.##..',
'.#.#....##.#..###.....#.##..#.#',
'.......#.#.#..#..#..#...##..#.#',
'.#.###...##.#.#.####.#.#...#...',
'...#.#....#......##.##.#.......',
'#...#.....##....#........##....',
'.....###...#.##.#......##.#..#.',
'..#...##.##.###..#..#......####',
'.#.##.#..#.##..##..........##..',
'..#.#.#..#.#.....#...###.....#.',
'..#..#.#....#.##.............##',
'.......#..###..#.#...#.....##.#',
'####.#.#......#..#.##.........#',
'..........#.....#..##......###.',
'..#..............#...#..##.....',
'......#.#.#..#.##.....####..##.',
'.##.#..#.#....#.......#..#.....',
'..#..#..#.##.#....###.#.#.#.#.#',
'.....#....#......###..#........',
'#.#.#..#...###.....#......#.##.',
'...#.#....#.#......#........#..',
'..#...###.#...#..#....##...#..#',
'.###.##..#..#...###.#..#.####..',
'#....#..##..##..#......#...##..',
'#.#..#...#..#...###..#.#.##....',
'##....#....##.####...#.#.###...',
'##.#...#.......#.##.##....#...#',
'..#.#..........#..#.#.#....#..#',
'..#........#...#....#....#....#',
'..#..#....#.......#........#...',
'......#....#....##.#....#.#.##.',
'.##...###.##.##....##.#...###..',
'.....##..#.#.....###..#.....###',
'....##.#.##...##..##........#..',
'#...#..##.#.#....#......#...#..',
'.###.##.#........#.####....#...',
'#.##.....#..#...#..##.##..#.#..',
'.....#.#..#....#..#...##.##.#..',
'.#......#####...##...#.#.###.#.',
'#......##....#.....#......##.#.',
'#.#.##.###.#......#####..#.....',
'........###.#...#..#.#........#',
'....#....###..#.##.#...#....#..',
'..........#..#.#....#...#.#...#',
'#.##......###.#.#.#....####...#',
'...#.#....#........##.#.....##.',
'.....##..#.#.#..###...##...#...',
'#...#...#....#....##........#..',
'.....#.........##.#......#..#..',
'#.....##..#.###.....#....##.##.',
'...#..#..#.#........##...##.#.#',
'..#..##.###.....#.#.....###.##.',
'..###.........#...##.....###...',
'...###...##.#...##....##.......',
'.#.#..#...###..#.#....#....#...',
'##..#.......#....#.#...#..#..#.',
'..#......#....####..##..#.###.#',
'..#.......##........#.#.#..#...',
'.#.......#.##.#.##.#.......#..#',
'###...#...#...#...#..#...#...##',
'..#..........#..###........##..',
'.##..#....##......##........#.#',
'......#.##......#......##...#.#',
'.#.#....#.#.#........#......#..',
'.#.#..#....####..##...##....#..',
'.#...##..#..#..#####....##.#...',
'.##.#.#...#...#.#...#.##.#...#.',
'###.#...##..#.###.#.....#.##.#.',
'#.....#.###.#.#...#..#....#.#..',
'..##..#....#......#.........###',
'.#...#...##......#...#.####....',
'..#.##...##..............#.#..#',
'..#......#..##...........#..#.#',
'..#####...#..#.......##...###..',
'..##..#....#.#...###.#...#.....',
'..#....#..#.#.......#..#.#.#...',
'.##..#.#.....##....#.......#...',
'...#.#..###...##....#....##..#.',
'.....##..#...##.####....##...#.',
'.......#.........#...#.##..####',
'........###..#..#.##.###..#....',
'.#.#..#.##.##.........#...#....',
'.###......#.....#....##....####',
'.##..##...........#.....#.....#',
'#.#.#.#.#.#.##..#.#.#..#.##....',
'.##.##...##..#....##..###..####',
'#..##.#......#...###.........#.',
'#..#...#..##..#..##.....##...#.',
'#...##..#...##.#.###.#...#.....',
'.###.....#.......#...#.##.###.#',
'..........#.#......#...###...##',
'..##....#.#..#....#.###...#..##',
'#.#..#....##.##..##.........##.',
'#.....#.##.###.#..#....##...#..',
'...#........##...#..###..######',
'#..#.#.#.#...#....#....###.#..#',
'...##.##.##.....##..#........#.',
'..#.#....#..#.......#...##.##.#',
'###.##.......##..#.####...#.#..',
'....#.#.....##.....#.#.##...#..',
'.#..##..#.....#.#..#...#..#..#.',
'.###....##...#......#.....#....',
'##.##.###......#...#...###.#...',
'#...#.##...#.#....##.....####..',
'#.#.#.#...###...##.............',
'..#....#.....##.#...#......#...',
'....#...#......#...#..#...#.#..',
'.###..#.....#..#...#....#...#..',
'..#...#.#..###.......#..#.#...#',
'#...###.##.....#....#..#.#..##.',
'...#.##.#.##......#.#.#.##.....',
'........####...##...##..#....#.',
'.#.#....#....#.#...##.###...##.',
'#.#...###.#.#.#....#....#.#....',
'.####.#..#.#....#..#.#..#..#...',
'#####...#...#...#....#.#.#..##.',
'..###.##.###...#..........#.##.',
'##.....#...#....###..###.#.#.#.',
'#..##.#..#..#..#...#.#...###..#',
'##....#.#...##......#.#...#...#',
'.##..........#.#....#...#.##..#',
'....#....####.#.####......#.###',
'..##.#.....####.#.####.......#.',
'#.##.##.#.....#.##......##...#.',
'......###..#.....#.....##......',
'..#..#....#.#...#.....#......##',
'##..#..#..###.#.#..#..##.....#.',
'#....#.#.....#####...#.#.......',
'.....#..#....#.#.#..#...#...#..',
'............#.##......##.##.#.#',
'....#...#.#........###....#....',
'..#..#...###.#....##..#..###.##',
'#.##....#...#.....##..#.##.#...',
'...##..###...#.#.....##.#......',
'.#..#.##.#####..#.......#..###.',
'...#.##...###.....####.#.#.....',
'.#......##.#.#.#.#.##.#.....#..',
'..#.##.#..##.......#.#.....##..',
'..................#....#...#...',
'.##.#..#.#.#..#.......#.#..##.#',
'....#........#......#..####..#.',
'#...#...##..##.#..#.......##...',
'#..#..#..#..#........####..#.#.',
'..#.#......#..#.##.##.#.#...#.#',
'...#..#......#.#.###.#.##..##..',
'..#...##.....#..#...##..#.#....',
'#.........#....#..#....##.##..#',
'..#..#.#....#..#...#.##.....#..',
'...#..#...#.#.....#..##..#.#...',
'....#........#.#....##..##..#..',
'#.....#.#..#.......#.##.....#..',
'.#.###.###...##...##..###...#..',
'.##.##.......#.#......#.....#.#',
'...#....##....#..#..........#.#',
'..#.##.........#.#.....#.....#.',
'...#.##..##.......##..##...#...',
'#.##......##.##..#.....##...##.',
'#.#.#..##...#.#............#.#.',
'....#.....#......##...#.#.....#',
'...#.#......#.#...###.......#..',
'......##..###....#.#...#.#####.',
'..#..#.#.#...##.#...###..##..#.',
'##.##.#.#.##.#..#....#...#...#.',
'#..#....######.##.#...#...#.#..',
'.#..#.##....#..#.#.......#....#',
'....#....#......##....##.#.#...',
'.###......#..#..#.......####..#',
'.#.#.....#..###...........##...',
'.##..##.##.....####..#..#..##..',
'..#..##.#......#...###.##..#.#.',
'....##..#.....###..#.##....##.#',
'#..#......#....#.........#.....',
'.#...#.....#.#..#..##....#.....',
'.##..#...#..##.#..#...........#',
'..#..##........##.......#..#...',
'#.....#....#....#.#.#...##.#...',
'...#...#.#.#..#.##.#.#...#.....',
'..#..#.#....#....###....#.#.#..',
'...###..#...#..#....#.....#....',
'...#...#.#..#.....#...###......',
'##......#..........#.#.#..#.#.#',
'....#.....#.....#..#..#.#.#.#..',
'...####...#.##...#.#..#....#.#.',
'#.##........##.............#.##',
'#.#.#.#.#.....................#',
'.#.###....#..##.##.##....#.....',
'#.#...#.####.###...#..#..#.#...',
'.##...#..###.......##..#.#.....',
'#.#.#.#...#...#.##.....#.......',
'.##.#.#.#......####..#.#.......',
'###..........#......#...##...#.',
'.........##...#.##...#.#.......',
'...#.#.....#...#..#...#..##..#.',
'.#..###...#.#.........###....#.',
'##..#...#........#.........##..',
'.....#...#.#...#.#.#...........',
'..#....##...#.#..#..#.##....##.',
'.##....#.#.....##.#..#..#...##.',
'..##......#.#...#.#.......##.#.',
'##...#..#...##.#........#.##...',
'#......#.##..#.#..#.###.......#',
'#.#...#.....#.#......#.#.#.....',
'#.....#..#.......#....##.#.#..#',
'###.#....#..##.#.##....#....#..',
'#.##.##....#.#..#.#...#....#...',
'####...#####...#.....#....##.#.',
'....#.#...#.#.##.#.#.##.#.#.###',
'#.....##.#.....#.#......#.#..#.',
'.#....##.#..#........#...##.#..',
'......#...#....##....##....##..',
'..###.....#....##.#...#..#.....',
'#....##...##.##..##.#...#...#..',
'#..#...#...#.#....##..#.#....#.',
'......................#.....#..',
'.#..#...#.........#....##...###',
'.##.#.#...##...#...#...#..#....',
'.#.###....#.#............##..#.',
'###..##.#.#.#.#....##...#......',
'.##................####...##.##',
'.#.#.........##....#.#.##.##.#.',
'....#...#...#...##...#.##.#..#.',
'.#.#........#..##.....#..#....#',
'##.#..#.#....#.....#...#...#...',
'.#...##....#.....##....#..#.#.#',
'####.....#..#....#......###.##.',
'##..##.#....###.....#...#......',
'.##.#...#.....#.#..#.#..#.#...#',
'.....#.#..#..#..###.#...###.#..',
'.#.#.##.#..#.#..#...#..#.......',
'..#.....#....#.##.##.##.......#',
'.#..##....###...#..............',
'#....#...#.#.......#....##.#...',
'....#.#..##.#....#..#.#....#.#.',
'#.........##...#.#.............',
'#.#.......##.....#...##..##.#.#',
'.......#....#..##...#..#######.',
'.#.#...##........#..#.....#.#..',
'.#.......#..#......#.##.##...##',
'.........#............#....#..#',
'.#......#...##...##...#....###.',
'.........#...#.#.###.......#...',
'###.#..#.#.#.#......##...#.#...',
'.#.........##.#....###....#.#..',
'#.#....#..#.##.#..#....##...#..',
'###.#...#..#..##........#.###..',
'.....#....#..#........#..#.##.#',
'..#.....##......#....#..#.#.#..',
'.#.........#.....#.....#.......',
'......#....#.###..#.#....#....#',
'..#.#..#.#.###.........#..#..#.',
'..#..#.#.#.........#....##.#.#.',
'#.......#........##...##....#..',
'##..#..#...###...#..##..#..#.#.',
'##..#..#....#.#..##..#..#.#..#.',
'..##.....##.#..#.#........###..',
'..#.#..#..##........#...#....##',
'.##..#....##..#..#..#..#.#....#',
'#....#.....##........#.....#.##',
'......#....#.#..#......#.##....',
'.......#..#..#......##.........',
'......#...#..##.....#......#..#',
'#..#..#....##....#........##..#',
'##....#...#.#.....#####........',
'...#.#..#.#.##.#.##..##...#....',
'..#..#..#..#..#....#..#..##...#',
'.#.....#....##.##....##.....#..',
'#...#.....#.....#.#...#.#....#.',
'.###...#..##....#..#...#.###...',
'....#..##..#.......#.##.##..###',
'#.......##.....#.......#.#...##',
'#.....#.#.#....#.#......#.#.#..',
'..##.....#..###......##........',
'.....#...#..##....#......#.....',
'#..#..#....#.#...#..###.......#',
'.....#.....#....#..#...#.#..##.',
'#####........#...#..#..##..#.#.',
'.#..#...#.##....#.#..#......###',
'#.###.#..#.....##..##....#...#.',
'.#...#.#####....##..........##.']


encounter = []
tree_lines = 0
tree_pos = 0

while tree_lines < len(forest): # RECORRE FILAS

  while tree_pos < len(forest[tree_lines]): # RECORRE COLUMNAS
    encounter.append(forest[tree_lines][tree_pos])
    tree_pos += 3
    break

  if tree_pos >= len(forest[tree_lines]):
    tree_pos = tree_pos - len(forest[tree_lines])

  tree_lines += 1

print("Total de árboles P3-1:", encounter.count('#')) # TOTAL DE ÁRBOLES ENCONTRADOS


# PROBLEMA (3-2)

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

import numpy as np

# tuples for moves
right = (1,3,5,7,1)
down  = (1,1,1,1,2)


def conteo_arboles_ruta(right_x, down_x):

  #encounter = []
  tree_lines = 0
  tree_pos = 0
  contador_arboles = 0

  while tree_lines < len(forest): # RECORRE FILAS

    while tree_pos < len(forest[tree_lines]): # RECORRE COLUMNAS
      
      if forest[tree_lines][tree_pos] == '#':
        contador_arboles += 1

      tree_pos += right_x

      if tree_pos >= len(forest[tree_lines]):
        tree_pos = tree_pos - len(forest[tree_lines])

      tree_lines += down_x
      
      break

  return(contador_arboles)


rutas = []

for i in range(0, len(right)):
  rutas.append(conteo_arboles_ruta(right[i],down[i]))


print("Total árboles según ID ruta",rutas)
print("Multip arboles rutas", np.prod(rutas))