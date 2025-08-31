from grafias import grafar, desgrafar
from tabelas import generate_tables

# desgrafar("texo", keys[7, 8, 9])

def main():
    seed_input: int = int(input("Escolha a seed q deseja usar: "))
    print(generate_tables(seed=seed_input))
    user_choice: str | None = None
    while user_choice != "s":
        user_choice: str = (input("[c] Criptografar | [d] Descriptografar | [s] Sair : ")).lower()
        if user_choice == "c":
            grafar(input("texto a grafar: "))
        elif user_choice == "d":
            user_input: str = input("Texto a desgrafar: ")
            chaves: list[int] | str = input("Enter the key separated by commas (ex: 7, 8, 9): ")
            chaves = chaves.split(", ")
            for i, e in enumerate(chaves):
                chaves[i] = int(chaves[i])
            print(chaves)

            desgrafar(user_input, chaves)


if __name__ == "__main__":
    main()
