tabelas = {
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

#Funcões
def grafar(text_to_crip: str, passes: [int] = [0]):

    def pegar_chave_por_index(dicionario, indice):
        return list(dicionario.keys())[indice]

    def pegar_chave_por_valor(dicionario, valor):
        for chave, val in dicionario.items():
            if val == valor:
                return chave
            
    def limpar_grifo(texto, manter):
        return "".join([c for c in texto if c in manter])

    the_pass = tabelas
    cripted_text = ""
    caracteres_invalidos = ""
    passes_usados = ""
    x = 0
    
    if passes != [0]:
    #Mandando o passe.
        xx = 0
        for t in text_to_crip:
            if xx == passes[-1]:
                x = 0
                xx = passes[x]
                if t in the_pass[xx]:
                    passes_usados = passes_usados + str(passes[x]) + "," + " "
                    cripted_text = cripted_text + the_pass[xx][t]
                    x += 1
                else:
                    caracteres_invalidos = caracteres_invalidos + t + "," + " "
            else:
                xx = passes[x]
                if t in the_pass[xx]:
                    passes_usados = passes_usados + str(passes[x]) + "," + " "
                    cripted_text = cripted_text + the_pass[xx][t]
                    x += 1
                else:
                    caracteres_invalidos = caracteres_invalidos + t + "," + " "
        else:
            return f"Texto grafado: {text_to_crip} : Grafo: {cripted_text} : Caracteres invalídos ({caracteres_invalidos}) : Os passes usados são: ({passes_usados})"
        
    #Não mandando o passe.
    else:
        keyboard = (len(the_pass))
        print (f"keyboard: {keyboard}")
        for t in text_to_crip:
            if x == keyboard:
                x = 0    
                if t in the_pass[pegar_chave_por_index(the_pass, x)]:
                    passes_usados = passes_usados + str(pegar_chave_por_index(the_pass, x)) + "," + " "
                    cripted_text = cripted_text + the_pass[pegar_chave_por_index(the_pass, x)][t]
                else:
                    caracteres_invalidos = caracteres_invalidos + t + "," + " "
                x += 1  
            else:
                if t in the_pass[pegar_chave_por_index(the_pass, x)]:
                    passes_usados = passes_usados + str(pegar_chave_por_index(the_pass, x)) + "," + " "
                    cripted_text = cripted_text + the_pass[pegar_chave_por_index(the_pass, x)][t]
                else:
                    caracteres_invalidos = caracteres_invalidos + t + "," + " "
                x += 1
        else:
            cripted_text = limpar_grifo(cripted_text, "#*")
            return f"Texto grafado: {text_to_crip} : Grafo: {cripted_text} : Caracteres invalídos ({caracteres_invalidos}) : Os passes usados são: ({passes_usados})"
        
#fluxo
while True:
    text_t = input("Escreva oque quer criptografar: ")
    print(grafar(text_t))