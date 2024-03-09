liczby = []

while len(liczby) < 10:
  liczba= int(input("Podaj liczbę: "))
  liczby.append(liczba)

parzyste = []
for i in liczby:
  if i % 2 == 0:
    parzyste.append(i)


print(parzyste)

