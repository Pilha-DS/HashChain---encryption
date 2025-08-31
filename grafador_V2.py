chaves = {
    7: {
        "a": "#*#####",
        "A": "#####",
        "b": "##*####",
        "B": "#####",
        "c": "###*###",
        "C": "#####",
        "d": "####*##",
        "D": "#####",
        "e": "#####*#",
        "E": "#####*#",
        "f": "###*#",
        "F": "###",
        "g": "###",
        "G": "#*#",
    },
    8: {
        "a": "#*######",
        "A": "######",
        "b": "##*#####",
        "B": "######",
        "c": "###*####",
        "C": "######",
        "d": "####*###",
        "D": "######",
        "e": "#####*##",
        "E": "######",
        "f": "######*#",
        "F": "######",
        "g": "######",
        "G": "####*#",
    },
    9: {
        "a": "#*#######",
        "A": "#######",
        "b": "##*######",
        "B": "#######",
        "c": "###*#####",
        "C": "#######",
        "d": "####*####",
        "D": "#######",
        "e": "#####*###",
        "E": "#######",
        "f": "######*##",
        "F": "#######",
        "g": "#######*#",
        "G": "#######",
    },
}

#funcoes
def pegar_chave_por_index(dicionario, indice):
    return list(dicionario.keys())[indice]

def pegar_chave_por_valor(dicionario, valor):
    for chave, val in dicionario.items():
        if val == valor:
            return chave
 
def grafar(text_to_crip: str, the_pass):
    text_to_crip
    the_pass
    cripted_text = ""
    keyboard = len(the_pass) - 1
    x = 0
                 
    for t in text_to_crip:
        if x > keyboard:
            x = 0
            print(f"x1: {x}")
            cripted_text = cripted_text + pegar_chave_por_valor(the_pass[x], t)
            x += 1
        else:
            print(the_pass[pegar_chave_por_index(the_pass, x)][t])
            """ if t in the_pass[pegar_chave_por_index(the_pass, x)]:
                cripted_text = cripted_text + pegar_chave_por_valor(the_pass[x], t)
                x += 1 """
                
#fluxo

""" valor = input("a: ")
print(inverter_dicionario(pass_s[0], valor)) """

text_t = input("Escreva oque quer criptografar: ")
print(grafar(text_t, chaves))




