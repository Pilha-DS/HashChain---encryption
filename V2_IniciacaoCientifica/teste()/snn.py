# SNEU-UC - Sistema de Numeração Exponencial Universal Ultra-Compacto
# Versão para Windows (sem shebang Unix)

import math

# Constantes globais
BASE62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
PRECISAO_PADRAO = 12

# ==================== FUNÇÕES BASE62 ====================

def criar_mapa_base62():
    """Cria mapa de caracteres Base62"""
    mapa = {}
    for indice, char in enumerate(BASE62):
        mapa[char] = indice
    return mapa

BASE62_MAPA = criar_mapa_base62()

def inteiro_para_base62(numero):
    """Converte número inteiro para string Base62"""
    if numero == 0:
        return BASE62[0]
    
    resultado = []
    n = numero
    while n > 0:
        n, resto = divmod(n, 62)
        resultado.append(BASE62[resto])
    
    return ''.join(reversed(resultado))

def base62_para_inteiro(base62_str):
    """Converte string Base62 para número inteiro"""
    resultado = 0
    for char in base62_str:
        resultado = resultado * 62 + BASE62_MAPA[char]
    return resultado

# ==================== FUNÇÕES PRINCIPAIS ====================

def sneu_compactar(numero, precisao=PRECISAO_PADRAO):
    """
    Compacta um número para formato SNEU-UC
    """
    # Caso especial: zero
    if numero == 0:
        return "0"
    
    # Extrair sinal
    sinal = "-" if numero < 0 else ""
    numero_abs = abs(numero)
    
    # Calcular magnitude e coeficiente
    if numero_abs < 1e-100:
        magnitude = -100
        coeficiente = numero_abs * (10 ** 100)
    else:
        magnitude = math.floor(math.log10(numero_abs))
        coeficiente = numero_abs / (10 ** magnitude)
    
    # Codificar magnitude
    if magnitude < 0:
        magnitude_cod = BASE62[magnitude + 100]  # Offset para negativos
    elif magnitude < 62:
        magnitude_cod = BASE62[magnitude]
    else:
        # Magnitude grande: usar dois caracteres
        high = magnitude // 62
        low = magnitude % 62
        magnitude_cod = BASE62[high] + BASE62[low]
    
    # Codificar precisão
    precisao_cod = BASE62[precisao]
    
    # Codificar coeficiente
    coeficiente_inteiro = round(coeficiente * (10 ** precisao))
    coeficiente_cod = inteiro_para_base62(coeficiente_inteiro)
    
    return f"{sinal}{magnitude_cod}{precisao_cod}{coeficiente_cod}"

def sneu_descompactar(codigo):
    """
    Descompacta código SNEU-UC para número
    """
    # Caso especial: zero
    if codigo == "0":
        return 0.0
    
    # Verificar tamanho mínimo
    if len(codigo) < 3:
        raise ValueError("Código SNEU-UC inválido")
    
    # Extrair sinal
    sinal = -1 if codigo[0] == "-" else 1
    codigo_sem_sinal = codigo[1:] if codigo[0] == "-" else codigo
    
    # Determinar tamanho da magnitude
    primeiro_char = codigo_sem_sinal[0]
    if primeiro_char in BASE62 and BASE62_MAPA[primeiro_char] >= 50:
        # Magnitude negativa (usando offset)
        magnitude_cod = codigo_sem_sinal[0]
        resto_codigo = codigo_sem_sinal[1:]
    else:
        # Verificar se magnitude tem 1 ou 2 caracteres
        if len(codigo_sem_sinal) >= 2 and codigo_sem_sinal[1] in BASE62:
            segundo_char = codigo_sem_sinal[1]
            if BASE62_MAPA[segundo_char] < 10:  # Provavelmente parte da magnitude
                magnitude_cod = codigo_sem_sinal[0:2]
                resto_codigo = codigo_sem_sinal[2:]
            else:
                magnitude_cod = codigo_sem_sinal[0]
                resto_codigo = codigo_sem_sinal[1:]
        else:
            magnitude_cod = codigo_sem_sinal[0]
            resto_codigo = codigo_sem_sinal[1:]
    
    # Extrair precisão e coeficiente
    if len(resto_codigo) < 2:
        raise ValueError("Código SNEU-UC incompleto")
    
    precisao_cod = resto_codigo[0]
    coeficiente_cod = resto_codigo[1:]
    
    # Decodificar magnitude
    if len(magnitude_cod) == 1:
        magnitude_val = BASE62_MAPA[magnitude_cod]
        if magnitude_val >= 50:  # Magnitude negativa com offset
            magnitude = magnitude_val - 100
        else:
            magnitude = magnitude_val
    else:
        high = BASE62_MAPA[magnitude_cod[0]]
        low = BASE62_MAPA[magnitude_cod[1]]
        magnitude = high * 62 + low
    
    # Decodificar precisão
    precisao = BASE62_MAPA[precisao_cod]
    
    # Decodificar coeficiente
    coeficiente_inteiro = base62_para_inteiro(coeficiente_cod)
    coeficiente = coeficiente_inteiro / (10 ** precisao)
    
    # Reconstruir número
    return sinal * coeficiente * (10 ** magnitude)

def calcular_eficiencia(numero_original, codigo_compactado):
    """Calcula taxa de compactação"""
    str_original = str(numero_original)
    return {
        'original': len(str_original),
        'compactado': len(codigo_compactado),
        'taxa': len(str_original) / len(codigo_compactado),
        'reducao_percentual': (1 - len(codigo_compactado) / len(str_original)) * 100
    }

# ==================== EXEMPLOS DE USO ====================
# Adicione este código ao final do arquivo sneu_uc.py

def teste_numero_gigante():
    """Teste específico para o número enorme"""
    numero_gigante = 111312112314212322132112141312131254221412241214112324131213121314126314132123142213121312141214431214221321221412141113121411133214111316
    
    print("=" * 70)
    print("TESTE SNEU-UC COM NÚMERO GIGANTE")
    print("=" * 70)
    
    print(f"Número original: {numero_gigante}")
    print(f"Tamanho original: {len(str(numero_gigante))} dígitos")
    print()
    
    # Compactar
    compactado = sneu_compactar(numero_gigante)
    print(f"Compactado: {compactado}")
    print(f"Tamanho compactado: {len(compactado)} caracteres")
    print()
    
    # Calcular eficiência
    eficiencia = calcular_eficiencia(numero_gigante, compactado)
    print(f"Taxa de compactação: {eficiencia['taxa']:.2f}:1")
    print(f"Redução: {eficiencia['reducao_percentual']:.1f}%")
    print()
    
    # Descompactar
    descompactado = sneu_descompactar(compactado)
    print(f"Descompactado: {descompactado}")
    print()
    
    # Verificar precisão
    if numero_gigante == descompactado:
        print("✅ PRECISÃO ABSOLUTA - Números idênticos!")
    else:
        erro = abs(numero_gigante - descompactado)
        erro_relativo = erro / numero_gigante
        print(f"❌ ERRO: {erro}")
        print(f"Erro relativo: {erro_relativo:.2e}")
    
    print("=" * 70)

# Executar o teste
if __name__ == "__main__":
    # main()  # Comente esta linha se já existir
    teste_numero_gigante()