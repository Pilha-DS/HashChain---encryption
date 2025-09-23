aux = "11111000010001010101010101"
posicao = 0
countHas = 0
countAst = 0
texto = " "

while posicao < len(aux):
    i = aux[posicao]

    if i == "0":
        countAst = 0
        countHas += 1
        if countHas >= 2 and posicao + 1 < len(aux) and aux[posicao + 1] != i:
            texto += str(countHas)
        if posicao + 1 < len(aux) and aux[posicao + 1] != i:
            texto += i

    else:
        countHas = 0
        countAst += 1
        if countAst >= 2 and posicao + 1 < len(aux) and aux[posicao + 1] != i:
            texto += str(countAst)
        if posicao + 1 < len(aux) and aux[posicao + 1] != i:
            texto += i

    posicao += 1

if countHas >= 2:
    texto += str(countHas) + "0"
elif countAst >= 2:
    texto += str(countAst) + "1"

print(texto)
            
