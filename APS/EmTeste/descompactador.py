norm = "4#5*#*#*4#3*#2*3#3*"
textF = ""
numb = 0

for posicao, i in enumerate(norm):
    if i.isdigit():
        numb = int(str(numb) + i) if numb else int(i)

        if posicao + 1 < len(norm) and norm[posicao + 1].isdigit():
            continue

        if posicao + 1 < len(norm):
            textF += norm[posicao + 1] * (numb - 1)

        numb = 0
    else:
        if numb == 0:
            textF += i

print(textF)
            
