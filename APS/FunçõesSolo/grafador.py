#Funcão
def grafar(texto_para_grafar:str = "", dicionario_de_tabelas_passes:dict = {}, passes = 0, limpar:bool = False, pre_seed:int = 00000000): #Função que criptografa o texto desejado.

    # funcoes
    def pegar_chave_por_index(dicionario, indice): #Função que pega a chae de um dicionario via index.
        return list(dicionario.keys())[indice] 

    def pegar_chave_por_valor(dicionario, valor): #Função que pega a chave de um dicionario pelo seu valor.
        for chave, valor_de_pesquisa in dicionario.items():
            if valor_de_pesquisa == valor:
                return chave
            
    def limpar_texto(texto_para_limpar, caracteres_para_manter): #Função para limpar um texto.
        return "".join([caracter for caracter in texto_para_limpar if caracter in caracteres_para_manter])

    if dicionario_de_tabelas_passes != {}:
        # variaveis
        texto_grafado = ""
        caracteres_invalidos = ""
        passes_usados = ""
        index_de_controle = 0
        
        # fluxo
        if passes != [0]: # mandando passe
            controle_condicional = 0 
            for t in texto_para_grafar:
                if controle_condicional == passes[-1]:
                    index_de_controle = 0
                    controle_condicional = passes[index_de_controle]
                    if t in dicionario_de_tabelas_passes[controle_condicional]:
                        passes_usados = passes_usados + str(passes[index_de_controle]) + " "
                        texto_grafado = texto_grafado + " " + dicionario_de_tabelas_passes[controle_condicional][t]
                        index_de_controle += 1
                    else:
                        caracteres_invalidos = caracteres_invalidos + t + "," + " "
                else:
                    controle_condicional = passes[index_de_controle]
                    if t in dicionario_de_tabelas_passes[controle_condicional]:
                        passes_usados = passes_usados + str(passes[index_de_controle]) + " "
                        texto_grafado = texto_grafado + " " + dicionario_de_tabelas_passes[controle_condicional][t]
                        index_de_controle += 1
                    else:
                        caracteres_invalidos = caracteres_invalidos + t + "," + " "
            else:
                if limpar == True:
                    texto_grafado = limpar_texto(texto_grafado, "#*")
                return texto_grafado, passes_usados, caracteres_invalidos, texto_para_grafar, pre_seed
                    
        else: # nao mandando passe.
            chave_de_controle = (len(dicionario_de_tabelas_passes))
            for t in texto_para_grafar:
                if index_de_controle == chave_de_controle:
                    index_de_controle = 0    
                    if t in dicionario_de_tabelas_passes[pegar_chave_por_index(dicionario_de_tabelas_passes, index_de_controle)]:
                        passes_usados = passes_usados + str(pegar_chave_por_index(dicionario_de_tabelas_passes, index_de_controle)) + " "
                        texto_grafado = texto_grafado + " " + dicionario_de_tabelas_passes[pegar_chave_por_index(dicionario_de_tabelas_passes, index_de_controle)][t]
                    else:
                        caracteres_invalidos = caracteres_invalidos + t + "," + " "
                    index_de_controle += 1  
                else:
                    if t in dicionario_de_tabelas_passes[pegar_chave_por_index(dicionario_de_tabelas_passes, index_de_controle)]:
                        passes_usados = passes_usados + str(pegar_chave_por_index(dicionario_de_tabelas_passes, index_de_controle)) + " "
                        texto_grafado = texto_grafado +  " " + dicionario_de_tabelas_passes[pegar_chave_por_index(dicionario_de_tabelas_passes, index_de_controle)][t]
                    else:
                        caracteres_invalidos = caracteres_invalidos + t + "," + " "
                    index_de_controle += 1
            else:
                if limpar == True:
                    texto_grafado = limpar_texto(texto_grafado, "#*")
                print(f"texto_grafado (funcao): {texto_grafado}")
                return texto_grafado, passes_usados, caracteres_invalidos, texto_para_grafar, pre_seed

    else:
        raise TypeError("Tabela de passes esta vazia.")