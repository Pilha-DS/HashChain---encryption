import tabelas
from grafador import grafar
import random
from desgrafar import desgrafar

def pular_linha():
    print(" ")

while True:
    # variaveis L
    seed = 0
    x = 0
    pas = []
    texto_mod = ""
    acao = ""
    passo = []
    menor_passo = 999
    maior_passo = 0
    possiveis_acoes = {
    "dcri" : {"d", "D", "Descriptografar", "descriptografar", "Desgrafar", "desgrafar"},
    "crip" : {"c", "C", "Criptografar", "criptografar", "Grafar", "grafar"},
    "comp" : {"Compactar", "compactar", "com", "Com", "COM"},
    "desc" : {"Descompactar", "descompactar", "des", "Des", "DES"},
    "sim" : {"sim", "SIM", "Sim", "s", "S"},
    "nao" : {"NAO", "NÃO", "Não", "Nao", "nao", "não", "N", "n"},
    "auto" : {"a", "A", "Auto", "auto", "automatica", "Automatica", "AUTO"},
    "manual" : {"M", "m", "Manual", "manual", "MANUAL"}
    }
    cor_terminal = {
    "vermelho" : "", 
    }

    # inicio
    print('Escolha : [d] para Descriptografar : [c] para Criptografar : [com] para Compactar : [des] para Descompactar')
    acao = input("escolha:  ")
    pular_linha()
    
    # criptografar
    if acao in possiveis_acoes["crip"]:
        texto_mod = input("Texto que irá criptar: ")
        pular_linha()

        # perguntar se irá usar seed
        print('Escolha : [s] para Sim : [n] para Não')
        print("Voce ira usar seed?")
        acao = input("escolha:  ")
        pular_linha()

        if acao in possiveis_acoes["sim"]:
            seed = int(input("Digite a seed: "))
            pular_linha()

        elif acao in possiveis_acoes["nao"]:
            sed = []
            for c in range(1, 9):
                x += 1
                print(x)
                sed.append(str(random.randint(0, 9)))
            else:
                x = 0
                seed = "".join(sed)
                seed = int(seed)
        print(f"seed: ({seed})")
        pular_linha()

        # perguntar se irá usar passo
        print('Escolha : [s] para Sim : [n] para Não')
        print("Voce irá usar passo?")
        acao = input("Escolha: ")
        pular_linha()

        if acao in possiveis_acoes["sim"]:
            passor = input('Digite o passo separe com espaço " " e o numero de passos não pode ser superior ao numero de caracteres. exemplo:(9 21 11): ')
            for c in passor:
                if c != " ":
                    pas.append(c)
                elif c == " ":
                    passo.append(int("".join(pas)))
                    pas.clear()
            else:
                passo.append(int("".join(pas)))
                pas.clear()
        elif acao in possiveis_acoes["nao"]:
            passo = [0]
        print(passo)
        pular_linha()

        # ver menor numero do passo e maior
        for x in passo:
            if x < menor_passo:
                menor_passo = x
            if x > maior_passo:
                maior_passo = x


        # criar tabela
        if passo == [0]:
            tabela = tabelas.gerar_tabelas(seed)
        else:
            tabela = tabelas.gerar_tabelas(seed, menor_passo, maior_passo)
        print(tabela)
        pular_linha()
        
        # chamar funcao que criptografa
        grafo = grafar(texto_mod, tabela, passo, True, int(seed))

        print(f"Grafo: ({grafo[0]}) : seed: ({grafo[-1]}) : passe: ({grafo[1]})")
        pular_linha()

    # desgrafar
    elif acao in possiveis_acoes["dcri"]:
        texto_mod = input("Escreva testo que irá descriptar: ")
        print(f"Grifo: ({texto_mod})")
        pular_linha()
        print('Escolha : [a] para Chave Semi-Automatica : [m] para Chave Manual')
        acao = input("Escolha: ")
        pular_linha()

        if acao in possiveis_acoes["manual"]:
            seed = int(input("Digite a seed: "))
            passor = input('Digite o passo separe com espaço " " e o numero de passos não pode ser superior ao numero de caracteres. exemplo:(9 21 11): ')
            pular_linha()
            
            for c in passor:
                if c != " ":
                    pas.append(c)
                elif c == " ":
                    passo.append(int("".join(pas)))
                    pas.clear()
            else:
                passo.append(int("".join(pas)))
                pas.clear()
            
            for x in passo:
                if x < menor_passo:
                    menor_passo = x
                if x > maior_passo:
                    maior_passo = x
            print(passo)
            pular_linha()

            tabela = tabelas.gerar_tabelas(seed, menor_passo, maior_passo)
            print(tabela)
            pular_linha()
            
            t_invertida = {k: {v: kk for kk, v in d.items()} for k, d in tabela.items()}
            print(t_invertida)
            pular_linha()

            desgrafo = desgrafar(texto_mod, passo, t_invertida)