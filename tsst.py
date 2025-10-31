from HashChainClass import HashChainEncryption
h = HashChainEncryption()
h.encrypt("This is a test message for encryption.")
h.out()
# Workaround: pass the uncompressed ciphertext (index 2) to avoid possible
# compression/format parsing issues when providing the compressed value (index 0).
ct = h.info(2)
key = h.info(1)
print("DEBUG: ciphertext length (uncompressed):", len(ct) if ct else None)
print("DEBUG: key length:", len(key) if key else None)
print(h.decrypt(ct, key))