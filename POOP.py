# HashChain in POOP (Python Object Oriented Programing).
# from typing import Optional
from tables import gerar_tabelas

class HashChainEncryption:
    # Initializes all the atributes.
    def __init__(
        self, 
        plain_text: str | None, 
        cipher_text: str | None, 
        compressed_cipher_text: str | None, 
        current_user_action: str,
        seed: int, 
        table_keys: list[int]
        ):
            
        self.plain_text: str = plain_text
        self.cipher_text: str = cipher_text
        self.compressed_cipher_text: str = compressed_cipher_text
        self.current_user_action: str = current_user_action
        self.seed: int = seed
        self.table_keys: list[int] = table_keys
        self.decompress_table: dict[str, str] = self.create_compression_dict_()
        self.compress_table: dict[str, str] = {v: k for k, v in self.decompress_table.items()}
        self.cipher_table = gerar_tabelas(seed)
        self.reverse_cipher_table = {k: {v: kk for kk, v in d.items()} for k, d in self.cipher_table.items()}
        # print(self.cipher_table[20][" "])
        # print(self.reverse_cipher_table[20]["00000000000000000001"])
        
    @staticmethod
    def create_compression_dict_():
        with open("HashChain/gitHash/HashChain---encryption/unicode_full.txt", "r", encoding="utf_8") as file:
            content = file.read(1_048_576)
        decompress_table: dict[str, str] = {char: f"{n:020b}" for n, char in enumerate(content)}
        return decompress_table
        
    # Receives a standard hash and retuns a compressed hash. 
    def compression_(self, cipher_text: str) -> str:
        compressed_cipher_text: list[str] = []
        aux: str = ""
        for char in cipher_text:
            aux += char
            if len(aux) == 20:
                compressed_cipher_text.append(self.compress_table[aux])
                aux = ""
        
        return "".join(compressed_cipher_text)

    # Receives a compressed hash and retuns the standard hash. 
    def decompression_(self, compressed_cipher_text: str) -> str:
        cipher_text: list[str] = []
        for char in compressed_cipher_text:
            cipher_text.append(self.decompress_table[char])
        return "".join(cipher_text)
        """ if len(grafo_comprimido) >= 50:
            grafo_descomprimido: list[str] = []
            for char in grafo_comprimido:
                grafo_descomprimido.append(self.decompress_table[char])
            return "".join(grafo_descomprimido)
        else:
            grafo_descomprimido: str = ""
            for char in grafo_comprimido:
                grafo_descomprimido += self.decompress_table[char]
            return grafo_descomprimido """
    
    # Receives a text and returns the hashed text.
    def encrypt_(self, plain_text: str, table_keys: list[int]) -> str:
        if not plain_text: plain_text = self.plain_text
        if not table_keys: table_keys = self.table_keys
        
        cipher_text: list[str] = []
        current_key_index: int = 0
        for _, char in enumerate(plain_text):
            cipher_text.append(self.cipher_table[table_keys[current_key_index]][char])
            if current_key_index == len(table_keys) - 1:
                current_key_index = 0
            else:
                current_key_index += 1
        return HashChainEncryption.compression_(self, "".join(cipher_text))

    # Receives a hashed text and returns the unhashed text.
    def decrypt_(self, cipher_text: str, table_keys: list[int]) -> str:
        cipher_text = HashChainEncryption.decompression_(self, cipher_text)
        inverted_tables = self.reverse_cipher_table
        key = table_keys
        saida: str = ""
        aux: str = ""
        repeticoes: int = 0
        j: int = 0

        for _, char in enumerate(cipher_text):
            if char != "0" and char != "1":
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
        saida += inverted_tables[key[j]][aux]
        
        return saida
