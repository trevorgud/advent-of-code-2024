
def safePair(num1, num2):
  diff = abs(num1 - num2)
  return 1 <= diff and diff <= 3

def safeReport(reportList):
  increasing = reportList[0] < reportList[1]
  for i in range(len(reportList) - 1):
    num1 = reportList[i]
    num2 = reportList[i+1]
    if increasing and (num1 > num2):
      # print("unsafe increasing")
      return False
    elif (not increasing) and (num1 < num2):
      # print("unsafe decreasing")
      return False
    if not safePair(num1, num2):
      # print("unsafe pair ", num1, num2)
      return False

  return True

safeCount = 0
for line in open("data.txt", "r"):
  if len(line) == 0:
    continue

  tokens = line.split()
  nums = []
  for token in tokens:
    nums.append(int(token))

  # print(nums)

  if safeReport(nums):
    safeCount += 1
  #   print("safe")
  # else:
  #   print("unsafe")


print(safeCount)

