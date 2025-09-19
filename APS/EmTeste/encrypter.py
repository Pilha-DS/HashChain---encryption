# Imports
from tables import gerar_tabelas
import random

# Functions
def encrypter(text_to_graph:str = "", dict_tables:dict = {}, pass_ = 0, seed:int = 00000000): #Função que criptografa o texto desejado.

    if len(seed) == 00000000:
        if len(seed) <= 7: 
            raise ValueError('(seed): Expect a number(int) of at least 8 digits | Exemple: encrypter(seed = 12345678)')
        else:
            seed = random.randint(100_000_000, 100_000_000)
    if dict_tables == {}:
        # raise ValueError('(dict_table): Expect a cryptography dictionary(dict) | Exemple: encrypter(dict_table = {7 : {"a" = "###***#", "b" = "##*##*#"}, 8 : {"a" = "***###**", "b" = "****####"} } )')
        gerar_tabelas(seed=seed)
    if text_to_graph == "":
        raise ValueError('(text_to_graph): Expect a text(str) | Exemple: encrypter(text_to_graph = "eggs")')
    if pass_ == 0:
        raise ValueError('(pass_): Expect a list of passes | Exemple: encrypter(pass_ = [10, 12, 21, 9, 12])')
    def get_key_on_index(dict, index):
        key = list(dict.keys())[index]
        return key
    
    encrypted_text_list, used_passes, invalid_characters_list = [], [], [] 
    encrypted_text, invalid_characters = "", ""
    control_index = 0
    condtional_control = 0 

    for t in text_to_graph:
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
                invalid_characters_list.append(t)
    
        

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