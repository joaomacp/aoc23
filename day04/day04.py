from dataclasses import dataclass

@dataclass
class Card:
  score: int
  copies: int

with open("input/day04.txt") as f:
  input = f.read()
input_lines = input.splitlines()

cards = []
result_part_one = 0
for card in input_lines:
  parts = card.split(": ")[1].split(" | ")
  winning = set([int(n) for n in parts[0].split(" ") if len(n) > 0])
  ours = set([int(n) for n in parts[1].split(" ") if len(n) > 0])
  card_score = 0
  for number in ours:
    if number in winning:
      card_score += 1
  if card_score > 0:
    result_part_one += 2**(card_score-1)
  cards.append(Card(card_score, 1))

print("Part 1:", result_part_one)

cards_processed = 0
for index, card in enumerate(cards):
  for _ in range(card.copies):
    for i in range(card.score):
      cards[index + i + 1].copies += 1
    cards_processed += 1

print("Part 2:", cards_processed)
