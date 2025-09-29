def dechavador(key:str = ''):
    if not key:
        raise ValueError("Coloque uma chave valída")

    lol_salt = int(key[0:3])
    index = 3 + lol_salt
    
    salt_l = int(key[3:index])
    posicoes = []

    for n in range(0, salt_l):
        posicoes.append(int(key[index:index + 10]))
        index += 10

    lol_p = int(key[index:index + 3])
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

    return salt_l, posicoes, pl, passes, seed, padding, index

dec = dechavador("002230000000001000000000400000000000000000001000000000300000000040000000007000000000800000000050000000000000000001300000000030000000009000000000000000000010000000014000000000100000000090000000009000000001000000000180000000018000000002700229202312079534160571174594069169164053197597247456425177316238144291023555287104064569053064720532271716212735475201753637551230442325532421240307503273472719099999908908")

print("salt_leng: ", dec[0])
print(" ")
print("posicoes: ",dec[1])
print(" ")
print("passes_leng: ",dec[2])
print(" ")
print("passes: ",dec[3])
print(" ")
print("seed: ",dec[4])
print(" ")
print("padding: ",dec[5])
print(" ")
print("index: ",dec[6])
print(" ")