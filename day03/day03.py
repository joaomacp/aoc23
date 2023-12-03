## Input
from dataclasses import dataclass

@dataclass(eq=False)
class EngineNumber:
  value: int
  i: int
  j: int

@dataclass
class Asterisk:
  i: int
  j: int

with open("input/day03.txt") as f:
  input = f.read()
input_lines = input.splitlines()
n_rows = len(input_lines)
n_cols = len(input_lines[0])

engine_numbers = []
asterisks = []
for i, line in enumerate(input_lines):
  cur_number_string = ""
  cur_number_start_j = -1
  for j, char in enumerate(line):
    if char.isdigit():
      if cur_number_start_j == -1:
        cur_number_start_j = j
      cur_number_string += char
    if not char.isdigit() or j == n_cols - 1:
      if char == "*": # for part 2
        asterisks.append(Asterisk(i, j))
      if cur_number_string:
        engine_numbers.append(EngineNumber(int(cur_number_string), i, cur_number_start_j))
      cur_number_string = ""
      cur_number_start_j = -1


## Part 1
import math

def is_part_number(engine_num):
  for i in range(engine_num.i - 1, engine_num.i + 2):
    for j in range(engine_num.j - 1, engine_num.j + int(math.log10(engine_num.value)) + 2):
      if 0 <= i < n_rows and 0 <= j < n_cols:
        char = input_lines[i][j]
        if not char.isdigit() and char != ".":
          return True

  return False

result_part_one = 0
for engine_num in engine_numbers:
  if is_part_number(engine_num):
    result_part_one += engine_num.value

print("Part 1:", result_part_one)


## Part 2
def get_owning_engine_number(i, j):
  for engine_number in engine_numbers:
    if engine_number.i == i:
      if engine_number.j <= j < engine_number.j + int(math.log10(engine_number.value)) + 1:
        return engine_number

def get_ratio(asterisk):
  neighbour_engine_numbers = set()
  for i in range(asterisk.i - 1, asterisk.i + 2):
    for j in range(asterisk.j - 1, asterisk.j + 2):
      if 0 <= i < n_rows and 0 <= j < n_cols:
        char = input_lines[i][j]
        if char.isdigit():
          neighbour_engine_numbers.add(get_owning_engine_number(i, j))
  if len(neighbour_engine_numbers) == 2:
    neighbour_list = list(neighbour_engine_numbers)
    return neighbour_list[0].value * neighbour_list[1].value
  return -1

result_part_two = 0
for asterisk in asterisks:
  if (ratio := get_ratio(asterisk)) != -1:
    result_part_two += ratio

print("Part 2:", result_part_two)