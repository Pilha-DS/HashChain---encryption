from tables import gerar_tabelas

def dechaveador(key:str = '', ciphertext:str = ''):
    if not key:
        raise ValueError("Coloque uma chave valída")
    if not ciphertext:
        raise ValueError("Coloque um ciphertext valído")

    lol_salt = int(key[0:3])
    index = 3 + lol_salt
    
    salt_l = int(key[3:index])
    posicoes = []

    for n in range(0, salt_l):
        pn = int(key[index:index + 3])
        index += 3  
        posicoes.append(int(key[index:index + pn]))
        index += pn

    lol_p = int(key[index:index + 3 ])
    pl = int(key[index + 3:index + 3 + lol_p])
    passes = []

    index += lol_p + 3
    for n in range(0, pl):
        passes.append(int(key[index:index + 3]))
        index += 3

    sl = int(key[index:index + 3])
    seed = int(key[index + 3:sl + index + 3])
    
    index += sl + 3

    padding = None if not key[index:] else int(key[index:])

    ciphertext_list = []

    s_index = 0

    for n in range(0, len(passes)):
        ciphertext_list.append(ciphertext[s_index:passes[n] + s_index])
        s_index += passes[n]
    
    pad = -1
    for p in range(0, len(posicoes)):
        del ciphertext_list[posicoes[pad]]
        del passes[posicoes[pad]]
        pad += -1

    return passes, seed, padding, ciphertext_list

def descrypter(key, ciphertext):
    desc = dechaveador(key, ciphertext)

    pass_ = desc[0]
    seed = desc[1]
    cipher = desc[3]

    plaintext = []

    # GERAÇÃO DE SEEDS DIFERENTES PARA CADA PASSE
    seeds_por_passe = []
    dict_tables_por_passe = {}
    
    # Usa a seed principal para gerar seeds únicas para cada passe
    for i, passe in enumerate(pass_):
        # Gera uma seed única para este passe baseada na seed principal + índice do passe
        seed_passe = seed + (i * 1000000) + passe
        seeds_por_passe.append(seed_passe)
        
        # Gera tabelas específicas para este passe
        dict_tables_passe = gerar_tabelas(seed_passe, [passe])[1]
        dict_tables_por_passe[passe] = dict_tables_passe[passe]

    for n, p in enumerate(pass_):
        try:
            plaintext.append(dict_tables_por_passe[p][cipher[n]])
        except:
            print("invalida")
                  
    return ''.join(plaintext)

