# Imports
from tables import gerar_tabelas
import random

# Functions
def encrypter(text_to_graph:str = "", dict_tables:dict = {}, pass_:list = [], seed:int = 00000000): #Função que criptografa o texto desejado.

    if text_to_graph == "":
        raise ValueError('(text_to_graph): Expect a text(str) | Exemple: encrypter(text_to_graph = "eggs")')

    if len(str(seed)) < 8:
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
        gerar_tabelas(seed=seed)
    
    if pass_ == []:
        p = random.randint(1, len(text_to_graph) )
        # raise ValueError('(pass_): Expect a list of passes | Exemple: encrypter(pass_ = [10, 12, 21, 9, 12])')
        while p > 1:
            p -= 1
            pass_.append(random.randint(9, 24) ) 
    
    def get_key_on_index(dict, index):
        key = list(dict.keys())[index]
        return key

    def key_generator(pass_, seed, salt, scrambler):
        key = [pass_, [seed]]
        return key
    
    encrypted_text_list, used_passes, invalid_characters_list, key = [], [], [], [] 
    encrypted_text, invalid_characters = "", ""
    control_index, condtional_control = 0, 0

    print(pass_)
    for t in text_to_graph:
        if t in dict_tables[control_index]:
            encrypted_text_list.append(dict_tables[condtional_control][t])
            used_passes.append(str(pass_[control_index]))
            control_index += 1
        else:
            invalid_characters_list.append(t)
    else:
        key = key_generator(pass_, seed)
        encrypted_text = ''.join(encrypted_text_list)
        invalid_characters = ''.join(invalid_characters_list)
        return encrypted_text, key, invalid_characters
        
print(encrypter(text_to_graph="abacaxi")[0])
"""     else:
        control_key = (len(dict_tables))
        for t in text_to_graph:
            if control_index == control_key:
                control_index = 0    
                if t in dict_tables[get_key_on_index(dict_tables, control_index)]:
                    encrypted_text.append(str(get_key_on_index(dict_tables, control_index)))
                    used_passes.append(str(get_key_on_index(dict_tables, control_index)))
                else:
                    invalid_characters.append(t)
                control_index += 1  
            else:
                if t in dict_tables[get_key_on_index(dict_tables, control_index)]:
                    encrypted_text.append(str(get_key_on_index(dict_tables, control_index)))
                    used_passes.append(str(get_key_on_index(dict_tables, control_index)))
                else:
                    invalid_characters.append(t)
                control_index += 1 """

"""     for t in text_to_graph:
        if condtional_control == pass_[-1]:
            control_index = 0
            condtional_control = pass_[control_index]
            if t in dict_tables[condtional_control]:
                encrypted_text_list.append(dict_tables[condtional_control][t])
                used_passes.append(str(pass_[control_index]))
                control_index += 1
            else:
                invalid_characters_list.append(t)
        else:
            condtional_control = pass_[control_index]
            if t in dict_tables[condtional_control]:
                encrypted_text_list.append(dict_tables[condtional_control][t])
                used_passes.append(str(pass_[control_index]))
                control_index += 1
            else:
                invalid_characters_list.append(t) """