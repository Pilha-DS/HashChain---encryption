aux = "####*****#*#*####***#**###***"
posicao = 0
countHas = 0
countAst = 0
texto = " "

while posicao < len(aux):
    i = aux[posicao]

    if i == "#":
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
    texto += str(countHas) + "#"
elif countAst >= 2:
    texto += str(countAst) + "*"

print(texto)
            
