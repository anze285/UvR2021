poteze = [("j", "a"), ("a", "b"), ("b", "j"), ("a", "b"), ("j", "a"),
          ("a", "b"), ("b", "j"), ("a", "b"), ("a", "j"), ("b", "a"),
          ("j", "a"), ("a", "j")]
a = 0
b = 0
for prva, druga in poteze:
    if prva == "j":
        if druga == "a":
            a = 7
        elif druga == "b":
            b = 4
    elif druga == "j":
        if prva == "a":
            a = 0
        elif prva == "b":
            b = 0
    elif prva == "a" and druga == "b":
        if b + a > 4:
            b, a = 4, a - (4 - b)
        else:
            b, a = b + a, 0
    elif prva == "b" and druga == "a":
        if b + a > 7:
            a, b = 7, b - (7 - a)
        else:
            a, b = a + b, 0
    print("a:", a, "b:", b)

stanja = [(7, 0), (3, 4), (3, 0), (0, 3), (7, 3), (6, 4),
          (6, 0), (2, 4), (0, 4), (4, 0), (7, 0), (0, 0)]
a = 0
b = 0
for prvo, drugo in stanja:
    if (a + b) < (prvo + drugo):
        moves = "j"
        if a < prvo:
            moves += " a"
        else:
            moves += " b"
    elif (a + b) > (prvo + drugo):
        if a > prvo:
            moves = "a"
        else:
            moves = "b"
        moves += " j"
    else:
        if prvo > a:
            moves = "b a"
        else:
            moves = "a b"
    a, b = prvo, drugo
    print(moves)


