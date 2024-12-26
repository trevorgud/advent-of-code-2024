from itertools import combinations


# Takes a 2d list of characters.
# Return a dicitonary where key is antenna frequency, and value is
# a list of coordinates for that antenna frequency.
def read_map(grid):
  antenna_locs = {}
  for nrow, row in enumerate(grid):
    for ncol, char in enumerate(row):
      if char == ".":
        continue
      if char not in antenna_locs:
        antenna_locs[char] = []
      antenna_locs[char].append((nrow, ncol))

  return antenna_locs


# Takes a file (already opened) and returns the text as a 2d array of characters.
def read_grid(map_file):
  text = f.read()
  rows = text.splitlines()
  grid = [list(row) for row in rows]
  return grid


# Extrapolate out along the line in the direction of p2,
# exptrapolate out the same distance between the two points.
def extrapolate(p1, p2):
  (p10, p11) = p1
  (p20, p21) = p2
  p30 = p20+(p20-p10)
  p31 = p21+(p21-p11)
  return (p30, p31)


f = open("data.txt", "r")

g = read_grid(f)
m = read_map(g)

maph = len(g)
mapw = len(g[0])


# Returns true if the point is in bounds, false if it is out of bounds.
def in_bounds(p):
  (p1, p2) = p
  return (0 <= p1 and p1 < maph) and (0 <= p2 and p2 < mapw)


# Given the list of nodes as a list of coordinates, return the set of antinode coordinates.
def find_antinodes(nodes):
  antinodes = set()
  pairs = combinations(nodes, 2)
  for (p1, p2) in pairs:
    p3 = extrapolate(p1, p2)
    if in_bounds(p3):
      antinodes.add(p3)
    p4 = extrapolate(p2, p1)
    if in_bounds(p4):
      antinodes.add(p4)
  return antinodes


antinodes = set()
for freq in m:
  nodes = m[freq]
  an = find_antinodes(nodes)
  antinodes = antinodes.union(an)

print(antinodes)
print(len(antinodes))
