def read_lab(lab_file):
  text = lab_file.read()
  rows = text.splitlines()
  grid = [list(row) for row in rows]
  return grid

def get_start_pos(lab):
  rowNum = 0
  for row in lab:
    colNum = 0
    for col in row:
      if col == "^":
        return (rowNum, colNum)
      colNum +=1
    rowNum +=1
  # Not found
  return None

f = open("data.txt", "r")

lab = read_lab(f)
start = get_start_pos(lab)

print(lab)
print(start)

# Length and width of lab grid.
labw = len(lab[0])
labh = len(lab)

# Traversal directions. Alternate as the guard turns right at each obstacle.
# 0. Traversing upwards.
# 1. Traversing rightwards.
# 2. Traversing downwards.
# 3. Traversing leftwards.
directions = [
  (-1, 0),
  (0, 1),
  (1, 0),
  (0, -1),
]

def patrol_lab(lab, start):
  turn_num = 0
  current_pos = start
  visited = {}
  while True:
    (row_offset, col_offset) = directions[turn_num % 4]
    found_obstacle = False
    while not found_obstacle:
      visited[current_pos] = True
      print(current_pos)
      (current_row, current_col) = current_pos
      next_row = current_row + row_offset
      next_col = current_col + col_offset
      # Have exited the grid, done traversing
      if 0 > next_row or next_row >= labh or 0 > next_col or next_col >= labw:
        return visited
      # Found an obstacle
      if lab[next_row][next_col] == "#":
        found_obstacle = True
      # Take another step
      else:
        current_pos = (next_row, next_col)

    turn_num += 1

visited = patrol_lab(lab, start)

# print(visited)

print(len(visited))