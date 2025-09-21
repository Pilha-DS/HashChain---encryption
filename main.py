# --- Imports ---
from input_colectors import InputCollector
from POOP import HashChainEncryption
import time
# Global use.
Collector: InputCollector = InputCollector
HashChain = HashChainEncryption(None, None, None, None, None, None)
""" start = time.perf_counter()
for i in range(10_000):
    print(HashChain.descompressao_("桶"))
end = time.perf_counter() """

print(f"{end - start:.3f}s")
# Will handle user input, function calls and the interface (WiP).
def main():
    """ action = Collector.get_action_()
    seed = Collector.get_seed_()
    passe = Collector.get_passes_()
    Hasher: HashChainEncryption = HashChainEncryption(input(), None, None, action, seed, passe) """

# Runs main the function if the "main.py" file is directly executed.
if __name__ == "__main__":
    main()