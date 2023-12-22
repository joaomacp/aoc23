from dataclasses import dataclass

@dataclass
class Mapping:
  destRangeStart: int
  sourceRangeStart: int
  rangeLength: int

  # returns tuple: (was_mapped, mapping) - meaning we can early-stop, even when mapping to the same number
  def map(self, n):
    if n in range(self.sourceRangeStart, self.sourceRangeStart + self.rangeLength):
      return (True, self.destRangeStart + n - self.sourceRangeStart)
    return (False, 0)

def process_map(list_of_mappings, n):
  for mapping in list_of_mappings:
    result = mapping.map(n)
    if result[0]:
      return result[1]
  return n

with open("input/day05.txt") as f:
  input = f.read()
input_lines = input.splitlines()

seeds = [int(num) for num in input_lines[0].replace("seeds: ", "").split(" ")]

maps = [] # list of lists of mappings

curr_map_index = -1
for line in input_lines[2:]:
  if line == "":
    continue
  if ":" in line:
    curr_map = []
    maps.append(curr_map)
    curr_map_index += 1
    continue
  mapping_parts = [int(part) for part in line.split(" ")]
  curr_map.append(Mapping(*mapping_parts))

resulting_seed_locations = []
for seed in seeds:
  for map in maps:
    seed = process_map(map, seed)
  resulting_seed_locations.append(seed)

print("Part 1: ", min(resulting_seed_locations))
