# --- Imports ---
from input_colectors import InputCollector
from POOP import HashChainEncryption

# Global use.
Collector: InputCollector = InputCollector
HashChain = HashChainEncryption(None, None, None, None, None, None)

print(HashChain.descompressao_("asdzxc"))
print(HashChain.compressao_(HashChain.descompressao_("asdzxc")))

# Will handle user input, function calls and the interface (WiP).
def main():
    """action = Collector.get_action_()
    seed = Collector.get_seed_()
    passe = Collector.get_passes_() """
    

# Runs main the function if the "main.py" file is directly executed.
if __name__ == "__main__":
    main()