def suma_dziel(num):
  dividers = []
  for div in range(1, (num // 2) + 1):
    if (num % div) == 0:
      dividers.append(div)
  return sum(dividers)
 
def is_perfect(num):
  return suma_dziel(num) == num
 
count = 0
for i in range(1, 1000):
  count += 1 if is_perfect(i) else 0

print(count)
