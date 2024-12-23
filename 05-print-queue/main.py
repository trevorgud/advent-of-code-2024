import math

# NOTE: Optimal solution may be to construct a graph structure based on the rules.
# Traverse the graph structure as you iterate over each update line, and enforce the rules.
# Attach a map lookup over top of the graph, for const time lookup of starting number in each list.
# Instead will use naive approach for completion speed.

# Take a file object (already opened) and extract rules from the contents.
# Rules returned as a map from number to set of numbers.
def parse_rules(rules_file):
  rules_map = {}
  for line in rules_file:
    tokens = line.split("|")
    if len(tokens) != 2:
      raise Exception("invalid num rule tokens")
    t1 = int(tokens[0])
    t2 = int(tokens[1].rstrip())
    if t1 not in rules_map:
      rules_map[t1] = set()
    rules_map[t1].add(t2)
  return rules_map

# Take a file object (already opened) and extract updates from the contents.
# Updates returned as a list of lists.
def parse_updates(updates_file):
  updates = []
  for line in updates_file:
    tokens = line.split(",")
    update = []
    for token in tokens:
      update.append(int(token))
    updates.append(update)
  return updates

def extract_middle_num(update):
  # Assumes odd numbered update lists.
  i = math.floor(len(update) / 2)
  return update[i]


def is_valid_update(rules, update):
  passed_nums = []
  # Iterate over each page number update to check violations.
  for each in update:
    # No rules to enforce
    if each not in rules:
      continue
    # Look up the full rules for each number.
    required_after = rules.get(each)
    # Iterate over already passed numbers to compare required_after(p,e),
    # and where p is found before e but must must actually be after according to rule.
    for p in passed_nums:
      if p in required_after:
        # Invalid rule found
        return False
    # Track the numbers already passed.
    passed_nums.append(each)

  # No rule violations found.
  return True

rules_file = open("rules.txt", "r")
rules = parse_rules(rules_file)

updates_file = open("updates.txt", "r")
updates = parse_updates(updates_file)

# valid = is_valid_update(rules, [75,47,61,53,29])
# print("valid: ", valid)

# invalid = is_valid_update(rules, [75,97,47,61,53])
# print("invalid: ", invalid)

total = 0
for update in updates:
  if is_valid_update(rules, update):
    middle = extract_middle_num(update)
    total += middle
    print("Valid:   ", update)
  else:
    print("Invalid: ", update)

print("Total: ", total)
