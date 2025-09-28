aux = "101010111111100000111110100000010111000"
posicao = 0
countZero = 0
countUm = 0
texto = " "

while posicao < len(aux):
    i = aux[posicao]

    if i == "0":
        countUm = 0
        countZero += 1
        if countZero >= 2 and posicao + 1 < len(aux) and aux[posicao + 1] != i:
            texto += str(countZero)
        if posicao + 1 < len(aux) and aux[posicao + 1] != i:
            texto += i

    else:
        countZero = 0
        countUm += 1
        if countUm >= 2 and posicao + 1 < len(aux) and aux[posicao + 1] != i:
            texto += str(countUm)
        if posicao + 1 < len(aux) and aux[posicao + 1] != i:
            texto += i

    posicao += 1

if countZero >= 2:
    texto += str(countZero) + "0"
elif countUm >= 2:
    texto += str(countUm) + "1"

print(texto)
            
