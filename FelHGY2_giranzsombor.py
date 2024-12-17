varosok = ["Debrecen", "Karcag", "Szolnok", "Szeged", "Miskolc"]
varos = input("Adj meg egy városnevet: ")
if varos in varosok:
    index = varosok.index(varos)
    if index < len(varosok) - 1:
        print(f"A következő város: {varosok[index + 1]}")
    else:
        print("Nincs következő város!")
else:
    varosok.append(varos)
    print(f"A város hozzáadva a listához: {varos}")