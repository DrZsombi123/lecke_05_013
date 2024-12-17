mondatok = []
for i in range(5):
    mondat = input(f"Írd be a {i+1}. mondatot: ")
    mondatok.append(mondat)
max_szokoz = -1
max_mondat = ""
for mondat in mondatok:
    szokozok_szama = mondat.count(' ')
    if szokozok_szama > max_szokoz:
        max_szokoz = szokozok_szama
        max_mondat = mondat
print("A legtöbb szóközt tartalmazó mondat:")
print(max_mondat)