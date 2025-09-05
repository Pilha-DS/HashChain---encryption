def desgrafar(entrada: str, key: list[int], cifras):

    saida: str = ""
    aux: str = ""
    repeticoes: int = 0
    j: int = 0

    for i, char in enumerate(entrada):
        if char != "#" and char != "*":
            return "FATAL ERROR: 963, Invalid character found"
        if repeticoes == key[j]:
            saida += cifras[key[j]][aux]
            aux = ""
            repeticoes = 0
            if j == len(key) - 1:
                j = 0
            else:
                j += 1
        aux += char
        repeticoes += 1
        # print(aux, "\n", repeticoes, "\n")
    saida += cifras[key[j]][aux]

    print(saida)
    return saida