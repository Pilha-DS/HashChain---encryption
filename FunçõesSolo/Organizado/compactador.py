texto_para_compactar = "#########*********###***#*"

def compactar(texto: str = "###***") -> str:
    if not texto:
        return ""
    
    resultado = []
    contador = 1
    anterior = texto[0]

    for atual in texto[1:]:
        if atual == anterior:
            contador += 1
        else:
            resultado.append(f"{contador}{anterior}")
            anterior = atual
            contador = 1
    
    # adiciona o último grupo
    resultado.append(f"{contador}{anterior}")
    return "".join(resultado)

print(f"compacto: {compactar(texto_para_compactar)} / para compactar: {texto_para_compactar}")
