import tabelas


#Funcões
def encryptor(steps_on_use:dict, text_to_cryp:str = "ameixa", manual_steps:list = [0], seed: int = 99999999, clear:bool = False):

    def get_key_on_index(dict, index):
        return list(dict.keys())[index]

    def get_key_on_value(dict, value):
        for key, research_value in dict.items():
            if research_value == value:
                return key
            
    def clear_text(text_to_clear, characters_to_keep): #
        return "".join([caracter for caracter in text_to_clear if caracter in characters_to_keep])

    steps_dict = steps_on_use
    ecrypted_text = ""
    invalid_characters = ""
    used_steps = ""
    control_index = 0
    
    if manual_steps != [0]:
        condtional_control = 0
        for character in text_to_cryp:
            if condtional_control == manual_steps[-1]:
                control_index = 0
                condtional_control = manual_steps[control_index]
                if character in steps_dict[condtional_control]:
                    used_steps = used_steps + str(manual_steps[control_index]) + "," + " "
                    ecrypted_text = ecrypted_text + " " + steps_dict[condtional_control][character]
                    control_index += 1
                else:
                    invalid_characters = invalid_characters + character + "," + " "
            else:
                condtional_control = manual_steps[control_index]
                if character in steps_dict[condtional_control]:
                    used_steps = used_steps + str(manual_steps[control_index]) + "," + " "
                    ecrypted_text = ecrypted_text + " " + steps_dict[condtional_control][character]
                    control_index += 1
                else:
                    invalid_characters = invalid_characters + character + "," + " "
        else:
            if clear == True:
                ecrypted_text = clear_text(ecrypted_text, "#*")
            return ecrypted_text, used_steps, invalid_characters, text_to_cryp, control_key
                
    else: #Não mandando passe.
        control_key = (len(steps_dict))
        for character in text_to_cryp:
            if control_index == control_key:
                control_index = 0    
                if character in steps_dict[get_key_on_index(steps_dict, control_index)]:
                    used_steps = used_steps + str(get_key_on_index(steps_dict, control_index)) + "," + " "
                    ecrypted_text = ecrypted_text + " " + steps_dict[get_key_on_index(steps_dict, control_index)][character]
                else:
                    invalid_characters = invalid_characters + character + "," + " "
                control_index += 1  
            else:
                if character in steps_dict[get_key_on_index(steps_dict, control_index)]:
                    used_steps = used_steps + str(get_key_on_index(steps_dict, control_index)) + "," + " "
                    ecrypted_text = ecrypted_text +  " " + steps_dict[get_key_on_index(steps_dict, control_index)][character]
                else:
                    invalid_characters = invalid_characters + character + "," + " "
                control_index += 1
        else:
            if clear == True:
                ecrypted_text = clear_text(ecrypted_text, "#*")
            return ecrypted_text, used_steps, invalid_characters, text_to_cryp, control_key, seed
while True:
    text_teste = input("Escreva oq quer criptografar: ")
    seed = int(input("Digite a seed: "))
    chaves = tabelas.gerar_tabelas(seed, 9, 12)
    grafo = encryptor(chaves, text_teste, [0], seed, True)

    print(chaves)
    print(f"Texto grafado: ({grafo[-3]}) | Grafo: ({grafo[-6]}) | Caracteres invalídos: ({grafo[-4]}) | Os passes usados são: ({grafo[-5]}) | Seed usada é:{grafo[-1]}")