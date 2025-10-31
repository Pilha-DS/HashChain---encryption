from HashChainClass import HashChainEncryption as HCE
HCO = HCE()

for _ in range(1):
    HCO.encrypt("This is a test message for encryption.")
    HCO.out(0)
    HCO.out(1)

    print()
    print("descriptografia:", HCO.decrypt(HCO.info(0), HCO.info(1), retonar=True))