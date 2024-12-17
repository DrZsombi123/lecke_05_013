import random
szamok = [random.randint(-100, 100) for _ in range(100)]
nagyobb_0 = 0
kisebb_0 = 0
for szam in szamok:
    if szam > 0:
        nagyobb_0 += 1
    elif szam < 0:
        kisebb_0 += 1

if nagyobb_0 > kisebb_0:
    print("Több van a 0-nál nagyobb számbol")
elif kisebb_0 > nagyobb_0:
    print("Több van a 0-nál kisebb számbol.")
else:
    print("A 0-nál nagyobb és kisebb számok száma egyenlő.")
index = -1
for i, szam in enumerate(szamok):
    if szam > 50:
        index = i
        break

if index != -1:
    print(f"Az első 50-től nagyobb szám sorszáma: {index}")
else:
    print("Nincs olyan szám, amely nagyobb lenne, mint 50.")
for i in range(len(szamok) - 1):
    if abs(szamok[i] - szamok[i + 1]) > 120:
        print(f"Van olyan eset: {szamok[i]}, {szamok[i + 1]}")
        break
else:
    print("Nincs olyan eset")
