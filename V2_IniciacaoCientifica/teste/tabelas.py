tables = {}
inverted_tables = {}

def gerar_cifra(seed, tamanho, indice):
    """
    Gera cifra determinística com início e fim aleatórios.
    Remove o padrão fixo de sempre começar e terminar com '#'.
    """
    if tamanho < 1:
        return ""
    
    # Gera um número baseado na seed e índice
    num = seed + indice * 2654435761
    
    cifra = []
    for i in range(tamanho):
        # Usa bits diferentes para cada posição
        bit = (num >> (i * 3)) & 1  # Usa mais bits para mais aleatoriedade
        cifra.append('#' if bit == 0 else '*')
    
    # Embaralha levemente para quebrar padrões visuais
    # (mantém o determinismo porque usa a seed)
    if tamanho > 2:
        # Decide se inverte primeiro e último baseado no bit 16
        if (num >> 16) & 1:
            cifra[0], cifra[-1] = cifra[-1], cifra[0]
        
        # Decide se inverte posições adjacentes baseado no bit 17
        if (num >> 17) & 1 and tamanho > 3:
            cifra[1], cifra[2] = cifra[2], cifra[1]
    
    return ''.join(cifra)

def gerar_tabelas(seed, inicio=9, fim=24, caracteres=None):
    global tables
    global inverted_tables
    
    if not isinstance(seed, int) or seed < 10_000_000:
        raise ValueError("Seed deve ser um número inteiro com no mínimo 8 dígitos.")

    if caracteres is None:
        caracteres = [
            "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t",
            "u","v","w","x","y","z",
            "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T",
            "U","V","W","X","Y","Z",
            "0","1","2","3","4","5","6","7","8","9",
            "!","\"","#","$","%","&","'","(",")","*","+",
            " ",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~"
        ]

    tables_ = {}

    for tamanho in range(inicio, fim+1):
        tabela = {}
        # Gera a cifra dos caracteres usando o índice
        for i, char in enumerate(caracteres):
            tabela[char] = gerar_cifra(seed, tamanho, i)
        tables_[tamanho] = tabela
    
    tables = tables_
    inverted_tables = {k: {v: kk for kk, v in d.items()} for k, d in tables.items()}
    return tables_

# Função para testar a melhoria
def testar_aleatoriedade():
    """Testa a melhoria na aleatoriedade das cifras"""
    seed = 12345678
    gerar_tabelas(seed, 10, 10)  # Gera apenas tamanho 10 para teste
    
    print("🔍 TESTE DE ALEATORIEDADE - Antes vs Depois")
    print("=" * 50)
    
    # Analisa padrões de início e fim
    inicios = {'#': 0, '*': 0}
    fins = {'#': 0, '*': 0}
    
    for char, cifra in tables[10].items():
        primeiro_char = cifra[0]
        ultimo_char = cifra[-1]
        inicios[primeiro_char] += 1
        fins[ultimo_char] += 1
    
    print("Distribuição do PRIMEIRO caractere:")
    print(f"#: {inicios['#']} | *: {inicios['*']}")
    print(f"Ratio: {inicios['#']/inicios['*']:.2f}")
    
    print("\nDistribuição do ÚLTIMO caractere:")
    print(f"#: {fins['#']} | *: {fins['*']}")
    print(f"Ratio: {fins['#']/fins['*']:.2f}")
    
    # Mostra alguns exemplos
    print("\n📋 Exemplos de cifras:")
    exemplos = list(tables[10].items())[:5]
    for char, cifra in exemplos:
        print(f"'{char}' → '{cifra}' (início: '{cifra[0]}', fim: '{cifra[-1]}')")

def main():
    # Testa a melhoria
    testar_aleatoriedade()

if __name__ == "__main__":
    main()