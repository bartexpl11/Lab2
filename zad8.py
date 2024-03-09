arr = [1, 'ha', 2, 'dwaaa', 3, 'halo', 4, 'opop', 5, 'piec', 1, 2, 3, 4, 5, 4, 5, 5]

licz_dict = {}
for element in arr:
  if element in licz_dict:
    licz_dict[element] += 1
  else:
    licz_dict[element] = 1

numeric_dict = {}
for key, value in licz_dict.items():
  if isinstance(key, int):
    numeric_dict[key] = value

print(numeric_dict)
