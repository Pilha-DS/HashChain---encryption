# --- Imports ---
from input_colectors import InputCollector
from HashChainClass import HashChainEncryption

# Global use.
Collector: InputCollector = InputCollector
HashChain: HashChainEncryption = HashChainEncryption()

# Will handle user input, function calls and the interface (WiP).
def main():
    HashChain.encrypt_("asd", [100, 50], 123131212313123123213121231231231312312321312123123312321312123123)
    HashChain.out("c")
    HashChain.decrypt_(HashChain.info("cc"), HashChain.info("k"))
    # print(HashChain.info("cc"), HashChain.info("k"))
    
# Runs main the function if the "main.py" file is directly executed.
if __name__ == "__main__":
    main()