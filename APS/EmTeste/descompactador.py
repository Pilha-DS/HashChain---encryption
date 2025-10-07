norm = "101010XZ12X0510160103130"
trad = {
    "Z": "0",
    "X": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9"
}

total = []
aux = []

for c in norm:
    if c in ["0", "1"] and not aux:
        total.append(c)
    elif c in ["Z", "X", "2","3","4","5","6","7","8","9"]:
        aux.append(trad[c])
    else:
        total.append(c * int("".join(aux)))
        aux = []
    
for i in total:
    print(len(i))
print("".join(total))
print(norm)
