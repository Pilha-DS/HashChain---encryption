
# ================ IMPORTS NECESSÁRIOS ================#
import random
import os
from tables import gerar_tabelas

# FUNÇÃO PARA GERAR SEED ALEATÓRIA
def gerar_seed_decimal_aleatoria(num_digitos: int = 256) -> int:
    """Gera seed de 256 caracteres por padrão"""
    # Gera bytes aleatórios seguros
    bytes_aleatorios = os.urandom(num_digitos // 2)  # cada byte ≈ 2 dígitos

    # Converte os bytes para inteiro
    large_number = int.from_bytes(bytes_aleatorios, 'big')

    # Formata para garantir exatamente num_digitos
    seed_str = str(large_number).zfill(num_digitos)
    seed_str = seed_str[:num_digitos]

    return int(seed_str)


# FUNÇÃO ENCRYPTER
def encrypter(
    plaintext: str = "",
    pass_: list = [],
    seed: int = 0,
    no_salt: bool = False,
    debug_mode: bool = False,
    min_table_leng: int = 20,
    max_table_leng: int = 100,
) -> list:
    """
    Criptografa texto utilizando tabelas de substituição geradas deterministicamente.
    
    Args:
        plaintext (str): Texto a ser criptografado (obrigatorio)
        dict_tables (dict): Dicionário com tabelas de substituição (opcional)
        pass_ (list): Lista de passes para geração de chave (opcional)
        seed (int): Seed para geração determinística (opcional)
        dict_tables (list): Tabela de substituição (opicional)
        no_salt (bool): Gera o cipher text sem salt (opicional)
        debug_mode (bool): Retornas os valores em modo desenvolvedor a função
        min_table_leng (int): O tamanho minimo da tabela de substituição (opicional). Não pode sere inferior a (20)
        max_table_leng (int): O tamanho maximo da tabela de substituição (opicional). Não pode ultrapassar (999)

    Returns:
        list: Lista contendo [texto cifrado, chave]
    
    Raises:
        ValueError: Se o texto plano não for fornecido
    """
    dict_tables = {}

    cor = {
    "pad" : "\033[0;0m",
    "red" : "\033[1;31m",
    "gre" : "\033[1;32m",
    "blu" : "\033[1;34m",
    "yel" : "\033[1;33m",
    "mag" : "\033[1;35m",
    "cya" : "\033[1;36m",
    }

    # Validação dos parâmetros obrigatórios
    if min_table_leng < 20:
        min_table_leng = 20

    if not plaintext:
        raise ValueError("Parâmetro obrigatório: plaintext deve ser uma string não vazia")

    # Geração de valores padrão se não informados
    if not seed:
        seed = gerar_seed_decimal_aleatoria(256)

    if not pass_:
        p = len(plaintext)
        while p > 1:
            p -= 1
            pass_.append(random.randint(min_table_leng, max_table_leng))

    if not dict_tables:
        dict_tables = gerar_tabelas(seed, pass_)[0]


    # Variáveis principais
    crude_ciphertext_list = []
    salt_ciphertext_list = []
    invalid_characters_list = []
    control_index = 0
    control_key = len(list(dict_tables.keys())) - 1

    # Funções internas auxiliares
    def enciphering(caracter: str) -> None:
        """Mapeia um caractere para a substituição correspondente na tabela"""
        if debug_mode:
            try:
                tabela_atual = dict_tables[get_key_on_index(control_index)]
                crude_ciphertext_list.append(cor["gre"] + tabela_atual[caracter] + cor["pad"])
            except KeyError:
                invalid_characters_list.append(caracter)
        else:
            try:
                tabela_atual = dict_tables[get_key_on_index(control_index)]
                crude_ciphertext_list.append(tabela_atual[caracter])
            except KeyError:
                invalid_characters_list.append(caracter)

    def get_key_on_index(index: int, dict: dict = dict_tables) -> int:
        """Obtém chave pelo índice dentro do dicionário"""
        return list(dict.keys())[index]

    def create_salt(
        ciphertext_list: list = [],
        pass_: list = [],
        seed: int = 0,
        min_leng: int = 20,
        max_leng: int = 100,
    ):
        """Insere salt no ciphertext para aumentar entropia"""
        mini, maxi = min_leng, max_leng
        posicoes = []

        salt_leng = random.randint(20, 20 + len(ciphertext_list))
        salt_ciphertext_list,  = [c for c in ciphertext_list], 

        if debug_mode:
            salt_passes = [cor["gre"] + str(p) + cor["pad"] for p in pass_]
        else:
            salt_passes = [p for p in pass_]

        if debug_mode:
            for _ in range(salt_leng):
                salt_pass = random.randint(mini, maxi)
                posicao = random.randint(0, (len(salt_ciphertext_list) - 1))

                tb = gerar_tabelas(seed, [salt_pass])
                salt_passes.insert(posicao, (cor["red"] + str(salt_pass).zfill(3) + cor["pad"]))
                salt_ciphertext_list.insert(posicao, cor["red"] + tb[0][salt_pass][chr(random.randint(65, 90))] + cor["pad"])
                posicoes.append(cor["yel"] + str(posicao).zfill(10) + cor["pad"])
        else:
            for _ in range(salt_leng):
                salt_pass = random.randint(mini, maxi)
                posicao = random.randint(0, (len(salt_ciphertext_list) - 1))

                tb = gerar_tabelas(seed, [salt_pass])
                salt_passes.insert(posicao, salt_pass)
                salt_ciphertext_list.insert(posicao, tb[0][salt_pass][chr(random.randint(65, 90))])
                posicoes.append(posicao)

        return salt_ciphertext_list, salt_passes, posicoes

    def key_generator(pass_: list = [], seed: int = 0, salt: list = []) -> list:
        """Gera chave polida para descriptografia posterior"""

        crude_passes = [p for p in pass_]
        poli_passes = []
        poli_salt = [str(s).zfill(10) for s in salt] if salt != [] else ''

        for p in crude_passes:
            poli_passes.append(str(p).zfill(3))

        if debug_mode:
            seed_value = cor["cya"] + str(seed) + cor["pad"]
            pl = cor["mag"] + str(len(poli_passes)) + cor["pad"]
            lolp = cor["mag"] + str(len(str(pl))).zfill(3) + cor["pad"]
            sl = cor["mag"] + str(len(str(seed))) + cor["pad"]
            salt_l = [cor["mag"] + str(len(salt)) + cor["pad"]] if poli_salt != '' else ''
            lol_salt = [cor["mag"] + str(len(salt_l[0])).zfill(3) + cor["pad"]] if salt_l != '' else ''
        else:
            seed_value = str(seed)
            pl = str(len(poli_passes))
            lolp = str(len(str(pl))).zfill(3)
            sl = str(len(seed_value))
            salt_l = [str(len(salt))] if poli_salt != '' else ''
            lol_salt = [str(len(salt_l[0])).zfill(3)] if salt_l != '' else ''

        crude_key = (
            f"\nsalt: lol_salt: {', '.join(p for p in lol_salt)}, salt_l: {', '.join(p for p in salt_l)}, \nposições salt: {', '.join(p for p in poli_salt)}\n\n"
            f"passes: lolp: {lolp}, pl: {pl}, \npasses: {', '.join(p for p in poli_passes)}\n\n"
            f"seed: seed: {sl}, seed {seed_value}"
        )

        polished_key = "".join(
            [
                "".join(lol_salt),
                "".join(salt_l),
                "".join(poli_salt),
                "".join(lolp),
                "".join(pl),
                "".join(poli_passes),
                "".join(sl),
                "".join(seed_value),
            ]
        )

        return poli_passes, polished_key, crude_key

    # Processo de criptografia
    for caracter in plaintext:
        enciphering(caracter)
        control_index = 0 if control_index == control_key else control_index + 1

    if not no_salt:
        salt = create_salt(crude_ciphertext_list, pass_, seed, 20, 100)
        salt_ciphertext_list = salt[0]
        ciphertext = "".join(salt_ciphertext_list)
        key = key_generator(salt[1], seed, salt[2])
    else:
        ciphertext = "".join(crude_ciphertext_list)
        key = key_generator(pass_, seed, [])

    # Saída final
    if debug_mode:
        return (
            f"\nPlaintext: {cor["blu"] + plaintext + cor["pad"]}\n\n"
            f"Ciphertext: {', '.join(p for p in salt_ciphertext_list) if not no_salt else ', '.join(p for p in crude_ciphertext_list)}\n\n"
            f"crude key: {key[2]}\n\n"
            f"polished key: {key[1]}\n\n"
            f"Invalid characters: {invalid_characters_list}\n\n"
        )
    else:
        return [ciphertext, key[1]]

# TESTE RÁPIDO
if __name__ == "__main__":
    encry = encrypter(plaintext="axabaci", max_table_leng=600, debug_mode=True, no_salt=False)
    print(encry)
