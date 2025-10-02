# --- Imports ---
from input_colectors import InputCollector
from POOP import HashChainEncryption

# Global use.
Collector: InputCollector = InputCollector
HashChain: HashChainEncryption = HashChainEncryption(None, None, None, None, 1233245678, [20])

# Will handle user input, function calls and the interface (WiP).
def main():
    """ action = Collector.get_action_()
    seed = Collector.get_seed_()
    passe = Collector.get_passes_()
    Hasher: HashChainEncryption = HashChainEncryption(input(), None, None, action, seed, passe) """
    while True:
        print(f"Deseja [C]: cripta | [D]: Decrita | [S]: sair")
        a = input(": ").lower()
        if a == "s": break
        esc = input("texto: ")
        # start = time.perf_counter()
        if a == "c":
            print(HashChain.encrypt_(esc, [20]))
        elif a == "d":
            print(HashChain.decrypt_(esc, [20]))
        # end = time.perf_counter()
        # print(f"{end - start:.3f}s")

# Runs main the function if the "main.py" file is directly executed.
if __name__ == "__main__":
    main()  