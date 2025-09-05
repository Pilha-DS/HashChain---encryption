texto_para_compactar = "#########*********###***#*"

def compactar(texto_para_comp: str = "###***"):
    texto_compactado = ""
    caracter_anterior = ""
    quantidade_atual = 0
    parte_a_juntar = ""

    for caracter_atual in texto_para_comp:
        if caracter_anterior == "":
            caracter_anterior = caracter_atual

        if caracter_atual == caracter_anterior:
            quantidade_atual += 1
        else:
            if texto_compactado == "":
                parte_a_juntar = str(quantidade_atual) + caracter_anterior
                texto_compactado = parte_a_juntar
                quantidade_atual = 1
            else:
                parte_a_juntar = str(quantidade_atual) + caracter_anterior
                texto_compactado = texto_compactado + parte_a_juntar
                quantidade_atual = 1
            caracter_anterior = caracter_atual

    else:
        parte_a_juntar = str(quantidade_atual) + caracter_anterior
        texto_compactado = texto_compactado + parte_a_juntar
        return texto_compactado

print(f"compacto: {compactar(texto_para_compactar)} / para compactar: {texto_para_compactar}")