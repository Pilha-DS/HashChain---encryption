def desgrafar(entrada: str, key: list[int], cifras: dict):

    """
    Descriptografa texto usando o novo sistema de tabelas com início/fim aleatórios.
    
    Args:
        entrada: Texto criptografado (apenas '#' e '*')
        key: Lista de tamanhos das cifras (ex: [10, 12, 9])
        cifras: Dicionário de tabelas {tamanho: {cifra: caractere}}
    
    Returns:
        Texto descriptografado ou mensagem de erro
    """
    saida: str = ""
    aux: str = ""
    repeticoes: int = 0
    j: int = 0
    i: int = 0

    # Verifica se a key está vazia
    if not key:
        return "ERROR: Key cannot be empty"

    # Verifica caracteres inválidos
    for char in entrada:
        if char != "#" and char != "*":
            return "ERROR: Invalid character found - only '#' and '*' allowed"

    # Processa a entrada caractere por caractere
    while i < len(entrada):
        tamanho_atual = key[j]
        
        # Coleta os caracteres para formar uma cifra completa
        while repeticoes < tamanho_atual and i < len(entrada):
            aux += entrada[i]
            repeticoes += 1
            i += 1
        
        # Se coletou uma cifra completa
        if repeticoes == tamanho_atual:
            # Verifica se a cifra existe na tabela
            if tamanho_atual in cifras and aux in cifras[tamanho_atual]:
                saida += cifras[tamanho_atual][aux]
            else:
                # Se não encontrou, tenta encontrar em outros tamanhos
                caractere_encontrado = None
                for tamanho, tabela in cifras.items():
                    if aux in tabela:
                        caractere_encontrado = tabela[aux]
                        break
                
                if caractere_encontrado:
                    saida += caractere_encontrado
                else:
                    saida += "?"  # Caractere desconhecido
            
            # Reseta para a próxima cifra
            aux = ""
            repeticoes = 0
            
            # Avança para a próxima key
            if j == len(key) - 1:
                j = 0
            else:
                j += 1
        else:
            # Caso onde a entrada não é múltipla exata dos tamanhos
            break

    # Processa qualquer resto final
    if aux:
        # Tenta encontrar a cifra parcial em algum tamanho
        encontrado = False
        for tamanho, tabela in cifras.items():
            if aux in tabela:
                saida += tabela[aux]
                encontrado = True
                break
        
        if not encontrado:
            saida += "?"  # Cifra incompleta ou desconhecida

    return saida


# Versão alternativa mais robusta para múltiplos tamanhos de cifra
def desgrafar_avancado(entrada: str, cifras: dict, key: list[int] = None):
    """
    Versão avançada que detecta automaticamente tamanhos de cifra.
    
    Args:
        entrada: Texto criptografado
        cifras: Dicionário de todas as tabelas {tamanho: {cifra: caractere}}
        key: Opcional - lista de tamanhos na ordem específica
    
    Returns:
        Texto descriptografado
    """
    saida = ""
    i = 0
    n = len(entrada)
    
    # Se key foi fornecida, usa ordem específica
    if key:
        j = 0
        while i < n:
            tamanho = key[j]
            if i + tamanho <= n:
                cifra = entrada[i:i+tamanho]
                if tamanho in cifras and cifra in cifras[tamanho]:
                    saida += cifras[tamanho][cifra]
                else:
                    saida += "?"
                i += tamanho
                j = (j + 1) % len(key)
            else:
                saida += "?"  # Cifra incompleta
                break
    else:
        # Tenta detectar automaticamente os tamanhos
        while i < n:
            encontrado = False
            # Tenta todos os tamanhos possíveis, do maior para o menor
            for tamanho in sorted(cifras.keys(), reverse=True):
                if i + tamanho <= n:
                    cifra = entrada[i:i+tamanho]
                    if cifra in cifras[tamanho]:
                        saida += cifras[tamanho][cifra]
                        i += tamanho
                        encontrado = True
                        break
            
            if not encontrado:
                # Se não encontrou cifra válida, avança 1 caractere
                saida += "?"
                i += 1

    return saida


# Função de teste para verificar a compatibilidade
def testar_desgrafar():
    """Testa a função desgrafar com diferentes cenários"""
    
    # Exemplo de tabelas (simulado)
    cifras_exemplo = {
        10: {
            "##***##*##": "a",
            "#********#": "b", 
            "#####**#*#": "c"
        },
        12: {
            "#*###*#####*": "j",
            "*####*##*#*#": "o",
            "*#***#####**": "n"
        }
    }
    
    # Teste 1: Descriptografia simples
    texto_cripto = "##***##*##" + "#********#" + "#####**#*#"
    resultado = desgrafar(texto_cripto, [10, 10, 10], cifras_exemplo)
    print(f"Teste 1 - Entrada: {texto_cripto}")
    print(f"Resultado: '{resultado}' (esperado: 'abc')")
    
    # Teste 2: Com key variada
    texto_cripto2 = "#*###*#####*" + "*####*##*#*#" + "*#***#####**"
    resultado2 = desgrafar(texto_cripto2, [12, 12, 12], cifras_exemplo)
    print(f"\nTeste 2 - Entrada: {texto_cripto2}")
    print(f"Resultado: '{resultado2}' (esperado: 'jon')")
    
    # Teste 3: Com key mista
    texto_cripto3 = "##***##*##" + "#*###*#####*" + "#********#"
    resultado3 = desgrafar(texto_cripto3, [10, 12, 10], cifras_exemplo)
    print(f"\nTeste 3 - Entrada: {texto_cripto3}")
    print(f"Resultado: '{resultado3}' (esperado: 'ajb')")


if __name__ == "__main__":
    testar_desgrafar()