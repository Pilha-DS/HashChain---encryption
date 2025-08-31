chaves = {
    7: {
        "a": "#*#####",
        "A": "##*####",
        "b": "###*###",
        "B": "####*##",
        "c": "#####*#",
        "C": "#**####",
        "d": "##**###",
        "D": "###**##",
        "e": "####**#",
        "E": "#*#*###",
        "f": "###*#*#",
        "F": "##*#*##",
        "g": "#*##*##",
        "5": "#*****#",
    },
    8: {
        "a": "#*######",
        "A": "##*#####",
        "b": "###*####",
        "B": "####*###",
        "c": "#####*##",
        "C": "######*#",
        "d": "#**#####",
        "D": "##**####",
        "e": "###**###",
        "E": "####**##",
        "f": "#####**#",
        "F": "#*#*####",
        "g": "##*#*###",
        "G": "###*#*##",
        "5": "#*****##",
    },
    9: {
        "a": "#*#######",
        "A": "##*######",
        "b": "###*#####",
        "B": "####*####",
        "c": "#####*###",
        "C": "######*##",
        "d": "#######*#",
        "D": "#**######",
        "e": "##**#####",
        "E": "###**####",
        "f": "####**###",
        "F": "#####**##",
        "g": "######**#",
        "G": "#*#*#####",
        "5": "#*****###",
    },
    10: {
        "a": "#*########",
        "A": "##*#######",
        "b": "###*######",
        "B": "####*#####",
        "c": "#####*####",
        "C": "######*###",
        "d": "#######*##",
        "D": "########*#",
        "e": "#**#######",
        "E": "##**######",
        "f": "###**#####",
        "F": "####**####",
        "5": "#*****####",
    },
    11: {
        "a": "#*#########",
        "A": "##*########",
        "b": "###*#######",
        "B": "####*######",
        "c": "#####*#####",
        "C": "######*####",
        "d": "#######*###",
        "D": "########*##",
        "e": "#########*#",
        "E": "#**########",
        "f": "##**#######",
        "F": "###**######",
        "5": "#*****#####",
    },
    12: {
        "a": "#*##########",
        "A": "##*#########",
        "b": "###*########",
        "B": "####*#######",
        "c": "#####*######",
        "C": "######*#####",
        "d": "#######*####",
        "D": "########*###",
        "e": "#########*##",
        "E": "##########*#",
        "f": "#**#########",
        "F": "##**########",
        "5": "#*****######",
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
    caracteres_invalidos = ""
    keyboard = (len(the_pass) - 1)
    print (f"keyboard: {keyboard}")
    x = 0
                 
    for t in text_to_crip:
        if x > keyboard:
            x = 0    
            if t in the_pass[pegar_chave_por_index(the_pass, x)]:
                print(f"x1: {x}")
                cripted_text = cripted_text + " " +the_pass[pegar_chave_por_index(the_pass, x)][t]
            else:
                caracteres_invalidos = caracteres_invalidos + t + "," + " "
            x += 1
                
        else:
            if t in the_pass[pegar_chave_por_index(the_pass, x)]:
                print(f"x2: {x}")
                cripted_text = cripted_text + " " +the_pass[pegar_chave_por_index(the_pass, x)][t]
            else:
                caracteres_invalidos = caracteres_invalidos + t + "," + " "
            x += 1

    else:
        return f"Texto grafado: {text_to_crip} : Grafo: {cripted_text} : Caracteres invalídos ({caracteres_invalidos})"
        
#fluxo
while True:
    text_t = input("Escreva oque quer criptografar: ")
    print(grafar(text_t, chaves))