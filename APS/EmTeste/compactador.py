aux = "1010101111111111000000000000000000000111110100000010111000"
posicao = 0
countZero = 0
countUm = 0
texto = ""
caltStr = "10"


while posicao < len(aux):
    i = aux[posicao]

    if i == "0":
        countUm = 0
        countZero += 1
        
        
        if countZero >= 2 and posicao + 1 < len(aux) and aux[posicao + 1] != i:
            caltStr = str(countZero)
            if len(caltStr) == 2:
                if caltStr[0] == "1":
                    if caltStr[1] == "0":
                        texto += "X" + "Z"
                    else:
                        texto += "X" + caltStr[1]
                elif caltStr[1] == "1":
                    texto += caltStr[0] + "X"
                elif caltStr[1] == "0":
                    texto += caltStr[0] + "Z"
            else:
                texto += str(countZero)
        if posicao + 1 < len(aux) and aux[posicao + 1] != i:
            texto += i

    else:
        countZero = 0
        countUm += 1
        
        if countUm >= 2 and posicao + 1 < len(aux) and aux[posicao + 1] != i:
            caltStr = str(countUm)
            if len(caltStr) == 2:
                if caltStr[0] == "1":
                    if caltStr[1] == "0":
                        texto += "X" + "Z"
                    else:
                        texto += "X" + caltStr[1]
                elif caltStr[1] == "1":
                    texto += caltStr[0] + "X"
                elif caltStr[1] == "0":
                    texto += caltStr[0] + "Z"
            else:
                texto += str(countUm)
        if posicao + 1 < len(aux) and aux[posicao + 1] != i:
            texto += i

    posicao += 1

if countZero >= 2:
    texto += str(countZero) + "0"
elif countUm >= 2:
    texto += str(countUm) + "1"

print(texto)
            
