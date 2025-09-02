def grafar(
    texto_para_grafar: str = "",
    dicionario_de_tabelas_passes: dict = {},
    passes=None,
    limpar: bool = False,
    pre_seed: int = 0
):
    """
    Função que criptografa o texto desejado.

    Retorna:
        (texto_grafado, passes_usados, caracteres_invalidos, texto_original, pre_seed)
    """

    # Funções auxiliares
    def pegar_chave_por_index(dicionario, indice):
        """Pega a chave de um dicionário pelo índice."""
        return list(dicionario.keys())[indice]

    def limpar_texto(texto, caracteres_para_manter):
        """Remove todos os caracteres não permitidos do texto."""
        return "".join([c for c in texto if c in caracteres_para_manter])

    # Se não tem tabela de passes -> erro
    if not dicionario_de_tabelas_passes:
        raise TypeError("Tabela de passes está vazia.")

    # Se passes não for passado, inicializa como lista vazia
    if passes is None:
        passes = [0]

    # Variáveis principais
    texto_grafado = []
    caracteres_invalidos = []
    passes_usados = []
    index_de_controle = 0

    # -----------------------------
    # MODO 1: usuário mandou passes
    # -----------------------------
    if passes != [0]:
        controle_condicional = 0
        for t in texto_para_grafar:
            if controle_condicional == passes[-1]:
                index_de_controle = 0
                controle_condicional = passes[index_de_controle]

            if t in dicionario_de_tabelas_passes[controle_condicional]:
                passes_usados.append(str(passes[index_de_controle]))
                texto_grafado.append(dicionario_de_tabelas_passes[controle_condicional][t])
                index_de_controle += 1
            else:
                caracteres_invalidos.append(t)

        resultado = "".join(texto_grafado)
        if limpar:
            resultado = limpar_texto(resultado, "#*")

        return resultado, ", ".join(passes_usados), ", ".join(caracteres_invalidos), texto_para_grafar, pre_seed

    # -----------------------------
    # MODO 2: sem passes definidos
    # -----------------------------
    chave_de_controle = len(dicionario_de_tabelas_passes)
    for t in texto_para_grafar:
        if index_de_controle == chave_de_controle:
            index_de_controle = 0

        chave_atual = pegar_chave_por_index(dicionario_de_tabelas_passes, index_de_controle)

        if t in dicionario_de_tabelas_passes[chave_atual]:
            passes_usados.append(str(chave_atual))
            texto_grafado.append(dicionario_de_tabelas_passes[chave_atual][t])
        else:
            caracteres_invalidos.append(t)

        index_de_controle += 1

    resultado = "".join(texto_grafado)
    if limpar:
        resultado = limpar_texto(resultado, "#*")

    return resultado, ", ".join(passes_usados), ", ".join(caracteres_invalidos), texto_para_grafar, pre_seed
