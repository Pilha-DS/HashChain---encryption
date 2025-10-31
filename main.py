# --- Imports ---
from input_colectors import InputCollector
from HashChainClass import HashChainEncryption

# Global use.
Collector: InputCollector = InputCollector
HashChain: HashChainEncryption = HashChainEncryption()

# Will handle user input, function calls and the interface (WiP).
def main():
    H = HashChainEncryption()

    H.encrypt_("ovolate")

    H.encrypt_("abacate", no_salt=True)

# Runs main the function if the "main.py" file is directly executed.
if __name__ == "__main__":
    main()