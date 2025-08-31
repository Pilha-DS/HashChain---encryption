from tabelas import tables, inverted_tables

def encurtar(entrada: str):
    saida: str = ""
    return saida


def desencurtar(entrada: str):
    saida: str = ""
    return saida


def grafar(text_to_crip: str):
    def pegar_chave_por_index(dicionario, indice):
        return list(dicionario.keys())[indice]

    def pegar_chave_por_valor(dicionario, valor):
        for chave, val in dicionario.items():
            if val == valor:
                return chave

    text_to_crip
    the_pass = tables
    cripted_text = ""
    caracteres_invalidos = ""
    keyboard = len(the_pass) - 1
    print(f"keyboard: {keyboard}")
    x = 0

    for t in text_to_crip:
        if x > keyboard:
            x = 0
            if t in the_pass[pegar_chave_por_index(the_pass, x)]:
                print(f"x1: {x}")
                cripted_text = (
                    cripted_text + " " + the_pass[pegar_chave_por_index(the_pass, x)][t]
                )
            else:
                caracteres_invalidos = caracteres_invalidos + t + "," + " "
            x += 1

        else:
            if t in the_pass[pegar_chave_por_index(the_pass, x)]:
                print(f"x2: {x}")
                cripted_text = (
                    cripted_text + " " + the_pass[pegar_chave_por_index(the_pass, x)][t]
                )
            else:
                caracteres_invalidos = caracteres_invalidos + t + "," + " "
            x += 1

    else:
        return f"Texto grafado: {text_to_crip} : Grafo: {cripted_text} : Caracteres invalídos ({caracteres_invalidos})"


def desgrafar(entrada: str, key: list[int]):
    global inverted_tables

    saida: str = ""
    aux: str = ""
    repeticoes: int = 0
    j: int = 0

    for i, char in enumerate(entrada):
        if char != "#" and char != "*":
            return "FATAL ERROR: 963, Invalid character found"
        if repeticoes == key[j]:
            saida += inverted_tables[key[j]][aux]
            aux = ""
            repeticoes = 0
            if j == len(key) - 1:
                j = 0
            else:
                j += 1
        aux += char
        repeticoes += 1
        # print(aux, "\n", repeticoes, "\n")
    saida += inverted_tables[key[j]][aux]

    print(saida)
    return saida


def main():
    print(grafar("asdasdasdasdsad"))
    pass


if __name__ == "__main__":
    main()
