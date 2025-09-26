
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
    dict_tables: dict = {},
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
        """Mapeia um caractere para a substituição correspondente"""
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

        salt_leng = random.randint(2, 2 + len(ciphertext_list))
        salt_ciphertext_list, salt_passes = [c for c in ciphertext_list], [p for p in pass_]

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
        seed_value = str(seed)
        crude_passes = [p for p in pass_]
        poli_passes = []
        poli_salt = [str(s).ljust(10, "0") for s in salt] if salt != [] else []

        for p in crude_passes:
            poli_passes.append(str(p).zfill(3))

        pl = str(len(poli_passes))
        lolp = str(len(str(pl))).ljust(3, "0")
        sl = str(len(seed_value))
        salt_l = [str(len(salt))] if poli_salt != None else []
        lol_salt = [str(len(salt_l)).ljust(3, "0")] if salt_l != None else []

        crude_key = (
            f"\nsalt: lol_salt: {lol_salt}, salt_l: {salt_l}, posições salt: {poli_salt}\n"
            f"passes: lolp: {[lolp]}, pl: {[pl]}, passes: {poli_passes}\n"
            f"seed: seed: {[sl]}, seed {[seed_value]}"
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
            f"Plaintext: {plaintext}\n"
            f"Ciphertext: {salt_ciphertext_list if not no_salt else crude_ciphertext_list}\n"
            f"crude key: {key[2]}\n"
            f"polished key: {key[1]}\n"
            f"Invalid characters: {invalid_characters_list}\n"
        )
    else:
        return [ciphertext, key[1]]

# TESTE RÁPIDO
if __name__ == "__main__":
    encry = encrypter(plaintext="axabaci", max_table_leng=600,debug_mode=True, no_salt=False)
    print(encry)
