import math
import time
from tables import gerar_tabelas
from encrypter import encrypter

def analise_espaco_chaves():
    """Analisa o tamanho do espaço de chaves"""
    print("=== ANÁLISE DO ESPAÇO DE CHAVES ===")
    
    # Seed de 256 dígitos decimais
    digitos_seed = 256
    espaco_total = 10 ** digitos_seed  # 10^256 possibilidades
    bits_entropia = math.log2(espaco_total)
    
    print(f"Tamanho da seed: {digitos_seed} dígitos decimais")
    print(f"Espaço total de chaves: 10^{digitos_seed}")
    print(f"Entropia: {bits_entropia:.2f} bits")
    print(f"Para comparação: AES-256 tem 256 bits de entropia")
    
    # Tempo estimado para força bruta
    tentativas_por_segundo = 1_000_000_000  # 1 bilhão de tentativas/segundo (supercomputador)
    segundos_total = espaco_total / tentativas_por_segundo
    anos_total = segundos_total / (365 * 24 * 3600)
    
    print(f"\nTempo estimado para força bruta:")
    print(f"Assumindo {tentativas_por_segundo:,} tentativas/segundo")
    print(f"Segundos necessários: {segundos_total:.2e}")
    print(f"Anos necessários: {anos_total:.2e}")
    print(f"Idade do universo: ~13.8 bilhões de anos")
    
    return espaco_total

analise_espaco_chaves()