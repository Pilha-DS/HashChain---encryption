# Imports
from tables import gerar_tabelas
import random

# Functions
def encrypter(text_to_graph:str = "", dict_tables:dict = {}, pass_:list = [], seed:int = 0): #Função que criptografa o texto desejado.

    if text_to_graph == "":
        raise ValueError('(text_to_graph): Expect a text(str) | Exemple: encrypter(text_to_graph = "eggs")')

    if seed == 0:
        s = random.randint(8, 32)
        ss = []
        while s > 0:
            s -= 1
            if ss == []:
                ss.append(str(random.randint(1, 9)))
            else: ss.append(str(random.randint(0, 9)))
        else: seed = int(''.join(ss))

    if dict_tables == {}:
        # raise ValueError('(dict_table): Expect a cryptography dictionary(dict) | Exemple: encrypter(dict_table = {7 : {"a" = "###***#", "b" = "##*##*#"}, 8 : {"a" = "***###**", "b" = "****####"} } )')
        dict_tables = gerar_tabelas(seed=seed)
    
    if pass_ == []:
        p = random.randint(1, len(text_to_graph) )
        # raise ValueError('(pass_): Expect a list of passes | Exemple: encrypter(pass_ = [10, 12, 21, 9, 12])')
        while p > 1:
            p -= 1
            pass_.append(random.randint(9, 24) ) 
    
    encrypted_text_list, used_passes, invalid_characters_list, key = [], [], [], [] 
    encrypted_text, invalid_characters = "", ""
    control_index = 0
    control_key = len(list(dict_tables.keys()))

    def geral(t):
        try:
            encrypted_text_list.append(dict_tables[get_key_on_index(dict_tables, control_index)][t])
        except:
            invalid_characters_list.append(dict_tables[get_key_on_index(dict_tables, control_index)][t])
            
    def get_key_on_index(dict, index):
        key = list(dict.keys())[index]
        return key

    def key_generator(pass_, seed, salt, scrambler):
        key = [pass_, [seed]]
        return key

    print(dict_tables)
    print(pass_)
    for t in text_to_graph:
        if control_index == control_key:
            geral(t)
            control_index = 0
        else:
            geral(t)
            control_index += 1

    encrypted_text = ''.join(encrypted_text_list)
    invalid_characters = ''.join(invalid_characters_list)
    return encrypted_text, key, invalid_characters

print(encrypter(text_to_graph="abacaxi"))