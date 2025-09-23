tables = {}
inverted_tables = {}

def generate_cipher(seed, size, index):
    """
    Generates deterministic cipher.
    Start and end are always '#', middle is uniquely calculated using seed and index.
    """
    # Generates a base number based on seed and index
    num = seed + index * 2654435761
    
    middle = []
    for i in range(size):
        # Chooses between '0' or '1'
        bit = (num >> i) & 1
        middle.append('0' if bit == 0 else '1')
    
    return ''.join(middle)

def generate_tables(seed, specific_sizes: list = None, characters=None):
    """
    Generates cipher tables for specific sizes.
    
    Args:
        seed: Integer number with at least 8 digits
        specific_sizes: List of specific sizes to generate (ex: [32, 15, 20])
        characters: List of characters to be encoded
    """
    global tables
    global inverted_tables
    
    if not isinstance(seed, int) or seed < 10_000_000:
        raise ValueError("Seed must be an integer with at least 8 digits.")

    # If not specified, uses sizes from 9 to 24 (original behavior)
    if specific_sizes is None:
        specific_sizes = list(range(9, 25))
    
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

    for size in specific_sizes:
        table = {}
        # Generates character ciphers using the index
        for i, char in enumerate(characters):
            table[char] = generate_cipher(seed, size, i)
        tables_[size] = table
    
    tables = tables_
    inverted_tables = {k: {v: kk for kk, v in d.items()} for k, d in tables_.items()}
    return tables_, inverted_tables