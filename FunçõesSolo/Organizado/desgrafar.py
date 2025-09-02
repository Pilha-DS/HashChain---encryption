def desgrafar(entrada: str, key: list[int], cifras: dict) -> str:
    saida = ""
    aux = ""
    repeticoes = 0
    j = 0  # índice da key

    for char in entrada:
        # valida se o caractere é permitido
        if char not in {"#", "*"}:
            return "ERRO: caractere inválido encontrado"

        aux += char
        repeticoes += 1

        # chegou no tamanho esperado pela key
        if repeticoes == key[j]:
            try:
                saida += cifras[key[j]][aux]
            except KeyError:
                return f"ERRO: padrão {aux} não encontrado em cifras[{key[j]}]"
            aux = ""
            repeticoes = 0
            j = (j + 1) % len(key)  # volta para 0 quando chega no fim

    # garante que sobras também sejam processadas
    if aux:
        try:
            saida += cifras[key[j]][aux]
        except KeyError:
            return f"ERRO final: padrão {aux} não encontrado em cifras[{key[j]}]"

    return saida
