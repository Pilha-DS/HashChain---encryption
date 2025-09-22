# Imports
from tables import gerar_tabelas
import random
import os

def gerar_seed_decimal_aleatoria(num_digitos: int = 256) -> int:
    """
    Gera uma seed numérica criptograficamente segura com o número especificado de dígitos.
    
    Args:
        num_digitos (int): Número de dígitos decimais desejados para a seed (padrão: 256)
    
    Returns:
        int: Seed numérica com exatamente num_digitos dígitos
    """
    # Gera bytes aleatórios criptograficamente seguros
    bytes_aleatorios = os.urandom(num_digitos // 2)  # Cada byte representa aproximadamente 2 dígitos decimais
    
    # Converte os bytes para um inteiro de precisão arbitrária
    large_number = int.from_bytes(bytes_aleatorios, 'big')
    
    # Formata para garantir exatamente num_digitos dígitos
    seed_str = str(large_number).zfill(num_digitos)
    seed_str = seed_str[:num_digitos]  # Garante o comprimento exato
    
    return int(seed_str)

def encrypter(plaintext:str = "",
              dict_tables:dict = {},
              pass_:list = [],
              min_table_leng:int = 20,
              max_table_leng:int = 999,
              no_salt:bool = False,
              seed:int = 0,
             ) -> list:
    """
    Criptografa texto utilizando tabelas de substituição geradas deterministicamente.
    
    Args:
        plaintext (str): Texto a ser criptografado
        dict_tables (dict): Dicionário com tabelas de substituição (opcional)
        pass_ (list): Lista de passes para geração de chave (opcional)
        seed (int): Seed para geração determinística (opcional)
    
    Returns:
        list: Lista contendo [texto cifrado, chave, caracteres inválidos]
    
    Raises:
        ValueError: Se o texto plano não for fornecido
    """
    
    # Validação dos parâmetros de entrada
    if not plaintext: 
        raise ValueError('Parâmetro obrigatório: plaintext deve ser uma string não vazia')
    
    # Geração de valores padrão para parâmetros opcionais
    if not seed:
        seed = gerar_seed_decimal_aleatoria(256)
    
    if not pass_:
        # Gera passes aleatórios baseados no comprimento do texto
        p = len(plaintext)
        while p > 1:
            p -= 1
            pass_.append(random.randint(min_table_leng, max_table_leng))
    
    if not dict_tables:
        # Gera tabelas de substituição usando a seed e passes fornecidos
        dict_tables = gerar_tabelas(seed, pass_)[0]
    
    # Variáveis de estado do processo de criptografia
    ciphertext_list = []
    ciphertext_list_with_salt = []
    invalid_characters_list = []
    key = []
    control_index = 0
    control_key = len(list(dict_tables.keys())) - 1

    def enciphering(caracter:str) -> None:
        try:
            # Obtém a substituição da tabela apropriada
            tabela_atual = dict_tables[get_key_on_index(control_index)]
            ciphertext_list.append(tabela_atual[caracter])
        except KeyError:
            # Registra caracteres não mapeados nas tabelas
            invalid_characters_list.append(caracter)
    
    def get_key_on_index(index:int, dict:dict = dict_tables) -> int:
        return list(dict.keys())[index]
    
    def create_salt(list_ciphertext:list = None):
        if not list_ciphertext:
            raise ValueError("Erro")
        salt_key = []
        pa = []
        list_salt_ciphertext = [n for n in list_ciphertext]

        mac = random.randint(4, 5 + len(list_ciphertext))
        sacra = mac
        while sacra > 1:
            sacra -= 1
            pa.append(random.randint(min_table_leng, max_table_leng))
        tab = gerar_tabelas(seed, pa)
        for n in range((mac - 1)):
            list_salt_ciphertext.insert(random.randint(0, len(list_ciphertext)), tab[0][pa[n]]["A"])

        salt_key = [pa, mac - 1]
        return {"salt" : list_salt_ciphertext, "salt_key" : salt_key}

    def key_generator(pass_:list, seed_value:int, salt:list) -> list:
        passes = [g for g in pass_]
        crude_key = []
        
        # Formata os passes para terem 3 dígitos cada
        for p in passes:
            crude_pass = str(p).zfill(3)
            crude_key.append(crude_pass)
        
        # Calcula metadados para incorporação na chave
        comprimento_total = len(''.join(crude_key))
        digitos_comprimento = len(str(comprimento_total))
        
        # Combina todos os componentes para formar a chave
        s_key = [
            ''.join(crude_key),
            str(seed_value),
            str(comprimento_total),
            str(digitos_comprimento)
        ]
        
        supra_key = [passes, [seed], salt]
        n_key = [''.join(s_key)]
        return {"key" : n_key, "crude" : supra_key}

    # Processo principal de cifragem
    for caracter in plaintext:
        if control_index == control_key:
            enciphering(caracter)
            control_index = 0
        else:
            enciphering(caracter)
            control_index += 1

    # Geração do salt e sua chave
    salt = create_salt(ciphertext_list)
    ciphertext_list_with_salt = create_salt(ciphertext_list)["salt"]

    # Geração da chave final
    key = key_generator(pass_, seed, salt["salt_key"])
    # Construção do texto cifrado final
    
    if no_salt == False:
        ciphertext = ''.join(ciphertext_list_with_salt)
    else:
        ciphertext = ''.join(ciphertext_list)
    
    return {"poli" : [[ciphertext], key["key"], invalid_characters_list], "crude" : [ciphertext_list, key["crude"], invalid_characters_list]}

# Exemplo de uso

encry = encrypter(plaintext="axabaci", max_table_leng=600)
print(encry["poli"])
