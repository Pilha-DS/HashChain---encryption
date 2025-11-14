# HashChain Encryption (HCC)

HCC é um esquema de criptografia por cadeias de substituição determinísticas com inserção opcional de salt, implementado em Python. Ele gera tabelas de substituição por passe a partir de uma seed principal e permite reverter o processo com uma chave compacta que embute toda a informação necessária para a descriptografia.

## Sumário
- Visão geral
- Requisitos
- Instalação / Setup
- Conceitos-chave
- Uso rápido
- Formato da chave (com e sem salt)
- Modo debug
- Boas práticas e considerações

## Visão geral
- **Substituição determinística:** Para cada caractere do texto plano, é aplicada uma substituição conforme tabelas geradas a partir de uma seed e dos passes.
- **Múltiplos passes:** O texto é segmentado por uma sequência de comprimentos (passes). Cada parte usa uma tabela específica.
- **Salt opcional:** Itens aleatórios (determinísticos via seed) podem ser inseridos no ciphertext para elevar a entropia e ofuscação. As posições do salt são codificadas na chave.
- **Chave polida:** A chave gerada guarda comprimentos, passes, seed, e metadados de salt/padding, permitindo a descriptografia.

## Requisitos
- Python 3.11+ (testado também no Python 3.13)

## Instalação / Setup
Clonar o repositório:
```bash
git clone https://github.com/SEU-USER/HashChain---encryption.git
cd HashChain---encryption
```
há dependências externas; o projeto usa biblioteca padrão do Python, e algumas mais avançadas como customTKinter, Secrets, TKinter.

## Conceitos-chave
- **Passes (`pass_`)**: lista de inteiros (3 dígitos na chave) que define como o ciphertext é segmentado e qual tabela usar por segmento.
- **Seed principal (`seed`)**: inteiro decimal que determina todas as seeds derivadas por passe e pelo salting.
- **Salt (opcional)**: strings inseridas em posições pseudoaleatórias, com base no `seed`. As posições e metadados são codificados na chave.
- **Padding (opcional)**: número de caracteres '1' adicionados ao final do ciphertext para adequar o comprimento quando necessário; a quantidade é guardada na chave.

## Uso rápido
### Exemplo mínimo
```python
from HashChainClass import HashChainEncryption

H = HashChainEncryption()
plaintext = "Mensagem secreta"

# Criptografar (com salt por padrão)
ciphertext, key = H.encrypt_(plaintext)

# Descriptografar
texto_original = H.decrypt_(ciphertext, key)
print(texto_original)
```

### Sem salt
```python
ciphertext, key = H.encrypt_("ABC", no_salt=True)
print(H.decrypt_(ciphertext, key))
```

### Com parâmetros customizados
```python
ciphertext, key = H.encrypt_(
    plaintext="Hello, HCC!",
    pass_=[25, 30, 18],  # tamanhos dos segmentos/passes
    seed=12345678901234567890,
    no_salt=False,
    min_table_leng=20,
    max_table_leng=999,
)
```

## API da classe `HashChainEncryption`
### `encrypt_(plaintext: str, pass_: list | None = None, seed: int = 0, no_salt: bool = False, debug_mode: bool = False, min_table_leng: int = 20, max_table_leng: int = 999)`
- **Retorno (modo normal):** `[ciphertext, key]`.
- **Comportamento:**
  - Gera passes automaticamente se `pass_` não for informado.
  - Gera `seed` decimal longa por padrão se não informada.
  - Insere salt quando `no_salt=False` (padrão); remove ou ajusta padding conforme necessário.
- **Modo debug:** ver seção “Modo debug”.

### `decrypt_(ciphertext: str | None, key: str | None) -> str`
- Aceita chaves com ou sem seção de salt (auto-detecta o formato):
  - Tenta parsear como “com salt”; se falhar, tenta “sem salt”.
- Remove automaticamente sequências ANSI caso `ciphertext`/`key` tenham sido copiadas de uma saída colorida.
- Se `ciphertext`/`key` vierem vazios/nulos, tenta usar `self._info` (quando preenchido por uma execução de `encrypt_` em modo normal).
- Retorna o texto plano.

### `info(search: str | int | None) -> str | None`
- Retorna um dos valores armazenados da última criptografia realizada em modo normal.
- `search` pode ser:
  - Índice: `0` (ciphertext), `1` (key), `2` (ciphertext – alias), `3` (plaintext)
  - Ou alias string: `"compressed"/"cipher"/"key"/"plain"` etc.
- Retorna `None` caso ainda não haja dados armazenados.

### `out(output: str | int = 0) -> None`
- Imprime um dos itens armazenados ou todos, conforme o parâmetro.

## Formato da chave
A chave “polida” concatena campos em sequência. As seções variam conforme o uso de salt.

### Com salt (resumo)
- `lol_salt` (3 dígitos) — comprimento do campo `salt_l`.
- `salt_l` — quantidade de posições de salt.
- `posicoes` — para cada posição, 3 dígitos indicando o número de dígitos do índice seguido do índice em si.
- `lol_p` (3 dígitos) e depois `pl` — quantidade total de passes e seu comprimento.
- `passes` — `pl` entradas de 3 dígitos cada.
- `sl` (3 dígitos) e depois `seed` — comprimento e valor da seed decimal.
- `padding` (opcional, ao final) — quantidade de '1' adicionados.

### Sem salt (resumo)
- `lol_p`, `pl`, `passes`, `sl`, `seed`, `padding` (opcional). Não inclui `lol_salt`, `salt_l` e `posicoes`.

Observação: o parser da chave valida consistência de comprimentos e soma dos segmentos com o comprimento do ciphertext (após remover padding, quando existir).

## Modo debug
- Ativar com `debug_mode=True` em `encrypt_`.
- A função apenas imprime informações coloridas (plaintext, lista de ciphertext, seeds por passe, chave detalhada e polida, caracteres inválidos, ciphertext final).
- **Não** retorna valores e **não** grava estado em `self._info`.
- Use o modo normal (sem `debug_mode`) para produzir `ciphertext` e `key` utilizáveis diretamente por `decrypt_`.

## Boas práticas e considerações
- Guarde sua `key` com segurança; ela contém tudo o que é necessário para reverter a criptografia.
- Para alta variabilidade, use seeds longas e deixe `no_salt=False`.
- Caso copie `ciphertext`/`key` de uma saída colorida, `decrypt_` remove sequências ANSI automaticamente.
- `min_table_leng` não deve ser menor que `20` e `max_table_leng` não deve exceder `999`.

## Executando o exemplo `main.py`
Um exemplo simples de uso pode estar em `main.py`. Ajuste conforme seu fluxo:
```python
from HashChainClass import HashChainEncryption

def main():
    H = HashChainEncryption()
    ct, k = H.encrypt_("Teste HCC")
    print("Ciphertext:", ct)
    print("Key:", k)
    print("Decrypted:", H.decrypt_(ct, k))

if __name__ == "__main__":
    main()
```

## Licença
Linceça MIT
