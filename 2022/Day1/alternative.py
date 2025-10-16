file_path = "./input.txt"
with open(file_path, "r") as file:
  calories_data = file.read().split("\n\n")

elfs: list[int] = []
for batch in calories_data:
  calories_as_strings = batch.split("\n")
  calories_as_integers = map(int, calories_as_strings)
  elfs.append(sum(calories_as_integers))

elfs.sort(reverse=True)
print(f"The most calories is {elfs[0]}")
print(f"Total of Top 3 is {sum(elfs[:3])} calories")