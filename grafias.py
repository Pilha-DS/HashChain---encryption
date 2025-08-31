from tabelas import tables, inverted_tables

#variaveis
pass_s = [{
    "key" : 7,
    "a" : "#*#####", "A" : "#*###*#",
    "b" : "##*####", "B" : "##*##*#",
    "c" : "###*###", "C" : "###*#*#",
    "d" : "####*##", "D" : "####**#",
    "e" : "#####*#", "E" : "#####*#",
    "f" : "#*##**#", "F" : "#**#**#",
    "g" : "#*#***#", "G" : "#*****#",
}, {
    "key" : 8,
    "a" : "#*######", "A" : "#*####*#",
    "b" : "##*#####", "B" : "##*###*#",
    "c" : "###*####", "C" : "###*##*#",
    "d" : "####*###", "D" : "####*#*#",
    "e" : "#####*##", "E" : "#####**#",
    "f" : "######*#", "F" : "#*####*#",
    "g" : "#####**#", "G" : "####***#",
}, {
    "key" : 9,
    "a" : "#*#######", "A" : "#*#####*#",
    "b" : "##*######", "B" : "##*####*#",
    "c" : "###*#####", "C" : "###*###*#",
    "d" : "####*####", "D" : "####*##*#",
    "e" : "#####*###", "E" : "#####*#*#",
    "f" : "######*##", "F" : "######**#",
    "g" : "#######*#", "G" : "#*#####*#",
}
]

def encurtar(entrada: str):
    saida: str = ""
    return saida


def desencurtar(entrada: str):
    saida: str = ""
    return saida


def grafar(text_to_crip: str):
    text_to_crip
    the_pass = pass_s
    cripted_text = ""
    keyboard = len(the_pass) - 1
    x = 0

    for t in text_to_crip:
        if x > keyboard:
            x = 0
            print(f"x1: {x}")
            cripted_text = cripted_text + " " + the_pass[x][t] + str(the_pass[x]["key"])
            x += 1
        else:
            if t in the_pass[x]:
                cripted_text = (
                    cripted_text + " " + the_pass[x][t] + str(the_pass[x]["key"])
                )
                print(f"x2: {x}")
                x += 1

    return cripted_text


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
    pass


if __name__ == "__main__":
    main()
