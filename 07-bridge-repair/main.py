# Attempting brute force

# Equations represented as list of tuple, where for each tuple,
# t0 is the test value and t1 is the numbers list.
def parse_equations(equations_file):
  equations = []
  for line in equations_file:
    tokens = line.split(": ")
    test_val = tokens[0]
    inner_tokens = tokens[1].split()
    numbers = []
    for token in inner_tokens:
      numbers.append(int(token))
    equations.append((int(test_val), numbers))
  return equations

# Set of operands is represented as a single integer value.
# Each bit representation of the integer is one operand.
# 0 is + and 1 is *
# 10 operand choices means an int sized to 10 bits, so max 2^10.

# The number of operand choices available.
def num_choices(numbers):
  # Always will be 1 less operand choice than the count of numbers
  return len(numbers) - 1

# Increment the operands to get the next set of operands.
def next_operands(operands):
  return operands + 1

# Returns the first invalid operands.
def end_operands(num_choices):
  return pow(2, num_choices)

# Get the initial starting operands for starting brute force.
def start_operands():
  return 0

# Can likely optimize by short circuiting running calcs that get too large.
# With only + and * a large number can never shrink back to a small one,
# so can abandon certain calcs early.

# When running calc exceeds target_val, exit early and return None.
# Function sig becomes:
# def evaluate_operands(numbers, operands, target_val):

def evaluate_operands(numbers, operands):
  nchoices = num_choices(numbers)
  current_calc = numbers[0]
  for i in range(nchoices):
    mask = pow(2, i)
    operand_bit = bool(operands & mask)
    next_number = numbers[i+1]
    if not operand_bit:
      current_calc = current_calc + next_number
    else:
      current_calc = current_calc * next_number
  return current_calc

# print("Evaluating!!!")
# print(2^0)
# print(evaluate_operands([5, 20], 0))
# print(evaluate_operands([5, 20], 1))
# print("DoneEvaluating!!!")


f = open("data.txt", "r")
equations = parse_equations(f)
# print(equations)

sum = 0

for eq in equations:
  (tval, numbers) = eq
  nchoices = num_choices(numbers)
  operands = start_operands()
  end = end_operands(nchoices)
  found_solution = False
  while operands != end and not found_solution:
    evaluated = evaluate_operands(numbers, operands)
    if evaluated == tval:
      found_solution = True
      print(tval, evaluated, numbers, operands, found_solution)
      print(sum)
    operands = next_operands(operands)

  if found_solution:
    sum += tval

print(sum)
