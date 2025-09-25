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
              pass_:list = [],
              seed:int = 0,
              # key:str = "",
              dict_tables:dict = {},
              no_salt:bool = False,
              debug_mode:bool = False,
              min_table_leng:int = 20,
              max_table_leng:int = 999,

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

    #====================================================#
    #= Validação dos parâmetros de entrada obrigatorios =#
    #====================================================#
    if not plaintext: # Verifica se o plaintext não esta vazio
        raise ValueError('Parâmetro obrigatório: plaintext deve ser uma string não vazia')

    #========================================================#    
    #= Geração de valores padrões para parâmetros opcionais =#
    #========================================================#
    if not seed: # Gera a seed aleatoria de 256 caracteres, caso nao seja passada como parâmetro
        seed = gerar_seed_decimal_aleatoria(256)
    
    if not pass_: # Gera passes aleatórios, caso nao seja passado como parâmetro. Baseado no comprimento do plaintext
        p = len(plaintext)
        while p > 1:
            p -= 1
            pass_.append(random.randint(min_table_leng, max_table_leng))
    
    if not dict_tables: # Gera tabelas de substituição usando a seed e os passes
        dict_tables = gerar_tabelas(seed, pass_)[0]
    
    #=============#
    #= Variaveis =#
    #=============#
    crude_ciphertext_list = []
    salt_ciphertext_list = []
    invalid_characters_list = []
    key = []
    control_index = 0
    control_key = len(list(dict_tables.keys())) - 1

    #===========#
    #= Funções =#
    #===========#
    # Faz a cipher text em formato de lista
    def enciphering(
            caracter:str
            ) -> None:
        
        try:
            # Obtém a substituição da tabela apropriada
            tabela_atual = dict_tables[get_key_on_index(control_index)]
            crude_ciphertext_list.append(tabela_atual[caracter])
        except KeyError:
            # Registra caracteres não mapeados nas tabelas
            invalid_characters_list.append(caracter)
    
    def get_key_on_index(
            index:int, 
            dict:dict = dict_tables
            ) -> int:
        
        return list(dict.keys())[index]
    
    # Gera o salt e retorna um ciphertext com salt em formato de lista
    def create_salt(
            ciphertext_list:list = [],
            pass_:list = [],
            seed:int = 0,
            min_leng:int = 20,
            max_leng:int = 100,
            ):

        # Variaveis
        mini, maxi = min_leng, max_leng
        posicoes = []

        # Definindo variaveis e outros
        salt_leng = random.randint(2, 2 + len(ciphertext_list))
        salt_ciphertext_list, salt_passes = [c for c in ciphertext_list], [p for p in pass_]

        for n in range(salt_leng):
            salt_pass = random.randint(mini, maxi)
            posicao = random.randint(0, (len(salt_ciphertext_list) - 1))
            
            # Gerando tabela
            tb = gerar_tabelas(seed, [salt_pass]) # tb = tabela

            # Inserindo dentro das tabelas de retorno
            salt_passes.insert(posicao, salt_pass)
            salt_ciphertext_list.insert(posicao, tb[0][salt_pass][chr(random.randint(65, 122))])
            posicoes.append(posicao)


        return salt_ciphertext_list, salt_passes, posicoes

    # Faz o polimento da chave para leitura posterior
    def key_generator(
            pass_:list = [], 
            seed:int = 0,
            salt:list = [],
            ) -> list:
        
        # Variaveis
        seed_value = str(seed)
        crude_passes = [p for p in pass_]
        poli_passes = []
        poli_salt = [str(s) for s in salt]
        
        # Formata os passes para terem 3 dígitos cada
        for p in crude_passes:
            poli_pass = str(p).zfill(3)
            poli_passes.append(poli_pass)
        
        # Calcula metadados para incorporação na chave
        pl = str(len(poli_passes)) # pl = passes leng
        lolp = str(len(str(pl))).ljust(3, '0') # lolp = leng of leng passes
        sl = str(len(seed_value)) # sl = seed leng
        salt_l = str(len(salt)) # salt_l = salt leng.0
        lol_salt = str(len(salt_l)).ljust(3, '0')# lol_salt = leng of leng salt

        # Gera a forma final das chaves
        crude_key = (f'\nsalt: lol_salt: {lol_salt}, salt_l: {[salt_l]}, posições salt: {poli_salt}\n'
                     f'passes c salt: lolp: {[lolp]}, pl: {[pl]}, passes: {poli_passes}\n'
                     f'seed: seed: {[sl]}, seed {[seed_value]}') # Para modo debug
        polished_key = ''.join([ # Para usuarios final
             ''.join(lol_salt),
             ''.join(salt_l),
             ''.join(poli_salt),
             ''.join(lolp),
             ''.join(pl),
             ''.join(poli_passes),
            ''.join(sl),
            ''.join(seed_value)
        ])

        return poli_passes, polished_key, crude_key

    #==============================#
    #= Gera a lista do ciphertext =#
    #==============================#
    for caracter in plaintext:
        if control_index == control_key:
            enciphering(caracter)
            control_index = 0
        else:
            enciphering(caracter)
            control_index += 1

    #==============================================================================#
    #= Gera o salt na criptografia caso possal, junta a lista e gera o ciphertext =#
    #==============================================================================#
    if no_salt == False:
        salt = create_salt(crude_ciphertext_list, pass_, seed, 20, 100)
        salt_ciphertext_list = salt[0]
        ciphertext = ''.join(salt_ciphertext_list)
    else:
        ciphertext = ''.join(crude_ciphertext_list)

    #==========================#
    #= Geração da chave final =#
    #==========================#
    key = key_generator(salt[1], seed, salt[2])

    #=======================#
    #= Verificações finais =#
    #=======================#
    if debug_mode == True:
        if no_salt == False:
            return (
                f'Plaintext: {plaintext}\n'
                f'Ciphertext: {salt_ciphertext_list}\n'
                f'Keys: {key[2]}\n' 
                f'Invalid characters: {invalid_characters_list}\n'
                )
        else:
            return (
                f'Plaintext: {plaintext}\n'
                f'Ciphertext: {crude_ciphertext_list}\n'
                f'Keys: {key[2]}\n' 
                f'Invalid characters: {invalid_characters_list}\n'
                )
    else:
        return [ciphertext, key[1]]

encry = encrypter(plaintext="axabaci", max_table_leng=600)
print(encry)
