list1 = []
list2 = []
for line in open("data.txt", "r"):
  if len(line) == 0:
    continue

  tokens = line.split()
  # print(tokens)

  nums = []
  for token in tokens:
    try:
      num = int(token)
      nums.append(num)
    except:
      pass

  if len(tokens) != 2:
    continue

  list1.append(int(tokens[0]))
  list2.append(int(tokens[1]))

list1.sort()
list2.sort()
total = 0
for i in range(len(list1)):
  diff = abs(list1[i] - list2[i])
  total += diff

print(total)