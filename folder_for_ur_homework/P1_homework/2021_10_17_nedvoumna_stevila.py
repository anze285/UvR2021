# 10000 v 98.76771354675293s
nedvoumna_stevila = [1, 2]
i = 2
while i < 10000:
    i += 1
    j = 0
    counter = 0
    while j < len(nedvoumna_stevila) and nedvoumna_stevila[j] < i / 2:
        prvo_stevilo = nedvoumna_stevila[j]
        k = j + 1
        while k < len(nedvoumna_stevila):
            drugo_stevilo = nedvoumna_stevila[k]
            vsota = prvo_stevilo + drugo_stevilo
            if vsota == i:
                counter += 1
            if counter > 1 or vsota > i:
                break
            k += 1
        if counter > 1:
            break
        j += 1
    if counter == 1:
        nedvoumna_stevila.append(i)
print(nedvoumna_stevila)

