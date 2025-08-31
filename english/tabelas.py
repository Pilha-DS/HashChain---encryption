tables = {}
inverted_tables = {}

def generate_cipher(seed, size, index):
    print(seed)

    # Generates a number based on the seed and index
    num = seed + index * 2654435761
    mid = []
    for i in range(size - 2):
        # pickup '#' or '*'
        bit = (num >> i) & 1
        mid.append('#' if bit == 0 else '*')
        print(mid)
    return '#' + ''.join(mid) + '#'

def generate_tables(seed, begin=9, end=24, characters=None):
    global tables
    global inverted_tables
    if not isinstance(seed, int) or seed < 10_000_000:
        raise ValueError("Seed must be an integer with at least 8 digits.")
    if characters is None:
        characters = [
            "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t",
            "u","v","w","x","y","z",
            "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T",
            "U","V","W","X","Y","Z",
            "0","1","2","3","4","5","6","7","8","9",
            "!","\"","#","$","%","&","'","(",")","*","+",
            " ",",","-",".","/",":",";","<","=",">","?","@","[","]","^","_","`","{","|","}","~"
        ]
    tables_ = {}
    for size_m in range(begin, end+1):
        table = {}

        # Generates the character cipher using the index
        for i, char in enumerate(characters):
            table[char] = generate_cipher(seed, size_m, i)
        tables_[size_m] = table
    tables = tables_
    inverted_tables = {key_s: {value: key for key, value in the_table_ss.items()} for key_s, the_table_ss in tables.items()}
    return tables_

def main():
    pass

if __name__ == "__main__":
    main()