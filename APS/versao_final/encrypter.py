# Imports
from tables import generate_tables
import random
import os

def generate_secure_decimal_seed(num_digits: int = 256) -> int:
    """
    Generates a cryptographically secure numeric seed with the specified number of digits.
    
    Args:
        num_digits (int): Number of decimal digits desired for the seed (default: 256)
    
    Returns:
        int: Numeric seed with exactly num_digits digits
    """
    # Generate cryptographically secure random bytes
    random_bytes = os.urandom(num_digits // 2)  # Each byte represents approximately 2 decimal digits
    
    # Convert bytes to arbitrary precision integer
    large_number = int.from_bytes(random_bytes, 'big')
    
    # Format to ensure exactly num_digits digits
    seed_str = str(large_number).zfill(num_digits)
    seed_str = seed_str[:num_digits]  # Ensure exact length
    
    return int(seed_str)

def encrypt(plaintext: str = "",
            substitution_tables: dict = {},
            passes: list = [],
            min_table_length: int = 20,
            max_table_length: int = 300,
            seed: int = 0) -> list:
    """
    Encrypts text using deterministically generated substitution tables.
    
    Args:
        plaintext (str): Text to be encrypted
        substitution_tables (dict): Dictionary with substitution tables (optional)
        passes (list): List of passes for key generation (optional)
        min_table_length (int): Minimum table length for random generation (optional)
        max_table_length (int): Maximum table length for random generation (optional)
        seed (int): Seed for deterministic generation (optional)
    
    Returns:
        list: List containing [ciphertext, key, invalid_characters]
    
    Raises:
        ValueError: If plaintext is not provided
    """
    # Input parameter validation
    if not plaintext: 
        raise ValueError('Required parameter: plaintext must be a non-empty string')
    
    # Default value generation for optional parameters
    if not seed:
        seed = generate_secure_decimal_seed(256)
    
    if not passes:
        # Generate random passes based on text length
        p = len(plaintext)
        while p > 1:
            p -= 1
            passes.append(random.randint(min_table_length, max_table_length))
    
    if not substitution_tables:
        # Generate substitution tables using provided seed and passes
        substitution_tables = generate_tables(seed, passes)[0]
    
    # Encryption process state variables
    ciphertext_list = []
    invalid_characters_list = []
    key = []
    control_index = 0
    control_key = len(list(substitution_tables.keys())) - 1

    def encipher(character: str) -> None:
        """
        Applies cryptographic substitution using appropriate tables.
        
        Args:
            character (str): Character to be encrypted
        """
        try:
            # Get substitution from appropriate table
            current_table = substitution_tables[get_key_by_index(control_index)]
            ciphertext_list.append(current_table[character])
        except KeyError:
            # Record characters not mapped in tables
            invalid_characters_list.append(character)
    
    def get_key_by_index(index: int) -> int:
        """
        Gets dictionary key based on current index.
        
        Args:
            index (int): Index of desired key
        
        Returns:
            int: Key corresponding to the index
        """
        return list(substitution_tables.keys())[index]
    
    def generate_key(pass_list: list, seed_value: int) -> list:
        """
        Generates a cryptographic key from passes and seed.
        
        Args:
            pass_list (list): List of numeric passes
            seed_value (int): Seed value for key derivation
        
        Returns:
            list: Formatted generated key
        """
        crude_key = []
        
        # Format passes to have 3 digits each
        for p in pass_list:
            formatted_pass = str(p).zfill(3)
            crude_key.append(formatted_pass)
        
        # Calculate metadata for key incorporation
        total_length = len(''.join(crude_key))
        length_digits = len(str(total_length))
        
        # Combine all components to form the key
        final_key = [
            ''.join(crude_key),
            str(seed_value),
            str(total_length),
            str(length_digits)
        ]
        
        return [''.join(final_key)]

    # Main encryption process
    for character in plaintext:
        if control_index == control_key:
            encipher(character)
            control_index = 0
        else:
            encipher(character)
            control_index += 1
    
    # Final key generation
    key = generate_key(passes, seed)
    
    # Final ciphertext construction
    ciphertext = ''.join(ciphertext_list)
    
    # Cleanup of sensitive variables
    ciphertext_list.clear()
    invalid_characters_list.clear()
    passes.clear()
    substitution_tables.clear()
    
    return [ciphertext], key, invalid_characters_list

# Usage example
encryption_result = encrypt(plaintext="axabaci")
print(encryption_result)