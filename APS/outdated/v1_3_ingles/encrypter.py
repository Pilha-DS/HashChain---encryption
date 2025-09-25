# =================================================== #
# ===================== IMPORTS ===================== #
# =================================================== #
import random
import os
from tables import gerar_tabelas   # Keep original name if external


# =================================================== #
# ====== FUNCTION TO GENERATE RANDOM SEED =========== #
# =================================================== #
def generate_random_decimal_seed(num_digits: int = 256) -> int:
    """
    Generates a cryptographically secure numeric seed with the specified number of digits.
    
    Args:
        num_digits (int): Number of decimal digits for the seed (default: 256)
    
    Returns:
        int: Numeric seed with exactly num_digits digits
    """
    random_bytes = os.urandom(num_digits // 2)  # each byte ≈ 2 digits
    large_number = int.from_bytes(random_bytes, "big")
    seed_str = str(large_number).zfill(num_digits)
    seed_str = seed_str[:num_digits]

    return int(seed_str)


# =================================================== #
# =================== ENCRYPTER ===================== #
# =================================================== #
def encrypter(
    plaintext: str = "",
    passes: list = [],
    seed: int = 0,
    dict_tables: dict = {},
    no_salt: bool = False,
    debug_mode: bool = False,
    min_table_len: int = 20,
    max_table_len: int = 999,
) -> list:
    """
    Encrypts text using substitution tables generated deterministically.
    
    Args:
        plaintext (str): Text to encrypt
        dict_tables (dict): Dictionary with substitution tables (optional)
        passes (list): List of passes to generate the key (optional)
        seed (int): Seed for deterministic generation (optional)
    
    Returns:
        list: [ciphertext, polished key]
    
    Raises:
        ValueError: If plaintext is not provided
    """

    # ===================== Validation ===================== #
    if not plaintext:
        raise ValueError("Mandatory parameter: plaintext must be a non-empty string")

    # ===================== Defaults ======================= #
    if not seed:
        seed = generate_random_decimal_seed(256)

    if not passes:
        p = len(plaintext)
        while p > 1:
            p -= 1
            passes.append(random.randint(min_table_len, max_table_len))

    if not dict_tables:
        dict_tables = gerar_tabelas(seed, passes)[0]

    # ===================== Variables ====================== #
    crude_ciphertext_list = []
    salt_ciphertext_list = []
    invalid_characters_list = []
    control_index = 0
    control_key = len(list(dict_tables.keys())) - 1

    # ================== Helper Functions ================== #
    def encipher_char(char: str) -> None:
        """Enciphers a single character using the current substitution table"""
        try:
            current_table = dict_tables[get_key_by_index(control_index)]
            crude_ciphertext_list.append(current_table[char])
        except KeyError:
            invalid_characters_list.append(char)

    def get_key_by_index(index: int, dict_: dict = dict_tables) -> int:
        """Gets the dictionary key by index"""
        return list(dict_.keys())[index]

    def create_salt(
        ciphertext_list: list = [],
        passes: list = [],
        seed: int = 0,
        min_len: int = 20,
        max_len: int = 100,
    ):
        """Adds salt into the ciphertext for entropy"""
        mini, maxi = min_len, max_len
        positions = []

        salt_len = random.randint(2, 2 + len(ciphertext_list))
        salt_ciphertext_list, salt_passes = [c for c in ciphertext_list], [p for p in passes]

        for _ in range(salt_len):
            salt_pass = random.randint(mini, maxi)
            pos = random.randint(0, (len(salt_ciphertext_list) - 1))

            tb = gerar_tabelas(seed, [salt_pass])
            salt_passes.insert(pos, salt_pass)
            salt_ciphertext_list.insert(pos, tb[0][salt_pass][chr(random.randint(65, 122))])
            positions.append(pos)

        return salt_ciphertext_list, salt_passes, positions

    def key_generator(passes: list = [], seed: int = 0, salt: list = []) -> list:
        """Generates the polished key for decryption"""
        seed_value = str(seed)
        formatted_passes = [str(p).zfill(3) for p in passes]
        formatted_salt = [str(s) for s in salt]

        pl = str(len(formatted_passes))
        lolp = str(len(str(pl))).ljust(3, "0")
        sl = str(len(seed_value))
        salt_l = str(len(salt))
        lol_salt = str(len(salt_l)).ljust(3, "0")

        crude_key = (
            f"\nsalt: lol_salt: {lol_salt}, salt_l: {[salt_l]}, salt positions: {formatted_salt}\n"
            f"passes + salt: lolp: {[lolp]}, pl: {[pl]}, passes: {formatted_passes}\n"
            f"seed: seed: {[sl]}, seed {[seed_value]}"
        )

        polished_key = "".join(
            [
                "".join(lol_salt),
                "".join(salt_l),
                "".join(formatted_salt),
                "".join(lolp),
                "".join(pl),
                "".join(formatted_passes),
                "".join(sl),
                "".join(seed_value),
            ]
        )

        return formatted_passes, polished_key, crude_key

    # ================== Ciphertext process ================= #
    for char in plaintext:
        encipher_char(char)
        control_index = 0 if control_index == control_key else control_index + 1

    if not no_salt:
        salt = create_salt(crude_ciphertext_list, passes, seed, 20, 100)
        salt_ciphertext_list = salt[0]
        ciphertext = "".join(salt_ciphertext_list)
        key = key_generator(salt[1], seed, salt[2])
    else:
        ciphertext = "".join(crude_ciphertext_list)
        key = key_generator(passes, seed, [])

    # ===================== Final Output ==================== #
    if debug_mode:
        return (
            f"Plaintext: {plaintext}\n"
            f"Ciphertext: {salt_ciphertext_list if not no_salt else crude_ciphertext_list}\n"
            f"Keys: {key[2]}\n"
            f"Invalid characters: {invalid_characters_list}\n"
        )
    else:
        return [ciphertext, key[1]]


# ===================== QUICK TEST ===================== #
if __name__ == "__main__":
    encry = encrypter(plaintext="axabaci", max_table_len=600)
    print(encry)
