from grafias import grafar, desgrafar
from APS.outdated.tables import gerar_tabelas

# desgrafar("texo", keys[7, 8, 9])

def main():
    seed_input: int = int(input("Escolha a seed q deseja usar: "))
    print(gerar_tabelas(seed=seed_input))
    t = gerar_tabelas(seed=seed_input)
    t_inverse = {k: {v: kk for kk, v in d.items()} for k, d in t.items()}
    
    user_choice: str | None = None
    
    while user_choice != "s":
        user_choice: str = (input("[c] Criptografar | [d] Descriptografar | [s] Sair : ")).lower()
        if user_choice == "c":
            ent = input("texto a grafar: ")
            chaves: list[int] | str = input("Enter the key separated by commas (ex: 7, 8, 9): ")
            chaves = chaves.split(", ")
            for i, e in enumerate(chaves):
                chaves[i] = int(chaves[i])
            print(grafar(ent, t, chaves))
        elif user_choice == "d":
            user_input: str = input("Texto a desgrafar: ")
            chaves: list[int] | str = input("Enter the key separated by commas (ex: 7, 8, 9): ")
            chaves = chaves.split(", ")
            for i, e in enumerate(chaves):
                chaves[i] = int(chaves[i])
            print(chaves)

            desgrafar(user_input, chaves, t_inverse)


if __name__ == "__main__":
    main()
