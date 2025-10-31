# --- Imports ---
from input_colectors import InputCollector
from HashChainClass import HashChainEncryption

# Global use.
Collector: InputCollector = InputCollector
HashChain: HashChainEncryption = HashChainEncryption()

# Will handle user input, function calls and the interface (WiP).
def main():
    HashChain.encrypt_("asd", no_salt=False)
    HashChain.decrypt_(HashChain.info("cc"), HashChain.info("k"))
    # print(HashChain.info("cc"), HashChain.info("k"))
    
# Runs main the function if the "main.py" file is directly executed.
if __name__ == "__main__":
    main()