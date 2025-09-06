import tabelas

seed = 12345678
tables = tabelas.gerar_tabelas(seed, 9, 24)

def desgrafar(entrada: str, tabela: dict, key: list[int] = None):
    cifras = t_invertida = {k: {v: kk for kk, v in d.items()} for k, d in tabela.items()}
    """
    Descriptografa texto do grafador enquanto descompacta cada bloco.
    Se key não for passada, percorre as tabelas na mesma ordem do grafador.
    """
    
    if not cifras:
        return "ERROR: Cifras cannot be empty"
    
    saida = ""
    i = 0
    n = len(entrada)

    # Ordem das tabelas
    if key is None:
        tables_order = list(cifras.keys())
        use_key_order = True
    else:
        tables_order = key
        use_key_order = False

    j = 0  # índice da tabela/key atual

    while i < n:
        # tabela atual
        if use_key_order:
            tabela_atual = tables_order[j % len(tables_order)]
            # tamanho da cifra: pega o tamanho de qualquer cifra na tabela
            tamanho_atual = len(next(iter(cifras[tabela_atual].keys())))
        else:
            tabela_atual = tables_order[j % len(tables_order)]
            tamanho_atual = tabela_atual

        bloco_descomp = ""
        cont = 0

        # ler caracteres e descompactar enquanto forma a cifra
        while cont < tamanho_atual and i < n:
            char = entrada[i]
            i += 1

            # descompacta "enquanto lê"
            if char.isdigit():
                quantidade = int(char)
                if i < n:
                    bloco_descomp += entrada[i] * quantidade
                    i += 1
                    cont += quantidade
            else:
                bloco_descomp += char
                cont += 1

        # consulta na tabela atual
        if tabela_atual in cifras and bloco_descomp in cifras[tabela_atual]:
            saida += cifras[tabela_atual][bloco_descomp]
        else:
            saida += "?"  # caractere desconhecido

        j += 1  # próxima tabela

    return saida


# ------------------------------
# Teste
# ------------------------------  

entrada = "#2*3#2*#2#*#*#*#2*8#3*2#2*3#*2#*#*3#*2#2*2#*##2*3#2*6#"
resultado = desgrafar(entrada=entrada, tabela=tables)
print(f"Entrada compactada: {entrada}")
print(f"Resultado desgrafado: {resultado}")  # esperado: 'abc'
