# ================ IMPORTS NECESSÁRIOS ================#
import random
import os
from typing import List, Tuple, Optional, Union
from tables import gerar_tabelas

# Constantes para melhor manutenibilidade
DEFAULT_SEED_DIGITS = 256
MIN_TABLE_LENGTH = 20
MAX_TABLE_LENGTH = 100
SALT_LENGTH_RANGE = (20, 20)  # Base + offset

# Códigos de cores ANSI
COLORS = {
    "pad": "\033[0;0m",
    "red": "\033[1;31m",
    "gre": "\033[1;32m",
    "blu": "\033[1;34m",
    "yel": "\033[1;33m",
    "mag": "\033[1;35m",
    "cya": "\033[1;36m",
}

def gerar_seed_decimal_aleatoria(num_digitos: int = DEFAULT_SEED_DIGITS) -> int:
    """Gera seed de 256 caracteres por padrão"""
    bytes_aleatorios = os.urandom(num_digitos // 2)  # cada byte ≈ 2 dígitos
    large_number = int.from_bytes(bytes_aleatorios, 'big')
    seed_str = str(large_number).zfill(num_digitos)[:num_digitos]
    return int(seed_str)

def _gerar_tabelas_por_passe(pass_: List[int], seed: int, min_table_leng: int, max_table_leng: int) -> Tuple[dict, List[int]]:
    """Gera tabelas únicas para cada passe baseado na seed principal"""
    seeds_por_passe = []
    dict_tables_por_passe = {}
    
    random.seed(seed)
    for i, passe in enumerate(pass_):
        seed_passe = seed + (i * 1000000) + passe
        seeds_por_passe.append(seed_passe)
        
        dict_tables_passe = gerar_tabelas(seed_passe, [passe])[0]
        dict_tables_por_passe[passe] = dict_tables_passe[passe]
    
    random.seed()  # Restaura estado aleatório
    return dict_tables_por_passe, seeds_por_passe

def _gerar_passes_automaticos(plaintext: str, min_table_leng: int, max_table_leng: int) -> List[int]:
    """Gera passes automáticos baseados no comprimento do texto"""
    return [random.randint(min_table_leng, max_table_leng) for _ in range(len(plaintext) - 1, 0, -1)]

def _processar_caracter(caracter: str, passe_atual: int, tabelas: dict, debug_mode: bool, invalid_chars: list) -> str:
    """Processa um caractere individual para criptografia"""
    try:
        cipher_char = tabelas[passe_atual][caracter]
        return COLORS["gre"] + cipher_char + COLORS["pad"] if debug_mode else cipher_char
    except KeyError:
        invalid_chars.append(caracter)
        return ""

def _criar_salt(ciphertext_list: List[str], current_pass: List[int], current_seed: int, 
                min_table_leng: int, max_table_leng: int, debug_mode: bool) -> Tuple[List[str], List[int], List[str]]:
    """Insere salt no ciphertext para aumentar entropia"""
    salt_ciphertext = ciphertext_list.copy()
    salt_passes = current_pass.copy()
    posicoes = []
    
    salt_leng = SALT_LENGTH_RANGE[0] + len(ciphertext_list)
    random.seed(current_seed)
    
    for salt_index in range(salt_leng):
        salt_pass = random.randint(min_table_leng, max_table_leng)
        posicao = random.randint(0, len(salt_ciphertext) - 1)
        
        seed_salt = current_seed + (salt_index * 100000) + salt_pass + posicao
        tabela_salt = gerar_tabelas(seed_salt, [salt_pass])[0]
        random_char = chr(random.randint(65, 90))
        
        if debug_mode:
            salt_passes.insert(posicao, COLORS["red"] + str(salt_pass).zfill(3) + COLORS["pad"])
            salt_ciphertext.insert(posicao, COLORS["red"] + tabela_salt[salt_pass][random_char] + COLORS["pad"])
            posicoes.extend([COLORS["cya"] + str(len(str(posicao))).zfill(3) + COLORS["pad"],
                           COLORS["yel"] + str(posicao) + COLORS["pad"]])
        else:
            salt_passes.insert(posicao, salt_pass)
            salt_ciphertext.insert(posicao, tabela_salt[salt_pass][random_char])
            posicoes.extend([str(len(str(posicao))).zfill(3), str(posicao)])
    
    random.seed()  # Restaura estado aleatório
    return salt_ciphertext, salt_passes, posicoes

def _gerar_chave(passes_list: List[int], current_seed: int, debug_mode: bool, 
                seeds_passes: Optional[List[int]] = None, 
                salt_positions: Optional[List[str]] = None, 
                padding: str = '') -> Tuple[List[str], str, str]:
    """Gera chave polida para descriptografia"""
    seeds_passes = seeds_passes or []
    salt_positions = salt_positions or []
    
    # Prepara componentes da chave
    poli_passes = [str(p).zfill(3) for p in passes_list]
    poli_seeds = [str(s).zfill(20) for s in seeds_passes]
    poli_salt = [str(s) for s in salt_positions]
    
    seed_value = str(current_seed)
    pl = str(len(poli_passes))
    lolp = str(len(pl)).zfill(3)
    sl = str(len(seed_value)).zfill(3)
    
    # Informações sobre seeds e salt
    seeds_l = str(len(seeds_passes))
    lol_seeds = str(len(seeds_l)).zfill(3)
    
    salt_l = [str(len(salt_positions) // 2)] if poli_salt else []
    lol_salt = [str(len(salt_l[0])).zfill(3)] if salt_l else []

    # Aplica cores se estiver em debug mode
    if debug_mode:
        seed_value = COLORS["blu"] + seed_value + COLORS["pad"]
        pl = COLORS["mag"] + pl + COLORS["pad"]
        lolp = COLORS["mag"] + lolp + COLORS["pad"]
        sl = COLORS["mag"] + sl + COLORS["pad"]
        salt_l = [COLORS["mag"] + s + COLORS["pad"] for s in salt_l]
        lol_salt = [COLORS["mag"] + s + COLORS["pad"] for s in lol_salt]
        poli_passes = [COLORS["gre"] + p + COLORS["pad"] for p in poli_passes]
        poli_seeds = [COLORS["yel"] + p + COLORS["pad"] for p in poli_seeds]
        poli_salt = [COLORS["red"] + p + COLORS["pad"] for p in poli_salt]

    # Gera chave detalhada (apenas para debug)
    crude_key = (
        f"\nseed principal: {seed_value}\n\n"
        f"salt: lol_salt: {', '.join(lol_salt)}, salt_l: {', '.join(salt_l)}, \n"
        f"posições salt: {', '.join(poli_salt)}\n\n"
        f"passes: lolp: {lolp}, pl: {pl}, \n"
        f"passes: {', '.join(poli_passes)}\n\n"
        f"padding: {padding}"
    )

    # Gera chave polida (para uso real)
    polished_key = "".join([
        "".join(lol_salt),
        "".join(salt_l),
        "".join(poli_salt),
        lolp,
        pl,
        "".join(poli_passes),
        sl,
        seed_value,
        padding
    ])
    
    return poli_passes, polished_key, crude_key

def _aplicar_padding(ciphertext: str) -> Tuple[str, str]:
    """Aplica padding ao ciphertext se necessário"""
    padding_needed = (20 - (len(ciphertext) % 20)) % 20
    if padding_needed > 0:
        return ciphertext + "1" * padding_needed, str(padding_needed)
    return ciphertext, ""

def encrypter(
    plaintext: str = "",
    pass_: Optional[List[int]] = None,
    seed: int = 0,
    no_salt: bool = False,
    debug_mode: bool = False,
    min_table_leng: int = MIN_TABLE_LENGTH,
    max_table_leng: int = MAX_TABLE_LENGTH,
) -> Union[List[str], str]:
    """
    Criptografa texto utilizando tabelas de substituição geradas deterministicamente.

    Args:
        plaintext (str): Texto a ser criptografado (obrigatorio)
        pass_ (list): Lista de passes para geração de chave (opcional)
        seed (int): Seed para geração determinística (opcional)
        no_salt (bool): Gera o cipher text sem salt (opcional)
        debug_mode (bool): Retornas os valores em modo desenvolvedor a função
        min_table_leng (int): O tamanho minimo da tabela de substituição (opcional). Não pode sere inferior a (20)
        max_table_leng (int): O tamanho maximo da tabela de substituição (opcional). Não pode ultrapassar (999)

    Returns:
        list: Lista contendo [texto cifrado, chave]

    Raises:
        ValueError: Se o texto plano não for fornecido
    """
    # Validações iniciais
    if not plaintext:
        raise ValueError("Parâmetro obrigatório: plaintext deve ser uma string não vazia")
    
    min_table_leng = max(min_table_leng, MIN_TABLE_LENGTH)
    max_table_leng = min(max_table_leng, MAX_TABLE_LENGTH)
    
    # Inicialização de parâmetros
    pass_ = pass_ or _gerar_passes_automaticos(plaintext, min_table_leng, max_table_leng)
    seed = seed or gerar_seed_decimal_aleatoria(DEFAULT_SEED_DIGITS)
    
    # Geração de tabelas
    dict_tables_por_passe, seeds_por_passe = _gerar_tabelas_por_passe(
        pass_, seed, min_table_leng, max_table_leng
    )
    
    # Processo de criptografia principal
    crude_ciphertext = []
    invalid_characters = []
    control_key = len(pass_) - 1
    
    for i, caracter in enumerate(plaintext):
        passe_atual = pass_[i % len(pass_)] if control_key > 0 else pass_[0]
        cipher_char = _processar_caracter(
            caracter, passe_atual, dict_tables_por_passe, debug_mode, invalid_characters
        )
        if cipher_char:
            crude_ciphertext.append(cipher_char)
    
    # Aplicação do salt e geração da chave
    if not no_salt:
        salt_result = _criar_salt(
            crude_ciphertext, pass_, seed, min_table_leng, max_table_leng, debug_mode
        )
        ciphertext_final, salt_passes, salt_positions = salt_result
        ciphertext_str = "".join(ciphertext_final)
        ciphertext_str, padding = _aplicar_padding(ciphertext_str)
        
        key_result = _gerar_chave(
            passes_list=salt_passes,
            current_seed=seed,
            debug_mode=debug_mode,
            seeds_passes=seeds_por_passe,
            salt_positions=salt_positions,
            padding=padding
        )
    else:
        ciphertext_str = "".join(crude_ciphertext)
        ciphertext_str, padding = _aplicar_padding(ciphertext_str)
        
        key_result = _gerar_chave(
            passes_list=pass_,
            current_seed=seed,
            debug_mode=debug_mode,
            seeds_passes=seeds_por_passe,
            padding=padding
        )
    
    # Saída final
    if debug_mode:
        ciphertext_display = ', '.join(crude_ciphertext) if no_salt else ', '.join(salt_result[0])
        return (
            f"\nPlaintext: {COLORS['blu'] + plaintext + COLORS['pad']}\n\n"
            f"Ciphertext_list: {ciphertext_display}\n\n"
            f"Seeds por passe: {seeds_por_passe}\n\n"
            f"Crude key: {key_result[2]}\n\n"
            f"Polished key: {key_result[1]}\n\n"
            f"Invalid characters: {invalid_characters}\n\n"
            f"Ciphertext: {ciphertext_str}\n\n"
        )
    else:
        return [ciphertext_str, key_result[1]]

enc = encrypter(plaintext='O mika ainda vai apanhar dos muleke da sala.')

print(enc)