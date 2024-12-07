

f = open("data.txt", "r")
text = f.read()

rows = text.splitlines()
grid = [list(row) for row in rows]

# Constants to assist traversal of grid.
offsets = [
  (-1, -1), (-1, 0), (-1, 1),
  (0, -1), (0, 1),
  (1, -1), (1, 0), (1, 1),
]
imax = len(grid)
jmax = len(grid[0])

# Helper function to avoid out of bounds.
# Returns true if (i,j) is a valid index into the grid.
def valid_range(i, j):
  return (
    0 <= i and i < imax and
    0 <= j and j < jmax
  )

# The search string
search = "XMAS"

count = 0

# Iterate over each character in the grid as the starting character.
for i in range(imax):
  for j in range(jmax):
    # For each starting character,
    for (iOffset, jOffset) in offsets:
      iInner = i
      jInner = j
      substr = ""
      for _ in range(len(search)):
        if not valid_range(iInner, jInner):
          break

        substr += grid[iInner][jInner]

        iInner += iOffset
        jInner += jOffset

      if substr == search:
        count += 1

print(count)

