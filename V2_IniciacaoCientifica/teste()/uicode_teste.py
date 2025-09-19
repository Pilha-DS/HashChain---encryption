import time
import os
import psutil

class BiDict:
    def __init__(self):
        self.forward = {}
        self.backward = {}

    def add(self, key, value):
        self.forward[key] = value
        self.backward[value] = key

    def get_hash(self, key):
        return self.forward.get(key)

    def get_char(self, value):
        return self.backward.get(value)


# ========= Início ==========
start = time.perf_counter()
process = psutil.Process(os.getpid())

print(f"RSS inicial: {process.memory_info().rss / 1024**2:.2f} MB")

# Lê 1 MB de caracteres
with open("Testes/unicode_full.txt", "r", encoding="utf_8") as file:
    content = file.read(1_048_576)

print(f"RSS após abrir arquivo: {process.memory_info().rss / 1024**2:.2f} MB")

# Criação das tabelas
table = BiDict()

for n, char in enumerate(content):
    table.add(char, n)  # guarda o inteiro em vez da string "#*"

print(f"RSS após criar tabela: {process.memory_info().rss / 1024**2:.2f} MB")

# Função para converter int → "#*"
symbols = str.maketrans("01", "#*")
def int_to_hash(num, bits=20):
    return f"{num:0{bits}b}".translate(symbols)

# Testes
hash_ç = int_to_hash(table.get_hash("ç"))
print("Hash de ç:", hash_ç)
print("Char do hash:", table.get_char(table.get_hash("ç")))

end = time.perf_counter()
print(f"Tempo total: {end - start:.4f}s")
