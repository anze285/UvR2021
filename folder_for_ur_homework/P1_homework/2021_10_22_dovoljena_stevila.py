#intervali = [tuple(int(x) for x in vrstica.split("-")) for vrstica in open("intervali.txt")]
intervali = [
    (12, 18),
    (2, 5),
    (3, 8),
    (0, 4),
    (15, 19),
    (6, 9),
    (13, 17),
    (4, 8)
]
dovoljena_stevila = [intervali[0]]
for spodnja_meja, zgornja_meja in intervali:
    for majhno, veliko in dovoljena_stevila:
        if spodnja_meja < majhno and zgornja_meja > veliko:
            majhno = spodnja_meja
            veliko = zgornja_meja
        elif spodnja_meja < majhno and zgornja_meja > majhno:
            majhno = spodnja_meja
        else:
            dovoljena_stevila.append((spodnja_meja, zgornja_meja))
            break

print(dovoljena_stevila)