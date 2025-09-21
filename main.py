# --- Imports ---
from input_colectors import InputCollector
from POOP import HashChainEncryption

# Global use.
Collector: InputCollector = InputCollector
HashChain: HashChainEncryption = HashChainEncryption(None, None, None, None, None, None)

# Will handle user input, function calls and the interface (WiP).
def main():
    """ action = Collector.get_action_()
    seed = Collector.get_seed_()
    passe = Collector.get_passes_()
    Hasher: HashChainEncryption = HashChainEncryption(input(), None, None, action, seed, passe) """
    """ while True:
        a = input("N: ")
        if a == "s": break
        esc = input("esc: ")
        start = time.perf_counter()
        if a == "c":
            print(HashChain.compressao_(esc))
        elif a == "d":
            print(HashChain.descompressao_(esc))
        end = time.perf_counter()
        print(f"{end - start:.3f}s") """

# Runs main the function if the "main.py" file is directly executed.
if __name__ == "__main__":
    main()