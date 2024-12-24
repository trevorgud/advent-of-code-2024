
# NOTE: Scrapping this idea because does not account for already visited spaces, only total distance traveled.

# Idea:
# Given a starting pos.
# Given a board, positions of obstacles.
# Structure of obstacles can be map indexed by row and column.
# Maintain a relevant obstacles handle. This is obstacles according to the current facing direction.
# 1. lookup first vertical obstical traveling upwards, count steps and update current pos.
# 2. lookup first horizontal obstacle traveling rightwards, count steps and update current pos.
# 3. ....do the same steps until
# Start traveling upwards, count num spaces until first obstacle.

START = "^"
OBSTACLE = "#"

# (6, 4) facing upwards
# look up obstacles in idx4
# lets say we find (7, 4), (3, 4), (1, 4)
# facing upwards, we look for the first one smaller than the row which is 3
# 6-3=3, but we cant land on the obstacle, so (6-3)+1=4 and our new position is (4, 4)
# Maybe need to handle


class LabMap():
  def __init__(self):
    # Obstacles represented as 2 maps. Choose map based on orientation.
    # row_obstacles is list of obstacles while walking along a row.
    # col_obstacles is list of obstacles while walking along a col.
    self.row_obstacles = {}
    self.col_obstacles = {}
    self.starting_pos = None

  def read_map_file(self, map_file):
    row = 0
    for line in map_file:
      col = 0
      for char in line:
        if char == START:
          self.starting_pos = (row, col)
        elif char == OBSTACLE:
          if row not in self.row_obstacles:
            self.row_obstacles[row] = []
          if col not in self.col_obstacles:
            self.col_obstacles[col] = []
          self.row_obstacles[row].append(col)
          self.col_obstacles[col].append(row)

        col += 1
      row += 1


f = open("data-simple.txt", "r")
lab = LabMap()
lab.read_map_file(f)
print(lab.row_obstacles)
print(lab.col_obstacles)
print(lab.starting_pos)

def next_obstacle(pos, obstacles, forward=True):
  for obstacle in obstacles:


done = False
while not done:
  (row, col) = lab.starting_pos
  obstacles = lab.col_obstacles[col]

