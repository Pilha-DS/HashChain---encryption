# HashChain in POOP (Python Object Oriented Programing).
# from typing import Optional

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
            
        self.texto: str = plain_text
        self.hash: str = cipher_text
        self.hash_comprimido: str = compressed_cipher_text
        self.acao: str = current_user_action
        self.seed: int = seed
        self.passe: list[int] = table_keys
        self.decompress_table: dict[str, str] = self.create_compression_dict_()
        self.compress_table: dict[str, str] = {v: k for k, v in self.decompress_table.items()}
        
        
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
    def encrypt_(plain_text: str, seed: int, passes: list[int]) -> str:
        pass

    # Receives a hashed text and returns the unhashed text.
    def decrypt_(cipher_text: str, seed: int, passes: list[int]) -> str:
        pass
