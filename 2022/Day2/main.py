file_path = "./input.txt"
with open(file_path, "r") as file:
  data = file.read().splitlines()

def play_to_score(play: str) -> int:
  return {"A X": 4,"A Y": 8,"A Z": 3,"B X": 1,"B Y": 5,"B Z": 9,"C X": 7,"C Y": 2,"C Z": 6}.get(play) or 0

def play_to_score_second_part(play: str) -> int:
  return {"A X": 3,"A Y": 4,"A Z": 8,"B X": 1,"B Y": 5,"B Z": 9,"C X": 2,"C Y": 6,"C Z": 7}.get(play) or 0

print(sum(map(play_to_score, data)))
print(sum(map(play_to_score_second_part, data)))