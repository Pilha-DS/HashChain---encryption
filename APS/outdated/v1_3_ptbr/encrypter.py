# =================================================== #
# ===================== IMPORTS ===================== #
# =================================================== #
import random
import os
from tables import gerar_tabelas


# =================================================== #
# ====== FUNÇÃO PARA GERAR SEED ALEATÓRIA =========== #
# =================================================== #
def gerar_seed_decimal_aleatoria(num_digitos: int = 256) -> int:
    """
    Gera uma seed numérica criptograficamente segura com o número especificado de dígitos.
    
    Args:
        num_digitos (int): Número de dígitos desejados para a seed (padrão: 256)
    
    Returns:
        int: Seed numérica com exatamente num_digitos dígitos
    """
    bytes_aleatorios = os.urandom(num_digitos // 2)  # cada byte ≈ 2 dígitos
    numero_grande = int.from_bytes(bytes_aleatorios, "big")
    seed_str = str(numero_grande).zfill(num_digitos)
    seed_str = seed_str[:num_digitos]

    return int(seed_str)


# =================================================== #
# =================== CRIPTOGRAFAR ================== #
# =================================================== #
def criptografar(
    texto: str = "",
    passes: list = [],
    seed: int = 0,
    tabelas: dict = {},
    sem_salt: bool = False,
    modo_debug: bool = False,
    min_tam_tabela: int = 20,
    max_tam_tabela: int = 999,
) -> list:
    """
    Criptografa um texto utilizando tabelas de substituição geradas deterministicamente.
    
    Args:
        texto (str): Texto a ser criptografado
        tabelas (dict): Dicionário com tabelas de substituição (opcional)
        passes (list): Lista de passes para geração da chave (opcional)
        seed (int): Seed para geração determinística (opcional)
    
    Returns:
        list: [texto_cifrado, chave_polida]
    
    Raises:
        ValueError: Se o texto não for fornecido
    """

    # ===================== Validação ===================== #
    if not texto:
        raise ValueError("Parâmetro obrigatório: texto deve ser uma string não vazia")

    # ===================== Valores padrão ================ #
    if not seed:
        seed = gerar_seed_decimal_aleatoria(256)

    if not passes:
        p = len(texto)
        while p > 1:
            p -= 1
            passes.append(random.randint(min_tam_tabela, max_tam_tabela))

    if not tabelas:
        tabelas = gerar_tabelas(seed, passes)[0]

    # ===================== Variáveis ===================== #
    lista_cifra_bruta = []
    lista_cifra_com_salt = []
    caracteres_invalidos = []
    indice_controle = 0
    chave_controle = len(list(tabelas.keys())) - 1

    # ================== Funções internas ================= #
    def cifrar_caractere(caractere: str) -> None:
        """Mapeia um caractere para a substituição correspondente"""
        try:
            tabela_atual = tabelas[obter_chave_por_indice(indice_controle)]
            lista_cifra_bruta.append(tabela_atual[caractere])
        except KeyError:
            caracteres_invalidos.append(caractere)

    def obter_chave_por_indice(indice: int, dict_: dict = tabelas) -> int:
        """Obtém a chave do dicionário pelo índice"""
        return list(dict_.keys())[indice]

    def criar_salt(
        lista_cifra: list = [],
        passes: list = [],
        seed: int = 0,
        min_len: int = 20,
        max_len: int = 100,
    ):
        """Insere salt no texto cifrado para aumentar a entropia"""
        mini, maxi = min_len, max_len
        posicoes = []

        tam_salt = random.randint(2, 2 + len(lista_cifra))
        lista_cifra_com_salt, passes_com_salt = [c for c in lista_cifra], [p for p in passes]

        for _ in range(tam_salt):
            passe_salt = random.randint(mini, maxi)
            posicao = random.randint(0, (len(lista_cifra_com_salt) - 1))

            tb = gerar_tabelas(seed, [passe_salt])
            passes_com_salt.insert(posicao, passe_salt)
            lista_cifra_com_salt.insert(posicao, tb[0][passe_salt][chr(random.randint(65, 122))])
            posicoes.append(posicao)

        return lista_cifra_com_salt, passes_com_salt, posicoes

    def gerar_chave(passes: list = [], seed: int = 0, salt: list = []) -> list:
        """Gera a chave polida para descriptografia posterior"""
        valor_seed = str(seed)
        passes_formatados = [str(p).zfill(3) for p in passes]
        salt_formatado = [str(s) for s in salt]

        pl = str(len(passes_formatados))
        lolp = str(len(str(pl))).ljust(3, "0")
        sl = str(len(valor_seed))
        salt_l = str(len(salt))
        lol_salt = str(len(salt_l)).ljust(3, "0")

        chave_crua = (
            f"\nsalt: lol_salt: {lol_salt}, salt_l: {[salt_l]}, posições salt: {salt_formatado}\n"
            f"passes + salt: lolp: {[lolp]}, pl: {[pl]}, passes: {passes_formatados}\n"
            f"seed: seed: {[sl]}, seed {[valor_seed]}"
        )

        chave_polida = "".join(
            [
                "".join(lol_salt),
                "".join(salt_l),
                "".join(salt_formatado),
                "".join(lolp),
                "".join(pl),
                "".join(passes_formatados),
                "".join(sl),
                "".join(valor_seed),
            ]
        )

        return passes_formatados, chave_polida, chave_crua

    # ================== Processo de cifra ================ #
    for caractere in texto:
        cifrar_caractere(caractere)
        indice_controle = 0 if indice_controle == chave_controle else indice_controle + 1

    if not sem_salt:
        salt = criar_salt(lista_cifra_bruta, passes, seed, 20, 100)
        lista_cifra_com_salt = salt[0]
        texto_cifrado = "".join(lista_cifra_com_salt)
        chave = gerar_chave(salt[1], seed, salt[2])
    else:
        texto_cifrado = "".join(lista_cifra_bruta)
        chave = gerar_chave(passes, seed, [])

    # ===================== Saída final =================== #
    if modo_debug:
        return (
            f"Texto original: {texto}\n"
            f"Texto cifrado: {lista_cifra_com_salt if not sem_salt else lista_cifra_bruta}\n"
            f"Chaves: {chave[2]}\n"
            f"Caracteres inválidos: {caracteres_invalidos}\n"
        )
    else:
        return [texto_cifrado, chave[1]]


# ===================== TESTE RÁPIDO ================== #
if __name__ == "__main__":
    cript = criptografar(texto="axabaci", max_tam_tabela=600)
    print(cript)
