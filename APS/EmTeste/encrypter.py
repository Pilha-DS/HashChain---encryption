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
    sorted_bytes = os.urandom(num_digitos // 2)  # Cada byte representa aproximadamente 2 dígitos decimais
    
    # Converte os bytes para um inteiro de precisão arbitrária
    large_number = int.from_bytes(sorted_bytes, 'big')
    
    # Formata para garantir exatamente num_digitos dígitos
    seed_str = str(large_number).zfill(num_digitos)
    seed_str = seed_str[:num_digitos]  # Garante o comprimento exato
    
    return int(seed_str)

def encrypter(plaintext:str = "",
              dict_tables:dict = {},
              pass_:list = [],
              min_table_leng:int = 20,
              max_table_leng:int = 300,
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
    invalid_characters_list = []
    key = []
    control_index = 0
    control_key = len(list(dict_tables.keys())) - 1

    def enciphering(caracter: str) -> None:
        """
        Aplica substituição criptográfica usando as tabelas apropriadas.
        
        Args:
            caracter (str): Caractere a ser cifrado
        """
        try:
            # Obtém a substituição da tabela apropriada
            tabela_atual = dict_tables[get_key_on_index(control_index)]
            ciphertext_list.append(tabela_atual[caracter])
        except KeyError:
            # Registra caracteres não mapeados nas tabelas
            invalid_characters_list.append(caracter)
    
    def get_key_on_index(index: int) -> int:
        """
        Obtém a chave do dicionário com base no índice atual.
        
        Args:
            index (int): Índice da chave desejada
        
        Returns:
            int: Chave correspondente ao índice
        """
        return list(dict_tables.keys())[index]
    
    def key_generator(passes: list, seed_value: int) -> list:
        """
        Gera uma chave criptográfica a partir dos passes e seed.
        
        Args:
            passes (list): Lista de passes numéricos
            seed_value (int): Valor da seed para derivação de chave
        
        Returns:
            list: Chave gerada formatada
        """
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
        
        return [''.join(s_key)]

    # Processo principal de cifragem
    for caracter in plaintext:
        if control_index == control_key:
            enciphering(caracter)
            control_index = 0
        else:
            enciphering(caracter)
            control_index += 1
    
    # Geração da chave final
    key = key_generator(pass_, seed)
    
    # Construção do texto cifrado final
    ciphertext = ''.join(ciphertext_list)
    
    # Limpeza de variáveis sensíveis
    ciphertext_list.clear()
    invalid_characters_list.clear()
    pass_.clear()
    dict_tables.clear()
    
    return [ciphertext], key, invalid_characters_list

# Exemplo de uso
encry = encrypter(plaintext="axabaci")
print(encry)