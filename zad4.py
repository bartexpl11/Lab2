liczba = int(input("Podaj liczbę: "))

prime = True

if liczba <= 1:
  print("Liczba nie jest pierwsza")
  exit()
elif liczba > 1:
  for i in range(2, liczba):
    if liczba % i == 0:
      prime = False
      break

print("Liczba jest pierwsza" if prime else "Liczba nie jest pierwsza")
