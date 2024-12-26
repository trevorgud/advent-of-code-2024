

def append_blocks(fs, id, num):
  newfs = fs
  for i in range(num):
    newfs.append(id)
  return newfs


def decompress(s):
  fs = []
  id = 0
  nchar = 0
  for char in s:
    num_blocks = int(char)
    if nchar % 2 == 0:
      # Interpret char as num file blocks
      append_blocks(fs, id, num_blocks)
      # Done with this ID, iterate to the next.
      id += 1
    else:
      # Interpret char as num empty blocks
      append_blocks(fs, None, num_blocks)

    nchar += 1
  return fs


def next_valid_block(fs, i):
  while i > -1 and fs[i] == None:
    i -= 1
  return i


def defrag(fs):
  # Start scanning with i from the end of fs.
  i = len(fs)-1
  for j, block in enumerate(fs):
    if block is None:
      i = next_valid_block(fs, i)
      # Defrag done
      if j >= i:
        break
      # Swap the empty block with the next valid block from the end.
      fs[j] = fs[i]
      # Wipe the old position of the block.
      fs[i] = None
    else:
      continue

  return fs


def checksum(fs):
  sum = 0
  for i, id in enumerate(fs):
    if id is None:
      break
    sum += i*id
  return sum


f = open("data.txt", "r")
compressed = f.read()

fs = decompress(compressed)
print(fs)

de = defrag(fs)
print(de)

cs = checksum(de)
print(cs)
