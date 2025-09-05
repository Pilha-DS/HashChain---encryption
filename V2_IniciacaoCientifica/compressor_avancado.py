# compressor_avancado.py - Compressor otimizado para sequências # e *
import math
from typing import Tuple

def compressor_avancado(entrada: str) -> Tuple[str, float]:
    """
    Compressão avançada com múltiplas técnicas para sequências # e *
    
    Args:
        entrada: String contendo apenas # e *
    
    Returns:
        (dados_comprimidos, taxa_compressao)
    """
    if not entrada:
        return "", 0.0
    
    # Verificar caracteres válidos
    for char in entrada:
        if char not in ['#', '*']:
            raise ValueError("A string deve conter apenas # e *")
    
    # Técnica 1: Compactação binária (mais eficiente)
    comprimido_bin, taxa_bin = _comprimir_binario(entrada)
    
    # Técnica 2: RLE tradicional (para comparação)
    comprimido_rle, taxa_rle = _comprimir_rle(entrada)
    
    # Técnica 3: Compactação por dicionário (para padrões repetitivos)
    comprimido_dict, taxa_dict = _comprimir_dicionario(entrada)
    
    # Escolher a melhor técnica
    tecnicas = [
        (comprimido_bin, taxa_bin, "binário"),
        (comprimido_rle, taxa_rle, "RLE"),
        (comprimido_dict, taxa_dict, "dicionário")
    ]
    
    # Ordenar por melhor taxa de compressão
    tecnicas.sort(key=lambda x: x[1], reverse=True)
    melhor_comprimido, melhor_taxa, tecnica = tecnicas[0]
    
    # Adicionar header indicando a técnica usada
    header = f"{tecnica[0]}"  # Primeira letra da técnica
    resultado_final = header + ":" + melhor_comprimido
    
    return resultado_final, melhor_taxa

def _comprimir_binario(entrada: str) -> Tuple[str, float]:
    """Técnica 1: Compactação binária ultra-eficiente"""
    # Mapear # → 0, * → 1
    bits = []
    for char in entrada:
        bits.append('0' if char == '#' else '1')
    
    binario_str = ''.join(bits)
    
    # Converter para bytes e depois para Base64 customizado
    comprimido = _binario_para_compacto(binario_str)
    
    taxa = (1 - len(comprimido) / len(entrada)) * 100
    return comprimido, max(taxa, 0)

def _binario_para_compacto(binario_str: str) -> str:
    """Converte string binária para formato compacto"""
    # Preencher com zeros para múltiplo de 6
    padding = (6 - len(binario_str) % 6) % 6
    binario_str += '0' * padding
    
    # Converter cada 6 bits em um caractere (64 possibilidades)
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    comprimido = []
    
    for i in range(0, len(binario_str), 6):
        grupo = binario_str[i:i+6]
        valor = int(grupo, 2)
        comprimido.append(caracteres[valor])
    
    # Adicionar informação de padding
    if padding > 0:
        comprimido.append(str(padding))
    
    return ''.join(comprimido)

def _comprimir_rle(entrada: str) -> Tuple[str, float]:
    """Técnica 2: RLE tradicional melhorado"""
    if not entrada:
        return "", 0.0
    
    comprimido = []
    count = 1
    current_char = entrada[0]
    
    for i in range(1, len(entrada)):
        if entrada[i] == current_char:
            count += 1
        else:
            if count > 3 or (count > 1 and current_char == '#'):
                comprimido.append(f"{count}{current_char}")
            else:
                comprimido.append(current_char * count)
            
            current_char = entrada[i]
            count = 1
    
    # Última sequência
    if count > 3 or (count > 1 and current_char == '#'):
        comprimido.append(f"{count}{current_char}")
    else:
        comprimido.append(current_char * count)
    
    resultado = ''.join(comprimido)
    taxa = (1 - len(resultado) / len(entrada)) * 100
    return resultado, max(taxa, 0)

def _comprimir_dicionario(entrada: str) -> Tuple[str, float]:
    """Técnica 3: Compactação por dicionário de padrões"""
    # Identificar padrões comuns
    padroes = {}
    n = len(entrada)
    
    # Procurar padrões de 2 a 8 caracteres
    for tamanho in range(2, 9):
        for i in range(0, n - tamanho + 1):
            padrao = entrada[i:i+tamanho]
            if padrao in padroes:
                padroes[padrao] += 1
            else:
                padroes[padrao] = 1
    
    # Selecionar padrões mais comuns
    padroes_comuns = [p for p, count in padroes.items() if count > 2 and len(p) > 3]
    padroes_comuns.sort(key=len, reverse=True)
    
    if not padroes_comuns:
        return _comprimir_rle(entrada)  # Fallback para RLE
    
    # Criar dicionário de substituição
    dicionario = {}
    substituicoes = {}
    
    for i, padrao in enumerate(padroes_comuns[:10]):  # Limitar a 10 padrões
        codigo = chr(65 + i)  # A, B, C, ...
        dicionario[codigo] = padrao
        substituicoes[padrao] = codigo
    
    # Aplicar substituições
    comprimido = entrada
    for padrao, codigo in substituicoes.items():
        comprimido = comprimido.replace(padrao, f"${codigo}")
    
    # Adicionar dicionário ao resultado
    dict_str = ",".join([f"{k}={v}" for k, v in dicionario.items()])
    resultado = f"DICT:{dict_str}|{comprimido}"
    
    taxa = (1 - len(resultado) / len(entrada)) * 100
    return resultado, max(taxa, 0)

# Descompressor correspondente
def descompressor_avancado(comprimido: str) -> str:
    """
    Descompacta dados comprimidos pelo compressor avançado
    """
    if not comprimido:
        return ""
    
    # Verificar técnica usada
    if ":" in comprimido:
        tecnica, dados = comprimido.split(":", 1)
        
        if tecnica == "b":  # binário
            return _descomprimir_binario(dados)
        elif tecnica == "R":  # RLE
            return _descomprimir_rle(dados)
        elif tecnica == "d":  # dicionário
            return _descomprimir_dicionario(dados)
        elif tecnica == "DICT":  # dicionário completo
            return _descomprimir_dicionario(comprimido)
    
    # Fallback: assumir RLE simples
    return _descomprimir_rle(comprimido)

def _descomprimir_binario(comprimido: str) -> str:
    """Descompacta formato binário"""
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    
    # Verificar se tem informação de padding
    if comprimido[-1].isdigit():
        padding = int(comprimido[-1])
        comprimido = comprimido[:-1]
    else:
        padding = 0
    
    # Converter cada caractere para 6 bits
    binario_str = ""
    for char in comprimido:
        if char in caracteres:
            valor = caracteres.index(char)
            binario_str += format(valor, '06b')
    
    # Remover padding
    if padding > 0:
        binario_str = binario_str[:-padding]
    
    # Converter bits para # e *
    resultado = []
    for bit in binario_str:
        resultado.append('#' if bit == '0' else '*')
    
    return ''.join(resultado)

def _descomprimir_rle(comprimido: str) -> str:
    """Descompacta RLE"""
    resultado = []
    i = 0
    n = len(comprimido)
    
    while i < n:
        if comprimido[i].isdigit():
            # Extrair número
            num_str = ""
            while i < n and comprimido[i].isdigit():
                num_str += comprimido[i]
                i += 1
            
            if i < n and comprimido[i] in ['#', '*']:
                char = comprimido[i]
                resultado.append(char * int(num_str))
                i += 1
            else:
                resultado.append(num_str)
        else:
            resultado.append(comprimido[i])
            i += 1
    
    return ''.join(resultado)

def _descomprimir_dicionario(comprimido: str) -> str:
    """Descompacta formato de dicionário"""
    if comprimido.startswith("DICT:"):
        partes = comprimido.split("|", 1)
        if len(partes) != 2:
            return comprimido
        
        dict_str, dados = partes
        dict_str = dict_str[5:]  # Remover "DICT:"
        
        # Reconstruir dicionário
        dicionario = {}
        for item in dict_str.split(","):
            if "=" in item:
                codigo, padrao = item.split("=", 1)
                dicionario[codigo] = padrao
        
        # Aplicar substituições inversas
        resultado = dados
        for codigo, padrao in dicionario.items():
            resultado = resultado.replace(f"${codigo}", padrao)
        
        return resultado
    
    return comprimido

# Funções utilitárias
def calcular_estatisticas(original: str, comprimido: str) -> dict:
    """Calcula estatísticas detalhadas da compressão"""
    tamanho_original = len(original)
    tamanho_comprimido = len(comprimido)
    taxa_compressao = (1 - tamanho_comprimido / tamanho_original) * 100
    
    return {
        'tamanho_original': tamanho_original,
        'tamanho_comprimido': tamanho_comprimido,
        'taxa_compressao': round(taxa_compressao, 2),
        'bytes_economizados': tamanho_original - tamanho_comprimido,
        'ratio': f"{tamanho_comprimido}:{tamanho_original}"
    }

# Exemplo de uso
if __name__ == "__main__":
    # Teste com diferentes padrões
    testes = [
        "####*****#*#*####***#**###***",
        "##*##*##*##*##*##*##*##*##*",
        "#*#*#*#*#*#*#*#*#*#*#*#*#*#*",
        "##########**********##########",
        "###**###**###**###**###**###**",
        "#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*"
    ]
    
    print("🚀 COMPRESSOR AVANÇADO - TESTES")
    print("=" * 50)
    
    for i, teste in enumerate(testes, 1):
        print(f"\n🔍 Teste {i}:")
        print(f"Original: {teste}")
        
        try:
            comprimido, taxa = compressor_avancado(teste)
            descomprimido = descompressor_avancado(comprimido)
            
            stats = calcular_estatisticas(teste, comprimido)
            
            print(f"Comprimido: {comprimido}")
            print(f"Tamanho: {stats['tamanho_original']} → {stats['tamanho_comprimido']}")
            print(f"Taxa: {stats['taxa_compressao']}%")
            print(f"✅ Integridade: {teste == descomprimido}")
            
            if teste != descomprimido:
                print(f"❌ ERRO: Original e descomprimido diferem!")
                print(f"Original:  {teste}")
                print(f"Descomp:   {descomprimido}")
                
        except Exception as e:
            print(f"❌ Erro: {e}")