import itertools

class AdvancedCryptoAnalyzer:
    def __init__(self):
        self.common_seeds = [
            12345678, 87654321, 11111111, 22222222, 33333333, 44444444,
            55555555, 66666666, 77777777, 88888888, 99999999, 10000000,
            12341234, 43214321, 12121212, 23232323, 34343434, 45454545,
            56565656, 67676767, 78787878, 89898989, 12344321, 11223344
        ]
    
    def gerar_cifra(self, seed: int, tamanho: int, indice: int) -> str:
        """Gera cifra determinística com seed + índice"""
        if tamanho < 2:
            return "#" * tamanho

        num = seed + indice * 2654435761
        meio = []
        
        for i in range(tamanho - 2):
            bit = (num >> i) & 1
            meio.append('#' if bit == 0 else '*')
        
        return '#' + ''.join(meio) + '#'
    
    def encontrar_possiveis_tamanhos(self, texto_criptografado):
        """Encontra possíveis tamanhos de bloco analisando padrões de #"""
        possiveis_tamanhos = set()
        
        # Encontrar todas as posições onde começa um bloco (# após não-# ou início)
        inicios = [0]
        for i in range(1, len(texto_criptografado)):
            if texto_criptografado[i] == '#' and texto_criptografado[i-1] != '#':
                inicios.append(i)
        
        # Calcular diferenças entre inícios como possíveis tamanhos
        for i in range(1, len(inicios)):
            tamanho = inicios[i] - inicios[i-1]
            if 8 <= tamanho <= 24:  # Faixa razoável baseada na sua nota
                possiveis_tamanhos.add(tamanho)
        
        # Também considerar do último início até o final
        ultimo_tamanho = len(texto_criptografado) - inicios[-1]
        if 8 <= ultimo_tamanho <= 24:
            possiveis_tamanhos.add(ultimo_tamanho)
        
        return sorted(possiveis_tamanhos)
    
    def dividir_em_blocos(self, texto_criptografado, tamanho):
        """Divide o texto em blocos do tamanho especificado"""
        blocos = []
        for i in range(0, len(texto_criptografado), tamanho):
            bloco = texto_criptografado[i:i+tamanho]
            if len(bloco) == tamanho:  # Apenas blocos completos
                blocos.append(bloco)
        return blocos
    
    def analisar_blocos(self, blocos):
        """Analisa padrões nos blocos"""
        print(f"\n📊 Análise dos {len(blocos)} blocos:")
        for i, bloco in enumerate(blocos):
            num_hash = bloco.count('#')
            num_star = bloco.count('*')
            print(f"Bloco {i+1}: '{bloco}' → {num_hash} #, {num_star} *")
    
    def tentar_descriptografar_com_seed(self, blocos, seed, caracteres_testar="abc"):
        """Tenta descriptografar com uma seed específica"""
        resultado = []
        
        for i, bloco in enumerate(blocos):
            tamanho = len(bloco)
            encontrado = False
            
            # Testar para cada caractere possível
            for j, char in enumerate(caracteres_testar):
                cifra_gerada = self.gerar_cifra(seed, tamanho, j)
                if cifra_gerada == bloco:
                    resultado.append(char)
                    encontrado = True
                    break
            
            if not encontrado:
                resultado.append('?')
        
        return ''.join(resultado)
    
    def encontrar_seed_por_forca_bruta(self, blocos, caracteres_esperados="abc", max_tentativas=1000):
        """Tenta encontrar a seed por força bruta limitada"""
        print(f"\n🔎 Buscando seed para {len(blocos)} blocos...")
        
        melhores_resultados = []
        
        # Primeiro testar seeds comuns
        for seed in self.common_seeds:
            resultado = self.tentar_descriptografar_com_seed(blocos, seed, caracteres_esperados)
            if '?' not in resultado:
                melhores_resultados.append((seed, resultado))
                print(f"✅ Seed {seed}: '{resultado}'")
        
        # Se não encontrou com seeds comuns, tentar um range limitado
        if not melhores_resultados:
            print("🧪 Testando seeds aleatórias...")
            for tentativa in range(min(max_tentativas, 10000)):
                seed = 10000000 + tentativa  # Seeds de 8 dígitos
                resultado = self.tentar_descriptografar_com_seed(blocos, seed, caracteres_esperados)
                if '?' not in resultado:
                    melhores_resultados.append((seed, resultado))
                    print(f"✅ Seed {seed}: '{resultado}'")
                    if len(melhores_resultados) >= 3:  # Limitar resultados
                        break
        
        return melhores_resultados
    
    def analisar_criptografia(self, texto_criptografado, texto_original=None):
        """Análise completa da criptografia"""
        print("🔍 ANÁLISE AVANÇADA DE CRIPTOGRAFIA")
        print("=" * 60)
        print(f"Criptografia: {texto_criptografado}")
        print(f"Tamanho: {len(texto_criptografado)} caracteres")
        print("=" * 60)
        
        # Passo 1: Encontrar possíveis tamanhos de bloco
        possiveis_tamanhos = self.encontrar_possiveis_tamanhos(texto_criptografado)
        print(f"📏 Possíveis tamanhos de bloco: {possiveis_tamanhos}")
        
        resultados = []
        
        # Testar cada tamanho possível
        for tamanho in possiveis_tamanhos:
            print(f"\n🧪 TESTANDO TAMANHO {tamanho}:")
            
            # Dividir em blocos
            blocos = self.dividir_em_blocos(texto_criptografado, tamanho)
            self.analisar_blocos(blocos)
            
            # Tentar encontrar a seed
            if texto_original and len(blocos) == len(texto_original):
                melhores_seeds = self.encontrar_seed_por_forca_bruta(blocos, texto_original)
            else:
                # Se não sabemos o texto original, testar com letras comuns
                melhores_seeds = self.encontrar_seed_por_forca_bruta(blocos, "abcdefghijklmnopqrstuvwxyz")
            
            for seed, resultado in melhores_seeds:
                resultados.append((tamanho, seed, resultado))
                print(f"🎯 Tamanho {tamanho}, Seed {seed}: '{resultado}'")
        
        return resultados

# Testar com a criptografia fornecida
if __name__ == "__main__":
    analyzer = AdvancedCryptoAnalyzer()
    
    texto_criptografado = "##******##****#*#*#######**#*#"
    
    print("🧪 ANALISANDO: ##******##****#*#*#######**#*#")
    print("=" * 70)
    
    # Primeiro, vamos supor que seja "abc" como nos exemplos anteriores
    resultados = analyzer.analisar_criptografia(texto_criptografado, "abc")
    
    print(f"\n🎯 RESULTADOS ENCONTRADOS:")
    for tamanho, seed, resultado in resultados:
        print(f"• Tamanho {tamanho}, Seed {seed}: '{resultado}'")
    
    # Se não encontrou com "abc", tentar sem saber o texto original
    if not resultados:
        print("\n🔎 Tentando sem texto original conhecido...")
        resultados = analyzer.analisar_criptografia(texto_criptografado)
        
        print(f"\n🎯 POSSÍVEIS RESULTADOS:")
        for tamanho, seed, resultado in resultados:
            print(f"• Tamanho {tamanho}, Seed {seed}: '{resultado}'")