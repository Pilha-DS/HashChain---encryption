from APS.outdated.tables import tables, inverted_tables

def encurtar(entrada: str):
    saida: str = ""
    return saida


def desencurtar(entrada: str):
    saida: str = ""
    return saida


def grafar(text_to_crip: str, cifras, passes:list = [0]):

    def pegar_chave_por_index(dicionario, indice):
        return list(dicionario.keys())[indice]

    def pegar_chave_por_valor(dicionario, valor):
        for chave, val in dicionario.items():
            if val == valor:
                return chave
            
    def limpar_grifo(texto, manter):
        return "".join([c for c in texto if c in manter])

    the_pass = cifras
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


def desgrafar(entrada: str, key: list[int], cifras):

    saida: str = ""
    aux: str = ""
    repeticoes: int = 0
    j: int = 0

    for i, char in enumerate(entrada):
        if char != "#" and char != "*":
            return "FATAL ERROR: 963, Invalid character found"
        if repeticoes == key[j]:
            saida += cifras[key[j]][aux]
            aux = ""
            repeticoes = 0
            if j == len(key) - 1:
                j = 0
            else:
                j += 1
        aux += char
        repeticoes += 1
        # print(aux, "\n", repeticoes, "\n")
    saida += cifras[key[j]][aux]

    print(saida)
    return saida


def main():
    print(grafar("asdasdasdasdsad"))
    pass


if __name__ == "__main__":
    main()
