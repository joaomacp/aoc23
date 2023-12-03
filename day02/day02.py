## Input
from dataclasses import dataclass

@dataclass
class CubeReveal:
  amount: int
  colour: str

@dataclass
class Game:
  id: int
  reveal_sets: list

with open("input/day02.txt") as f:
  input = f.read()
input_lines = input.splitlines()

games = []
for index, line in enumerate(input_lines):
  line = line.split(": ")[1]
  reveal_sets = []
  game = Game(index + 1, reveal_sets)
  games.append(game)
  for reveal_set in line.split("; "):
    set = []
    game.reveal_sets.append(set)
    for reveal_string in reveal_set.split(", "):
      amount = int(reveal_string.split(" ")[0])
      colour = reveal_string.split(" ")[1]
      set.append(CubeReveal(amount, colour))


## Part 1
capacities = {
   "red": 12,
   "green": 13,
   "blue": 14
}

result_part_one = 0

for game in games:
  count_game = True
  for reveal_set in game.reveal_sets:
    for reveal in reveal_set:
      if reveal.amount > capacities[reveal.colour]:
        count_game = False
    
  if count_game:
    result_part_one += game.id

print("Part 1:", result_part_one)


## Part 2
result_part_two = 0

for game in games:
  minimum_capacities = {"red": 0, "green": 0, "blue": 0}
  for reveal_set in game.reveal_sets:
    for reveal in reveal_set:
      minimum_capacities[reveal.colour] = max(minimum_capacities[reveal.colour], reveal.amount)
  result_part_two += minimum_capacities["red"] * minimum_capacities["green"] * minimum_capacities["blue"]

print("Part 2:", result_part_two)
