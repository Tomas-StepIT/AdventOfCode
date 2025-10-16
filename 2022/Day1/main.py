elfs = [0]
elf_index = 0

while True:
  prompt = input()
  
  if prompt == "":
    elfs.append(0)
    elf_index += 1
    continue
  
  if prompt == "stop":
    break
  
  if not prompt.isnumeric():
    print("Invalid input")
    continue
  
  elfs[elf_index] += int(prompt)
  
elfs.sort(reverse=True)

max_calories = elfs[0]
top3_calories = elfs[0] + elfs[1] + elfs[2]

print(f"The elf with the most calories has {max_calories} calories and the Top 3 has a total of {top3_calories} calories")
