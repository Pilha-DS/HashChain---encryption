# --- Imports ---
from input_colectors import InputCollector

# Global use.
Collector: InputCollector = InputCollector

# Receives a text and returns the hashed text.
def grafar(texto: str, seed: int, passes: list[int]) -> str:
    pass

# Receives a hashed text and returns the unhashed text.
def desgrafar(grafo: str, seed: int, passes: list[int]) -> str:
    pass

# Receives a standard hash and retuns a compressed hash. 
def compressao(grafo: str) -> str:
    return grafo_comprimido

# Receives a compressed hash and retuns the standard hash. 
def descompressao(grafo_comprimido: str) -> str:
    return grafo_descomprimido

# Will handle user input, function calls and the interface (WiP).
def main():
    action = Collector.get_action_()
    seed = Collector.get_seed_()
    passe = Collector.get_passes_()
    

# Runs main the function if the "main.py" file is directly executed.
if __name__ == "__main__":
    main()