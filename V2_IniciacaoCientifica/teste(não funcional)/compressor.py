import time

def carregar_unicode():
    """Carrega o conteúdo do arquivo Unicode"""
    start_load = time.perf_counter()
    with open("09-9-25/unicode_full.txt", "r", encoding="utf_8") as file:
        content = file.read(1_048_576)
    end_load = time.perf_counter()
    return content, end_load - start_load

# Configurações iniciais
symbols = str.maketrans("01", "#*")
reverse_symbols = str.maketrans("#*", "01")

# Carrega o conteúdo e mede o tempo de carregamento
content, tempo_carregamento = carregar_unicode()

def char_to_binary(char):
    """Converte um caractere para sua representação binária"""
    try:
        index = content.index(char)
        return f"{index:0{20}b}".translate(symbols)
    except ValueError:
        return None

def binary_to_char(binary):
    """Converte uma representação binária de volta para o caractere"""
    try:
        clean_binary = binary.translate(reverse_symbols)
        index = int(clean_binary, 2)
        if index < len(content):
            return content[index]
        else:
            return None
    except ValueError:
        return None

def converter_texto_para_binario(texto):
    """Converte texto completo para binário"""
    start_time = time.perf_counter()
    resultados = []
    
    for char in texto:
        binario = char_to_binary(char)
        if binario is not None:
            resultados.append(binario)
        else:
            resultados.append(f"[ERRO: '{char}' não encontrado]")
    
    end_time = time.perf_counter()
    return resultados, end_time - start_time

def converter_binario_para_texto(lista_binarios):
    """Converte lista de binários de volta para texto"""
    start_time = time.perf_counter()
    resultados = []
    
    for binario in lista_binarios:
        if len(binario) == 20 and all(c in "#*" for c in binario):
            char = binary_to_char(binario)
            if char is not None:
                resultados.append(char)
            else:
                resultados.append(f"[ERRO: Binário inválido '{binario}']")
        else:
            resultados.append(f"[ERRO: Formato inválido '{binario}']")
    
    end_time = time.perf_counter()
    return resultados, end_time - start_time

# Loop principal para interação com o usuário
print(f"Tempo de carregamento do arquivo: {tempo_carregamento:.7f} segundos")

while True:
    print("\n" + "="*70)
    print("CONVERSOR UNICODE - BINÁRIO (MÚLTIPLOS CARACTERES)")
    print("="*70)
    print("1. Converter texto para binário")
    print("2. Converter binário para texto")
    print("3. Converter caractere único para binário")
    print("4. Converter binário único para caractere")
    print("5. Teste de performance")
    print("6. Sair")
    print("="*70)
    
    opcao = input("Escolha uma opção (1-6): ").strip()
    
    if opcao == "1":
        # Converter texto completo para binário
        texto_input = input("Digite o texto para converter: ").strip()
        
        if len(texto_input) == 0:
            print("Por favor, digite algum texto.")
            continue
        
        start_total = time.perf_counter()
        resultados, tempo_conversao = converter_texto_para_binario(texto_input)
        end_total = time.perf_counter()
        
        print(f"\n╔{'═'*60}╗")
        print(f"║ {'RESULTADO - TEXTO PARA BINÁRIO':^58} ║")
        print(f"╠{'═'*60}╣")
        print(f"║ Texto original: {texto_input:<43} ║")
        print(f"╠{'═'*60}╣")
        
        for i, (char, binario) in enumerate(zip(texto_input, resultados)):
            print(f"║ {i+1:2d}. '{char}' → {binario:<20} ║")
        
        print(f"╠{'═'*60}╣")
        print(f"║ Caracteres convertidos: {len(resultados):<36} ║")
        print(f"║ Tempo conversão: {tempo_conversao:>38.7f}s ║")
        print(f"║ Tempo total: {(end_total - start_total):>41.7f}s ║")
        print(f"╚{'═'*60}╝")
        
    elif opcao == "2":
        # Converter binário para texto
        print("Digite os códigos binários (20 caracteres cada, com # e *)")
        print("Separe com espaços ou digite um por linha (ENTER para finalizar):")
        
        binarios_input = []
        while True:
            linha = input().strip()
            if linha == "":
                break
            # Separa por espaços se houver múltiplos na mesma linha
            partes = linha.split()
            binarios_input.extend(partes)
        
        if len(binarios_input) == 0:
            print("Nenhum código binário foi informado.")
            continue
        
        start_total = time.perf_counter()
        resultados, tempo_conversao = converter_binario_para_texto(binarios_input)
        end_total = time.perf_counter()
        
        print(f"\n╔{'═'*60}╗")
        print(f"║ {'RESULTADO - BINÁRIO PARA TEXTO':^58} ║")
        print(f"╠{'═'*60}╣")
        
        texto_final = ''.join([str(r) for r in resultados])
        print(f"║ Texto resultante: {texto_final:<43} ║")
        print(f"╠{'═'*60}╣")
        
        for i, (binario, char) in enumerate(zip(binarios_input, resultados)):
            print(f"║ {i+1:2d}. {binario:<20} → '{char}' ║")
        
        print(f"╠{'═'*60}╣")
        print(f"║ Códigos convertidos: {len(resultados):<37} ║")
        print(f"║ Tempo conversão: {tempo_conversao:>38.7f}s ║")
        print(f"║ Tempo total: {(end_total - start_total):>41.7f}s ║")
        print(f"╚{'═'*60}╝")
        
    elif opcao == "3":
        # Converter caractere único para binário (modo antigo)
        char_input = input("Digite o caractere Unicode: ").strip()
        
        if len(char_input) == 0:
            print("Por favor, digite um caractere.")
            continue
            
        start_total = time.perf_counter()
        resultado = char_to_binary(char_input[0])
        end_total = time.perf_counter()
        
        tempo_conversao = end_total - start_total
        
        print(f"\n╔{'═'*40}╗")
        print(f"║ {'RESULTADO - CARACTERE ÚNICO':^38} ║")
        print(f"╠{'═'*40}╣")
        print(f"║ Caractere: {char_input[0]:>26} ║")
        print(f"║ Binário: {resultado if resultado else 'ERRO':>28} ║")
        print(f"║ Tempo total: {tempo_conversao:>22.7f}s ║")
        print(f"╚{'═'*40}╝")
        
    elif opcao == "4":
        # Converter binário único para caractere (modo antigo)
        bin_input = input("Digite o código binário (20 caracteres com # e *): ").strip()
        
        if len(bin_input) != 20:
            print("Erro: O código binário deve ter exatamente 20 caracteres.")
            continue
            
        if not all(c in "#*" for c in bin_input):
            print("Erro: Use apenas os caracteres # e *.")
            continue
        
        start_total = time.perf_counter()
        resultado = binary_to_char(bin_input)
        end_total = time.perf_counter()
        
        tempo_conversao = end_total - start_total
        
        print(f"\n╔{'═'*40}╗")
        print(f"║ {'RESULTADO - BINÁRIO ÚNICO':^38} ║")
        print(f"╠{'═'*40}╣")
        print(f"║ Binário: {bin_input:>28} ║")
        print(f"║ Caractere: {resultado if resultado else 'ERRO':>26} ║")
        print(f"║ Tempo total: {tempo_conversao:>22.7f}s ║")
        print(f"╚{'═'*40}╝")
        
    elif opcao == "5":
        # Teste de performance com múltiplos caracteres
        print("\n╔{'═'*50}╗")
        print("║ {'TESTE DE PERFORMANCE COM MÚLTIPLOS CARACTERES':^48} ║")
        print("╠{'═'*50}╣")
        
        texto_teste = "Hello! 你好! 123 ABC çãó é€ 🐍★"
        print(f"║ Texto de teste: {texto_teste:<30} ║")
        print(f"║ {'─'*48} ║")
        
        # Teste de ida (texto → binário)
        start_ida = time.perf_counter()
        binarios, tempo_ida = converter_texto_para_binario(texto_teste)
        end_ida = time.perf_counter()
        
        # Teste de volta (binário → texto)
        start_volta = time.perf_counter()
        texto_reconstruido, tempo_volta = converter_binario_para_texto(binarios)
        end_volta = time.perf_counter()
        
        texto_final = ''.join(texto_reconstruido)
        
        print(f"║ Original: {texto_teste:<36} ║")
        print(f"║ Reconstruído: {texto_final:<34} ║")
        print(f"║ Correto? {'SIM' if texto_teste == texto_final else 'NÃO':<38} ║")
        print(f"║ {'─'*48} ║")
        print(f"║ Tempo ida: {tempo_ida:>38.7f}s ║")
        print(f"║ Tempo volta: {tempo_volta:>37.7f}s ║")
        print(f"║ Total: {(end_volta - start_ida):>41.7f}s ║")
        print(f"║ Velocidade: {len(texto_teste)/(end_volta - start_ida):>35.0f} chars/s ║")
        print(f"╚{'═'*50}╝")
        
    elif opcao == "6":
        print("Saindo do programa...")
        break
        
    else:
        print("Opção inválida! Escolha 1, 2, 3, 4, 5 ou 6.")

# Tempo total do programa
tempo_total = time.perf_counter() - tempo_carregamento
print(f"\nTempo total de execução do programa: {tempo_total:.7f} segundos")