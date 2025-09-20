# HashChain in POOP (Python Object Oriented Programing).

class HashChain:
    # Initializes all the atributes.
    def __innit__(self, texto: str | None, hash: str | None, hash_comprimido: str | None, acao: str, seed: int, passe: list[int]):
        def create_compression_dict_():
            with open("HashChain/gitHash/HashChain---encryption/unicode_full.txt", "r", encoding="utf_8") as file:
                content = file.read(1_048_576)
            decompress_table: dict[str, str] = {char: f"{n:020b}" for n, char in enumerate(content)}
            return decompress_table
            
        self.texto: str = texto if texto else None
        self.hash: str = hash if hash else None
        self.hash_comprimido: str = hash_comprimido if hash_comprimido else None
        self.acao: str = acao if acao else None
        self.seed: int = seed if seed else None
        self.passe: list[int] = passe if passe else None
        self.decompress_table: dict[str, int] = create_compression_dict_()
        self.compress_table: dict[int, str] = {v: k for k, v in self.decompress_table.items()}
        
    # Receives a text and returns the hashed text.
    def grafar_(texto: str, seed: int, passes: list[int]) -> str:
        pass

    # Receives a hashed text and returns the unhashed text.
    def desgrafar_(grafo: str, seed: int, passes: list[int]) -> str:
        pass

    # Receives a standard hash and retuns a compressed hash. 
    def compressao_(grafo: str) -> str:
        return grafo_comprimido

    # Receives a compressed hash and retuns the standard hash. 
    def descompressao_(grafo_comprimido: str) -> str:
        return grafo_descomprimido