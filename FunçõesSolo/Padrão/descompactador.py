def desencurtar(texto: str):
    quantidade = ""
    caracter: str = ""
    saida: str = ""
    for char in texto:
        if char in ["0", "1", "2", "3", "4", "5", "6", "7,", "8", "9"]:
            quantidade += char
        else:
            caracter = char
            for i in range(int(quantidade)):
                saida += f"{caracter}"
            quantidade = ""
    print(saida)


def main():
    desencurtar("")
    pass


if __name__ == "__main__":
    main()
