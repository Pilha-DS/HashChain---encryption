from tabelas import tables

#Funcões
def grafar(text_to_crip: str, copia_passes:dict,  passes:list = [0], ):

    def pegar_chave_por_index(dicionario, indice):
        return list(dicionario.keys())[indice]

    def pegar_chave_por_valor(dicionario, valor):
        for chave, val in dicionario.items():
            if val == valor:
                return chave
            
    def limpar_grifo(texto, manter):
        return "".join([c for c in texto if c in manter])

    passes_para_usar = copia_passes
    texto_grafado = ""
    caracteres_invalidos = ""
    passes_usados = ""
    pre_index = 0
    
    if passes != [0]:
    #Mandando o passe.
        index_do_passe = 0
        for t in text_to_crip:
            if index_do_passe == passes[-1]:
                pre_index = 0
                index_do_passe = passes[pre_index]
                if t in passes_para_usar[index_do_passe]:
                    passes_usados = passes_usados + str(passes[pre_index]) + "," + " "
                    texto_grafado = texto_grafado + passes_para_usar[index_do_passe][t]
                    pre_index += 1
                else:
                    caracteres_invalidos = caracteres_invalidos + t + "," + " "
            else:
                index_do_passe = passes[pre_index]
                if t in passes_para_usar[index_do_passe]:
                    passes_usados = passes_usados + str(passes[pre_index]) + "," + " "
                    texto_grafado = texto_grafado + passes_para_usar[index_do_passe][t]
                    pre_index += 1
                else:
                    caracteres_invalidos = caracteres_invalidos + t + "," + " "
        else:
            return f"Texto grafado: {text_to_crip} : Grafo: {texto_grafado} : Caracteres invalídos ({caracteres_invalidos}) : Os passes usados são: ({passes_usados})"
        
    #Não mandando o passe.
    else:
        keyboard = (len(passes_para_usar))
        print (f"keyboard: {keyboard}")
        for t in text_to_crip:
            if pre_index == keyboard:
                pre_index = 0    
                if t in passes_para_usar[pegar_chave_por_index(passes_para_usar, pre_index)]:
                    passes_usados = passes_usados + str(pegar_chave_por_index(passes_para_usar, pre_index)) + "," + " "
                    texto_grafado = texto_grafado + passes_para_usar[pegar_chave_por_index(passes_para_usar, pre_index)][t]
                else:
                    caracteres_invalidos = caracteres_invalidos + t + "," + " "
                pre_index += 1  
            else:
                if t in passes_para_usar[pegar_chave_por_index(passes_para_usar, pre_index)]:
                    passes_usados = passes_usados + str(pegar_chave_por_index(passes_para_usar, pre_index)) + "," + " "
                    texto_grafado = texto_grafado + passes_para_usar[pegar_chave_por_index(passes_para_usar, pre_index)][t]
                else:
                    caracteres_invalidos = caracteres_invalidos + t + "," + " "
                pre_index += 1
        else:
            texto_grafado = limpar_grifo(texto_grafado, "#*")
            return f"Texto grafado: {text_to_crip} : Grafo: {texto_grafado} : Caracteres invalídos ({caracteres_invalidos}) : Os passes usados são: ({passes_usados})"

while True:
    t_text = input("Escreva oque quer criptografar: ")
    print(grafar)