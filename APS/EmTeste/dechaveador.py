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
    for n in range(0, pl):
        ciphertext_list.append(ciphertext[s_index:passes[n]])

    return salt_l, posicoes, pl, passes, seed, padding, index, ciphertext_list 