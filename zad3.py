slowo = input("Podaj słowo: ")

start = 0
end = len(slowo) - 1

while start < end:
  if slowo[start] != slowo[end]:
    print("To nie jest palindrom")
    exit()
  start += 1
  end -= 1

print("To jest palindrom")
