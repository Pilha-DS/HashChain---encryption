import tabelas
seed = 12345678
tables = tabelas.gerar_tabelas(seed, 9, 24)

def grafar(
    texto_para_grafar: str = "",
    tabelas_passes: dict = {},
    passes=None,
    limpar: bool = False,
    pre_seed: int = 0
        ):
    """
    Função que criptografa um texto usando tabelas de substituição.
    
    Parâmetros:
        texto_para_grafar (str): Texto de entrada.
        dicionario_de_tabelas_passes (dict): Dicionário com as tabelas de substituição.
        passes (list|None): Sequência de passes a serem usados. Se None ou [0], percorre todas as tabelas.
        limpar (bool): Se True, mantém apenas caracteres "#" e "*" no resultado.
        pre_seed (int): Valor inicial para seed.
    
    Retorna:
        tuple: (texto_grafado, passes_usados, caracteres_invalidos, texto_original, pre_seed)
    """

    # ------------------------------
    # Funções auxiliares
    # ------------------------------
    def chave_por_index(dicionario, indice):
        """Pega a chave de um dicionário a partir do índice."""
        return list(dicionario.keys())[indice]

    def limpar_texto(texto, caracteres_para_manter):
        """Remove caracteres que não estão na lista de permitidos."""
        return "".join(c for c in texto if c in caracteres_para_manter)

    def compactar(texto: str) -> str:
        if not texto:
            return ""

        texto_compactado = ""
        caracter_anterior = texto[0]
        quantidade_atual = 1

        for caracter_atual in texto[1:]:
            if caracter_atual == caracter_anterior:
                quantidade_atual += 1
            else:
                texto_compactado += f"{quantidade_atual}{caracter_anterior}"
                caracter_anterior = caracter_atual
                quantidade_atual = 1

        # Adiciona o último grupo
        texto_compactado += f"{quantidade_atual}{caracter_anterior}"
        return texto_compactado

    # ------------------------------
    # Validação
    # ------------------------------
    if not tabelas_passes:
        raise TypeError("Tabela de passes está vazia.")

    if passes is None:
        passes = [0]

    # ------------------------------
    # Variáveis de controle
    # ------------------------------
    texto_grafado = ""
    caracteres_invalidos = ""
    passes_usados = ""
    index_de_controle = 0

    # ------------------------------
    # Caso 1: Usuário passou lista de passes
    # ------------------------------
    if passes != [0]:
        controle_condicional = 0
        for t in texto_para_grafar:
            # Se chegamos no fim da lista de passes, volta para o início
            if controle_condicional == passes[-1]:
                index_de_controle = 0

            controle_condicional = passes[index_de_controle]

            if t in tabelas_passes[controle_condicional]:
                passes_usados += str(passes[index_de_controle]) + " "
                texto_grafado += " " + tabelas_passes[controle_condicional][t]
                index_de_controle += 1
            else:
                caracteres_invalidos += t + ", "

    # ------------------------------
    # Caso 2: Não foi passada lista de passes (usa todas as tabelas em ordem)
    # ------------------------------
    else:
        qtd_passes = len(tabelas_passes)

        for t in texto_para_grafar:
            if index_de_controle == qtd_passes:
                index_de_controle = 0

            chave_atual = chave_por_index(tabelas_passes, index_de_controle)

            if t in tabelas_passes[chave_atual]:
                passes_usados += str(chave_atual) + " "
                texto_grafado += " " + tabelas_passes[chave_atual][t]
            else:
                caracteres_invalidos += t + ", "

            index_de_controle += 1

    # ------------------------------
    # Limpeza final (se ativada)
    # ------------------------------
    if limpar:
        texto_grafado = limpar_texto(texto_grafado, "#*")

    return texto_grafado, passes_usados, caracteres_invalidos, texto_para_grafar, pre_seed

print(grafar(texto_para_grafar="ameixa", tabelas_passes=tables, pre_seed=seed))