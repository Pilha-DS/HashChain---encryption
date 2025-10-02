tables = {}
inverted_tables = {}

def generate_cipher(seed, tamanho, indice):
    # Gera um número baseado na seed e índice
    num = seed + indice * 2654435761
    
    meio = []
    for i in range(tamanho):
        # Escolhe entre '#' ou '*'
        bit = (num >> i) & 1
        meio.append('0' if bit == 0 else '1')
    
    return ''.join(meio) 

def gerar_tabelas(seed, inicio=19, fim=20, caracteres=None):
    global tables
    global inverted_tables
    if not isinstance(seed, int) or seed < 10_000_000:
        raise ValueError("Seed deve ser um número inteiro com no mínimo 8 dígitos.")

    if caracteres is None:
        caracteres = [
            "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o", "p","q","r","s","t",
            "u","v","w","x","y","z",
            "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T",
            "U","V","W","X","Y","Z",
            "0","1","2","3","4","5","6","7","8","9",
            "!","\"","#","$","%","&","'","(",")","*","+",
            " ",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~",
            "ã", "ó", "é", "ç", "í", "á", "à", "è", "ì", "ò", "â"
        ]

    tables_ = {}

    for tamanho in range(inicio, fim+1):
        tabela = {}
        # Gera a cifra dos caracteres usando o índice
        for i, char in enumerate(caracteres):
            tabela[char] = generate_cipher(seed, tamanho, i)
        tables_[tamanho] = tabela
    tables = tables_
    inverted_tables = {k: {v: kk for kk, v in d.items()} for k, d in tables.items()}
    return tables_

def main():
    pass

if __name__ == "__main__":
    main()