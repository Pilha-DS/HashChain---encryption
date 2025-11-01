# Inputs imports and dependencies
class InputCollector:
    def __init__(self):
        pass
    
    def get_action(Stable: bool) -> int:
        while Stable:
            action = input("\nEscolha uma ação:\n1. Criptografar Texto\n2. Descriptografar Texto\n3. Comprimir Texto\n4. Descomprimir Texto\n5. Sair\n\nDigite o número da ação desejada: ").strip()

            if action not in ["1", "2", "3", "4", "5"]:
                print("\nAção inválida. Tente novamente.")
                continue
            action = int(action)
        return action

    def get_action_() -> str:
        # Prints Menu
        print(f"[C]: Criptografar | [D]: Descriptografar | [S]: Sair")

        # Initializes user_choice
        user_choice: str = ""

        while user_choice not in ["c", "d", "s"]:
            user_choice: str = input(": ").strip().lower()

            if user_choice == "s":
                print("Closing")
                exit()

            try:
                if user_choice not in ["c", "d"]:
                    raise Exception(
                        "Invalid user actions, must be [C] or [D] to proceed."
                    )
            except Exception as e:
                print(e)

        return user_choice

    def get_seed_() -> int:
        seed: int = 0

        while len(str(seed)) < 8 or not isinstance(seed, int):
            seed = input("Digite uma seed de no minimo 8 digitos: ")

            try:
                if len(str(seed)) < 8:
                    raise Exception("A seed deve ter no minimo 8 digitos.")
                seed = int(seed)
            except Exception as e:
                print("Erro: ", e, " Digite uma seed valida (int).")

        return seed

    def get_passes_() -> list[int]:

        def is_valid_pass_(passos: list[int]) -> bool:
            if len(str(passos)) <= 0:
                return False
            for _, passo in enumerate(passos):
                if not isinstance(passo, int) or passo < 20 or passo > 999:
                    return False

            return True

        def conver_input_(raw_passos: str) -> list[int] | int:
            valid_chars: list[str] = [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                " ",
            ]
            raw_passos += " "
            passos: list[int] = []
            aux: list[str] = []
            try:
                for char in raw_passos:
                    if char not in valid_chars:
                        raise Exception("Caractere inválido.")
                    if char != " ":
                        aux.append(char)
                    elif char == " ":
                        passos.append(int("".join(aux)))
                        aux: list[str] = []
            except Exception as e:
                print(e)
                return [-1]

            return passos

        print("Escolha a sequencia de passos: ")

        while True:
            raw_passos: str = input(
                "Digite os passos separados por espaços, cada um sendo um inteiro de 20 a 999. (Exemplo: 20 450 999): "
            )
            passos: list[int] = conver_input_(raw_passos)
            if is_valid_pass_(passos):
                break
            print(
                "Input inválido. Passes devem ser inteiros de 20 a 999. Tente novamente."
            )

        return passos


# Handlers imports and dependencies
import json
import importlib.util
from pathlib import Path

# Global

# Terminal colors
r = '\033[0m'      # Reset
red = '\033[0;31m' # Red
green = '\033[0;32m' # Green
yellow = '\033[0;33m' # Yellow
blue = '\033[0;34m' # Blue
white = '\033[0;37m' # White
black = '\033[0;30m' # Black
cyan = '\033[0;36m' # Cyan
purple = '\033[0;35m' # Purple
gray = '\033[0;90m' # Gray

# Estilos
bold = '\033[1m'       # Bold
italic = '\033[3m'     # Italic
underline = '\033[4m'  # Underline

class Handler:
    def __init__(self):
        pass

    def find_config_file() -> Path | None:
        start_path = Path(".")
        expected_id = 25599852140000
        for path in start_path.rglob("config.json"):  # procura recursivamente
            try:
                with open(path, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    if expected_id is None or data.get("idd") == expected_id:
                        print(f"\nArquivo de configuração encontrado em: {italic}{path}{r}")
                        return path
                    else:
                        print(f"{bold}Ignorando {path}, id diferente ({data.get('idd')}).{r}")
            except (json.JSONDecodeError, OSError) as e:
                print(f"Erro ao ler {path}: {e}")
        print(f"\n{bold}Erro:{r} O arquivo de configurações {bold}'config.json' não foi encontrado no diretório.{r}")
        print(f"{italic} - As opções de criptografia padronizadas{r} {bold}não estarão disponíveis.{r}")
        return None
    
    def load_config(config_path) -> dict[str, bool] | None:
        if config_path is None:
            config = {}
            config["terminal_mode"] = True
            return config
        else:
            try:
                with open(config_path, "r") as config_file:
                    config = json.load(config_file)
                    print(f"{italic} - Configurações carregadas com sucesso.{r}")
                    return config
            except FileNotFoundError:
                print(f" - {italic}Erro: O arquivo de configurações {r}{bold}'config.json' não foi encontrado no diretório.{r}")
            except json.JSONDecodeError:
                print(f" - {italic}Erro: Falha ao decodificar o arquivo {r}{bold}'config.json'.{r} Verifique sua integridade.")
                
    def verify_required_modules():
        dependencies = ["tkinter", "customtkinter"]
        for module in dependencies:
            if importlib.util.find_spec(module) is not None:
                print(f"Atualemte o módulo \033[1m{module}\033[0m está instalado.")
            else:
                print(f"Atualemte o módulo \033[1m{module} não está instalado\033[0m, rode o seguinte comando no terminal para instalar:\npip install \033[1m{module}\033[0m")
        has_dependencies = True if all(importlib.util.find_spec(module) is not None for module in dependencies) else False
        if not has_dependencies:
            print(f"{italic}Para instalar utilizando o {r}{bold}pip{r}{italic}, é necessário ter o pip {r}{bold}instalado e configurado no PATH do sistema.{r}")
            print(f"Por opção dos criadores, decidimos não forçar a instalação do pip e dos módulos necessários necessários para utilização a interface gráfica, pois, consideramos essa prática como {bold}intrusiva{r}, e acreditamos que o usuário deve ter controle sobre o que é instalado em seu sistema.")
        
        return has_dependencies
    
    def save_config(config, config_path):
        if config_path is None:
            print("Programa encerrado.")
            raise SystemExit
        elif config_path is not None:
            try:
                with open(config_path, "w") as config_file:
                    json.dump(config, config_file, indent=4)
            except FileNotFoundError:
                print(f"{bold}Erro: O arquivo de configurações 'config.json' não foi encontrado no diretório.{r}")
            except json.JSONDecodeError:
                print(f"{bold}Erro: Falha ao decodificar o arquivo 'config.json'. Verifique sua integridade.{r}")
        print("\nPrograma encerrado.\n")
        raise SystemExit
