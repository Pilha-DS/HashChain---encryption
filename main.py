# --- Imports ---
from input_colectors import InputCollector
from HashChainClass import HashChainEncryption

# Global use.
Collector: InputCollector = InputCollector
HashChain: HashChainEncryption = HashChainEncryption()

# Will handle user input, function calls and the interface (WiP).
def main():
    H = HashChainEncryption()
    plaintext = "aba"
    for i in range(10):
        H.encrypt_(plaintext)
        dec = H.decrypt_(H.info(0), H.info(1))
        if dec != plaintext:
            print(f"FAIL at {i}: dec={dec!r}")
            return
        print(f"OK at {i}: dec={dec!r}")
    print("OK 200 runs")

    H.encrypt_("ovolate")
    print(H.decrypt_(H._info[0], H._info[1]))
# Runs main the function if the "main.py" file is directly executed.
if __name__ == "__main__":
    main()