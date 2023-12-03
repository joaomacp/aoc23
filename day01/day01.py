## Input
with open("input/day01.txt") as f:
  input = f.read()
input_lines = input.splitlines()


## Part 1
def find_digit_part_one(char_iterator):
  for char in char_iterator:
    if char.isdigit():
      return char

result_part_one = 0

for line in input_lines:
  first_digit = find_digit_part_one(line)
  last_digit = find_digit_part_one(reversed(line))
  result_part_one += int(first_digit + last_digit)

print("Part 1:", result_part_one)


## Part 2
from queue import Queue

number_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def find_number_in_queue(q): # Returns 0 if not found
  for index, number_string in enumerate(number_strings):
    number_string_length = len(number_string)
    if (q.qsize() >= number_string_length
        and ''.join(list(q.queue)[-number_string_length::]) == number_string):
      return str(index + 1)
  return 0

result_part_two = 0

for line in input_lines:
  q = Queue(5) # the longest number strings have 5 characters
  numbers = []
  for char in line:
    if char.isdigit():
      numbers.append(char)
      q = Queue(5)
    else:
      if q.full():
        q.get()
      q.put(char)
      number_found = find_number_in_queue(q)
      if number_found != 0:
        numbers.append(number_found)
  result_part_two += int(numbers[0] + numbers[-1])

print("Part 2:", result_part_two)
