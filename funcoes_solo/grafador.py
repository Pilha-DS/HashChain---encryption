import gerador_tabelas


#Funcões
def grafar(passes_a_usar:dict, texto_para_grafar:str = "ameixa", passes:list = [0], pre_seed:int = 12345678, limpar:bool = False): #Função que criptografa o texto desejado.

    def pegar_chave_por_index(dicionario, indice): #Função que pega a chae de um dicionario via index.
        return list(dicionario.keys())[indice]

    def pegar_chave_por_valor(dicionario, valor): #Função que pega a chave de um dicionario pelo seu valor.
        for chave, valor_de_pesquisa in dicionario.items():
            if valor_de_pesquisa == valor:
                return chave
            
    def limpar_texto(texto_para_limpar, caracteres_para_manter): #
        return "".join([caracter for caracter in texto_para_limpar if caracter in caracteres_para_manter])

    dicionario_de_passes = passes_a_usar
    texto_grafado = ""
    caracteres_invalidos = ""
    passes_usados = ""
    index_de_controle = 0
    
    if passes != [0]:
        controle_condicional = 0 #Mandando um passe.
        for t in texto_para_grafar:
            if controle_condicional == passes[-1]:
                index_de_controle = 0
                controle_condicional = passes[index_de_controle]
                if t in dicionario_de_passes[controle_condicional]:
                    passes_usados = passes_usados + str(passes[index_de_controle]) + "," + " "
                    texto_grafado = texto_grafado + " " + dicionario_de_passes[controle_condicional][t]
                    index_de_controle += 1
                else:
                    caracteres_invalidos = caracteres_invalidos + t + "," + " "
            else:
                controle_condicional = passes[index_de_controle]
                if t in dicionario_de_passes[controle_condicional]:
                    passes_usados = passes_usados + str(passes[index_de_controle]) + "," + " "
                    texto_grafado = texto_grafado + " " + dicionario_de_passes[controle_condicional][t]
                    index_de_controle += 1
                else:
                    caracteres_invalidos = caracteres_invalidos + t + "," + " "
        else:
            if limpar == True:
                texto_grafado = limpar_texto(texto_grafado, "#*")
            return texto_grafado, passes_usados, caracteres_invalidos, texto_para_grafar, chave_de_controle
                
    else: #Não mandando passe.
        chave_de_controle = (len(dicionario_de_passes))
        for t in texto_para_grafar:
            if index_de_controle == chave_de_controle:
                index_de_controle = 0    
                if t in dicionario_de_passes[pegar_chave_por_index(dicionario_de_passes, index_de_controle)]:
                    passes_usados = passes_usados + str(pegar_chave_por_index(dicionario_de_passes, index_de_controle)) + "," + " "
                    texto_grafado = texto_grafado + " " + dicionario_de_passes[pegar_chave_por_index(dicionario_de_passes, index_de_controle)][t]
                else:
                    caracteres_invalidos = caracteres_invalidos + t + "," + " "
                index_de_controle += 1  
            else:
                if t in dicionario_de_passes[pegar_chave_por_index(dicionario_de_passes, index_de_controle)]:
                    passes_usados = passes_usados + str(pegar_chave_por_index(dicionario_de_passes, index_de_controle)) + "," + " "
                    texto_grafado = texto_grafado +  " " + dicionario_de_passes[pegar_chave_por_index(dicionario_de_passes, index_de_controle)][t]
                else:
                    caracteres_invalidos = caracteres_invalidos + t + "," + " "
                index_de_controle += 1
        else:
            if limpar == True:
                texto_grafado = limpar_texto(texto_grafado, "#*")
            return texto_grafado, passes_usados, caracteres_invalidos, texto_para_grafar, chave_de_controle, pre_seed
while True:
    text_teste = input("Escreva oq quer criptografar: ")
    seed = int(input("Digite a seed: "))
    chaves = gerador_tabelas.gerar_tabelas(seed, 9, 12)
    grafo = grafar(chaves, text_teste, [0], seed, True)

    print(chaves)
    print(f"Texto grafado: ({grafo[-3]}) | Grafo: ({grafo[-6]}) | Caracteres invalídos: ({grafo[-4]}) | Os passes usados são: ({grafo[-5]}) | Seed usada é:{grafo[-1]}")