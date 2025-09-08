import tabelas
from grafador import grafar
import random
from desgrafar import desgrafar
from compressor_avancado import compressor_avancado, descompressor_avancado

def pular_linha():
    print(" ")

def obter_input_numerico(mensagem, tipo=int):
    """Obtém input numérico com tratamento de erro"""
    while True:
        try:
            return tipo(input(mensagem))
        except ValueError:
            print("❌ Erro: Digite um número válido!")

def processar_passos(passor):
    """Processa string de passos para lista de inteiros"""
    pas = []
    passo = []
    for c in passor:
        if c != " ":
            pas.append(c)
        elif c == " ":
            if pas:  # Só adiciona se não estiver vazio
                passo.append(int("".join(pas)))
                pas.clear()
    if pas:  # Adiciona o último passo
        passo.append(int("".join(pas)))
    return passo

def obter_seed_automatica():
    """Gera uma seed automática de 8 dígitos"""
    return random.randint(10_000_000, 99_999_999)

def calcular_limites_passos(passo):
    """Calcula menor e maior passo da lista"""
    if not passo:
        return 0, 0
    return min(passo), max(passo)

# Dicionário de ações possíveis
possiveis_acoes = {
    "dcri": {"d", "D", "Descriptografar", "descriptografar", "Desgrafar", "desgrafar"},
    "crip": {"c", "C", "Criptografar", "criptografar", "Grafar", "grafar"},
    "comp": {"Compactar", "compactar", "com", "Com", "COM"},
    "desc": {"Descompactar", "descompactar", "des", "Des", "DES"},
    "sim": {"sim", "SIM", "Sim", "s", "S"},
    "nao": {"NAO", "NÃO", "Não", "Nao", "nao", "não", "N", "n"},
    "auto": {"a", "A", "Auto", "auto", "automatica", "Automatica", "AUTO"},
    "manual": {"M", "m", "Manual", "manual", "MANUAL"}
}

while True:
    # Variáveis resetadas a cada loop
    seed = 0
    passo = []
    texto_mod = ""
    acao = ""
    menor_passo = 999
    maior_passo = 0

    # Menu principal
    print('=' * 60)
    print('ESCOLHA UMA AÇÃO:')
    print('[c] Criptografar')
    print('[d] Descriptografar') 
    print('[com] Compactar')
    print('[des] Descompactar')
    print('[q] Sair')
    print('=' * 60)
    
    acao = input("Escolha: ").strip()
    pular_linha()
    
    # Opção de saída
    if acao.lower() in {'q', 'quit', 'exit', 'sair'}:
        print("👋 Saindo...")
        break
    
    # CRIPTOGRAFAR
    if acao in possiveis_acoes["crip"]:
        texto_mod = input("Texto para criptografar: ").strip()
        pular_linha()

        # Configurar seed
        print("Usar seed personalizada?")
        print('[s] Sim | [n] Não (gerar automaticamente)')
        escolha_seed = input("Escolha: ").strip()
        pular_linha()

        if escolha_seed in possiveis_acoes["sim"]:
            seed = obter_input_numerico("Digite a seed (8+ dígitos): ")
        else:
            seed = obter_seed_automatica()
            print(f"🔐 Seed gerada automaticamente: {seed}")
        pular_linha()

        # Configurar passos
        print("Usar passos personalizados?")
        print('[s] Sim | [n] Não (usar padrão)')
        escolha_passos = input("Escolha: ").strip()
        pular_linha()

        if escolha_passos in possiveis_acoes["sim"]:
            passor = input('Digite os passos separados por espaço (ex: "9 21 11"): ').strip()
            passo = processar_passos(passor)
        else:
            passo = [0]
        
        print(f"📋 Passos configurados: {passo}")
        pular_linha()

        # Calcular limites dos passos
        if passo != [0]:
            menor_passo, maior_passo = calcular_limites_passos(passo)
        else:
            # Usar range padrão se não houver passos específicos
            menor_passo, maior_passo = 9, 24

        # Gerar tabelas
        try:
            tabela = tabelas.gerar_tabelas(seed, menor_passo, maior_passo)
            print("✅ Tabelas geradas com sucesso!")
        except Exception as e:
            print(f"❌ Erro ao gerar tabelas: {e}")
            continue
        pular_linha()
        
        # Criptografar
        try:
            resultado = grafar(texto_mod, tabela, passo, True, seed)
            texto_cripto, passes_usados, chars_invalidos, texto_original, seed_final = resultado
            
            print("🎉 CRIPTOGRAFIA BEM-SUCEDIDA!")
            print(f"📝 Texto original: {texto_original}")
            print(f"🔒 Texto criptografado: {texto_cripto}")
            print(f"🔑 Seed utilizada: {seed_final}")
            print(f"🛣️  Passos usados: {passes_usados}")
            
            if chars_invalidos:
                print(f"⚠️  Caracteres inválidos ignorados: {chars_invalidos}")
                
        except Exception as e:
            print(f"❌ Erro durante a criptografia: {e}")
        pular_linha()

    # DESCRIPTOGRAFAR
    elif acao in possiveis_acoes["dcri"]:
        texto_mod = input("Texto para descriptografar: ").strip()
        pular_linha()
        
        print("Modo de descriptografia:")
        print('[a] Automático (detectar tamanhos)')
        print('[m] Manual (informar seed e passos)')
        modo = input("Escolha: ").strip()
        pular_linha()

        if modo in possiveis_acoes["auto"]:
            # Modo automático - tenta detectar
            try:
                # Gera tabelas com range padrão para teste
                tabela_teste = tabelas.gerar_tabelas(12345678, 9, 24)
                t_invertida = {k: {v: kk for kk, v in d.items()} for k, d in tabela_teste.items()}
                
                # Tenta descriptografar com detecção automática
                desgrafo = desgrafar(texto_mod, [0], t_invertida)
                print(f"🔓 Texto descriptografado: {desgrafo}")
                
            except Exception as e:
                print(f"❌ Erro na descriptografia automática: {e}")
                
        elif modo in possiveis_acoes["manual"]:
            # Modo manual
            seed = obter_input_numerico("Digite a seed: ")
            passor = input('Digite os passos separados por espaço: ').strip()
            passo = processar_passos(passor)
            pular_linha()

            menor_passo, maior_passo = calcular_limites_passos(passo)
            
            try:
                tabela = tabelas.gerar_tabelas(seed, menor_passo, maior_passo)
                t_invertida = {k: {v: kk for kk, v in d.items()} for k, d in tabela.items()}
                
                desgrafo = desgrafar(texto_mod, passo, t_invertida)
                print(f"🔓 Texto descriptografado: {desgrafo}")
                
            except Exception as e:
                print(f"❌ Erro na descriptografia: {e}")
        pular_linha()

    # COMPACTAR
    elif acao in possiveis_acoes["comp"]:
        texto_mod = input("Texto para compactar (apenas # e *): ").strip()
        pular_linha()
        
        try:
            comprimido, taxa = compressor_avancado(texto_mod)
            print("✅ COMPACTAÇÃO BEM-SUCEDIDA!")
            print(f"📦 Texto compactado: {comprimido}")
            print(f"📊 Taxa de compressão: {taxa:.2f}%")
            print(f"📏 Tamanho original: {len(texto_mod)}")
            print(f"📐 Tamanho compactado: {len(comprimido)}")
            
        except Exception as e:
            print(f"❌ Erro na compactação: {e}")
        pular_linha()

    # DESCOMPACTAR
    elif acao in possiveis_acoes["desc"]:
        texto_mod = input("Texto para descompactar: ").strip()
        pular_linha()
        
        try:
            descomprimido = descompressor_avancado(texto_mod)
            print("✅ DESCOMPACTAÇÃO BEM-SUCEDIDA!")
            print(f"📦 Texto descompactado: {descomprimido}")
            print(f"📏 Tamanho: {len(descomprimido)} caracteres")
            
        except Exception as e:
            print(f"❌ Erro na descompactação: {e}")
        pular_linha()

    else:
        print("❌ Opção inválida! Tente novamente.")
        pular_linha()