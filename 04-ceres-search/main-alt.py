# This implementation does not account for diagonals.
# I didn't read carefully enough.
# Keeping it for reference because I thought transpose approach was clever.


# Given a grid string containing newlines,
# transpose it into a new grid.
# Credit to ChatGPT for this one.
def transpose_grid(grid):
  # Step 1: Split the grid into rows
  rows = grid.splitlines()

  # Step 2: Split each row into characters
  grid_matrix = [list(row) for row in rows]

  # Step 3: Transpose the grid
  transposed = zip(*grid_matrix)

  # Step 4: Join back into lines and then into a single string
  transposed_rows = [''.join(row) for row in transposed]
  transposed_grid = '\n'.join(transposed_rows)

  return transposed_grid

def count_occurrences(text, substring):
  count = 0
  i = 0
  end = len(text)
  done = False
  while not done:
    pos = text.find(substring, i, end)
    if pos == -1:
      done = True
    else:
      i = pos + 1
      count += 1
  return count

f = open("data.txt", "r")
grid = f.read()
print("transposing")
tgrid = transpose_grid(grid)

xmas = "XMAS"
samx = "SAMX"

total = 0
print("counting 1")
total += count_occurrences(grid, xmas)
print("counting 2")
total += count_occurrences(grid, samx)
print("counting 3")
total += count_occurrences(tgrid, xmas)
print("counting 4")
total += count_occurrences(tgrid, samx)

print(total)