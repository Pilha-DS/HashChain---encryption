from encrypter import encrypter

def testar_vulnerabilidades():
    # Teste 1: Verificar se a mesma entrada produz saída diferente
    print("=== TESTE 1: Aleatoriedade ===")
    texto = "hello"
    resultado1 = encrypter(plaintext=texto, max_table_leng=600)
    resultado2 = encrypter(plaintext=texto, max_table_leng=600)
    
    print(f"Texto: {texto}")
    print(f"Ciphertext 1: {resultado1['poli'][0][0][:50]}...")
    print(f"Ciphertext 2: {resultado2['poli'][0][0][:50]}...")
    print(f"São diferentes? {resultado1['poli'][0][0] != resultado2['poli'][0][0]}")
    
    # Teste 2: Verificar padrões em textos repetitivos
    print("\n=== TESTE 2: Padrões em repetição ===")
    texto_repetitivo = "aaa"
    resultado = encrypter(plaintext=texto_repetitivo, max_table_leng=600, no_salt=True)
    ciphertext_sem_salt = resultado['crude'][0]
    
    print(f"Texto: {texto_repetitivo}")
    print(f"Ciphertext (sem salt): {ciphertext_sem_salt}")
    print(f"Os 'a' são cifrados igualmente? {ciphertext_sem_salt[0] == ciphertext_sem_salt[1] == ciphertext_sem_salt[2]}")
    
    # Teste 3: Análise de distribuição
    print("\n=== TESTE 3: Distribuição de caracteres ===")
    texto_longo = "a" * 100 + "b" * 100
    resultado = encrypter(plaintext=texto_longo, max_table_leng=600, no_salt=True)
    ciphertext = resultado['crude'][0]
    
    count_0 = ciphertext.count('0')
    count_1 = ciphertext.count('1')
    total = len(ciphertext)
    
    print(f"Total de bits: {total}")
    print(f"Zeros: {count_0} ({count_0/total*100:.2f}%)")
    print(f"Uns: {count_1} ({count_1/total*100:.2f}%)")
    
    # Teste 4: Verificar dependência da seed
    print("\n=== TESTE 4: Dependência da seed ===")
    seed_fixa = 123456789
    texto = "test"
    
    resultado1 = encrypter(plaintext=texto, seed=seed_fixa, max_table_leng=600, no_salt=True)
    resultado2 = encrypter(plaintext=texto, seed=seed_fixa, max_table_leng=600, no_salt=True)
    
    print(f"Com seed fixa, cifras são idênticas? {resultado1['crude'][0] == resultado2['crude'][0]}")

# Executar testes
testar_vulnerabilidades()