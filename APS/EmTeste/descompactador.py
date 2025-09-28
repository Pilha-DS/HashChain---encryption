norm = "1010107150510160103130"
textF = ""
numb = 0
            
for posicao in norm:
    
    if numb + 1 < len(norm) and norm[numb + 1] != posicao:
        if posicao != "0" and posicao != "1":
            textF += (int(posicao) - 1) * norm[numb + 1]
        else:    
            textF += posicao
    if numb + 1 == len(norm):
        textF += norm[-1]

    numb += 1
    
print(textF)
            
