tables = {}
inverted_tables = {}

def gerar_cifra(seed: int, tamanho: int, indice: int) -> str:
    """
    Gera cifra determinística.
    - Sempre começa e termina com '#'
    - O meio é calculado bit a bit, usando seed + índice
    """
    if tamanho < 2:
        raise ValueError("O tamanho da cifra deve ser >= 2")

    num = seed + indice * 2654435761  # constante para espalhar bits
    meio = []

    for i in range(tamanho - 2):
        bit = (num >> i) & 1
        meio.append('#' if bit == 0 else '*')

    return '#' + ''.join(meio) + '#'


def gerar_tabelas(seed: int, inicio: int = 9, fim: int = 24, caracteres: list[str] | None = None) -> dict:
    """
    Gera dicionário de tabelas de cifra.
    
    Args:
        seed: número base (>= 8 dígitos)
        inicio: tamanho mínimo da cifra
        fim: tamanho máximo da cifra
        caracteres: lista de caracteres a cifrar (default = alfanumérico + símbolos comuns)

    Returns:
        dict: {tamanho: {caractere: cifra}}
    """
    global tables, inverted_tables

    if not isinstance(seed, int) or seed < 10_000_000:
        raise ValueError("Seed deve ser um inteiro com no mínimo 8 dígitos.")

    if caracteres is None:
        caracteres = [
            *"abcdefghijklmnopqrstuvwxyz",
            *"ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            *"0123456789",
            "!\"#$%&'()*+",
            " ,-.\/:;<=>?@[\\]^_`{|}~"
        ]
        # como a string acima inclui blocos, precisamos expandir:
        caracteres = list("".join(caracteres))

    tables_ = {}
    for tamanho in range(inicio, fim + 1):
        tabela = {char: gerar_cifra(seed, tamanho, i) for i, char in enumerate(caracteres)}
        tables_[tamanho] = tabela

    tables = tables_
    inverted_tables = {tam: {cifra: char for char, cifra in d.items()} for tam, d in tables.items()}

    return tables_


def main():
    seed = 12345678
    gerar_tabelas(seed)

    print("Exemplo de cifra:")
    print("Caractere 'a' em tamanho 9:", tables[9]['a'])
    print("Inverso:", inverted_tables[9][tables[9]['a']])


if __name__ == "__main__":
    main()
