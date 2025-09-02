import random
import tabelas
from grafador import grafar
from desgrafar import desgrafar


def pular_linha():
    print(" ")


def gerar_seed_manual() -> int:
    return int(input("Digite a seed: "))


def gerar_seed_aleatoria() -> int:
    return int("".join(str(random.randint(0, 9)) for _ in range(8)))


def ler_passos() -> list[int]:
    """
    Lê do usuário uma sequência de passos separados por espaço
    Exemplo: 9 21 11
    """
    entrada = input('Digite os passos (exemplo: 9 21 11): ')
    return [int(x) for x in entrada.split()]


def gerar_tabela(seed: int, passos: list[int]):
    if passos == [0]:
        return tabelas.gerar_tabelas(seed)
    else:
        return tabelas.gerar_tabelas(seed, min(passos), max(passos))


def criptografar():
    texto = input("Texto que irá criptografar: ")
    pular_linha()

    usar_seed = input("Usar seed? [s/n]: ").strip().lower()
    if usar_seed in {"s", "sim"}:
        seed = gerar_seed_manual()
    else:
        seed = gerar_seed_aleatoria()
    print(f"Seed escolhida: {seed}")
    pular_linha()

    usar_passos = input("Usar passo? [s/n]: ").strip().lower()
    passos = ler_passos() if usar_passos in {"s", "sim"} else [0]
    print(f"Passos: {passos}")
    pular_linha()

    tabela = gerar_tabela(seed, passos)
    grafo = grafar(texto, tabela, passos, True, seed)

    print(f"Grafo: {grafo[0]}")
    print(f"Seed: {grafo[-1]}")
    print(f"Passos usados: {grafo[1]}")
    pular_linha()


def descriptografar():
    texto = input("Texto que irá descriptografar: ")
    print(f"Entrada: {texto}")
    pular_linha()

    chave = input("Chave [a] Semi-automática ou [m] Manual? ").strip().lower()
    if chave.startswith("m"):  # manual
        seed = gerar_seed_manual()
        passos = ler_passos()
        print(f"Passos: {passos}")
        pular_linha()

        tabela = gerar_tabela(seed, passos)
        tabela_invertida = {k: {v: kk for kk, v in d.items()} for k, d in tabela.items()}

        desgrafo = desgrafar(texto, passos, tabela_invertida)
        print(f"Texto descriptografado: {desgrafo}")


def main():
    possiveis_acoes = {
        "crip": {"c", "crip", "criptografar", "grafar"},
        "dcri": {"d", "dcri", "descriptografar", "desgrafar"},
        "comp": {"com", "compactar"},
        "desc": {"des", "descompactar"},
    }

    while True:
        print("[c] Criptografar | [d] Descriptografar | [com] Compactar | [des] Descompactar")
        acao = input("Escolha: ").strip().lower()
        pular_linha()

        if acao in possiveis_acoes["crip"]:
            criptografar()
        elif acao in possiveis_acoes["dcri"]:
            descriptografar()
        elif acao in possiveis_acoes["comp"]:
            print("⚠️ Compactar ainda não implementado.")
        elif acao in possiveis_acoes["desc"]:
            print("⚠️ Descompactar ainda não implementado.")
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    main()
