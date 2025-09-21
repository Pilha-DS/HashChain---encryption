# HashChain in POOP (Python Object Oriented Programing).
from typing import Optional

class HashChainEncryption:
    # Initializes all the atributes.
    def __init__(
        self, texto: str | None, 
        hash: str | None, 
        hash_comprimido: str | None, 
        acao: str, seed: int, 
        passe: list[int]
        ):
            
        self.texto: str = texto
        self.hash: str = hash
        self.hash_comprimido: str = hash_comprimido
        self.acao: str = acao
        self.seed: int = seed
        self.passe: list[int] = passe
        self.decompress_table: dict[str, str] = self.create_compression_dict_()
        self.compress_table: dict[str, str] = {v: k for k, v in self.decompress_table.items()}
        
        
    @staticmethod
    def create_compression_dict_():
        with open("HashChain/gitHash/HashChain---encryption/unicode_full.txt", "r", encoding="utf_8") as file:
            content = file.read(1_048_576)
        decompress_table: dict[str, str] = {char: f"{n:020b}" for n, char in enumerate(content)}
        return decompress_table
        
    # Receives a standard hash and retuns a compressed hash. 
    def compressao_(self, grafo: str) -> str:
        grafo_comprimido: list[str] = []
        aux: str = ""
        for char in grafo:
            aux += char
            if len(aux) == 20:
                grafo_comprimido.append(self.compress_table[aux])
                aux = ""
        
        return "".join(grafo_comprimido)

    # Receives a compressed hash and retuns the standard hash. 
    def descompressao_(self, grafo_comprimido: str) -> str:
        grafo_descomprimido: list[str] = []
        for char in grafo_comprimido:
            grafo_descomprimido.append(self.decompress_table[char])
        return "".join(grafo_descomprimido)
    
    # Receives a text and returns the hashed text.
    def grafar_(texto: str, seed: int, passes: list[int]) -> str:
        pass

    # Receives a hashed text and returns the unhashed text.
    def desgrafar_(grafo: str, seed: int, passes: list[int]) -> str:
        pass
