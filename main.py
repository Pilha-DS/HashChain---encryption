# --- Imports ---
from input_colectors import InputCollector
from HashChainClass import HashChainEncryption

# Global use.
Collector: InputCollector = InputCollector
HashChain: HashChainEncryption = HashChainEncryption()

# Will handle user input, function calls and the interface (WiP).
def main():
    HashChain.encrypt_("O Senhor é a minha força, e o meu cântico; ele me foi por salvação; ele é o meu Deus, e eu lhe farei uma habitação; ele é o Deus de meu pai, e eu o exaltarei.” “O Senhor dará força ao seu povo; o Senhor abençoará o seu povo com paz.")
    
# Runs main the function if the "main.py" file is directly executed.
if __name__ == "__main__":
    main()