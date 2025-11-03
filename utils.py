# Inputs imports and dependencies
class InputCollector:
    def __init__(self):
        pass

    def get_action(Stable: bool) -> int:
        while Stable:
            action = input(
                "\nEscolha uma ação:\n1. Criptografar Texto\n2. Descriptografar Texto\n3. Comprimir Texto\n4. Descomprimir Texto\n5. Sair\n\nDigite o número da ação desejada: "
            ).strip()

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
import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox
import importlib.util
from pathlib import Path

# Global

# Terminal colors
r = "\033[0m"  # Reset
red = "\033[0;31m"  # Red
green = "\033[0;32m"  # Green
yellow = "\033[0;33m"  # Yellow
blue = "\033[0;34m"  # Blue
white = "\033[0;37m"  # White
black = "\033[0;30m"  # Black
cyan = "\033[0;36m"  # Cyan
purple = "\033[0;35m"  # Purple
gray = "\033[0;90m"  # Gray

# Estilos
bold = "\033[1m"  # Bold
italic = "\033[3m"  # Italic
underline = "\033[4m"  # Underline


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
                        print(
                            f"\n{c("g")}Arquivo de configuração encontrado em: {italic}{bold}{path}{r}"
                        )
                        return path
                    else:
                        print(
                            f"{c(bold=True, faint=True)}Ignorando {path}, id diferente ({data.get('idd')}).{r}"
                        )
            except (json.JSONDecodeError, OSError) as e:
                print(f"{c('r', True)}Erro ao ler {path}: {e}")
        print(
            f"\n{c('y', bold=True)}Aviso:{r} {c('y', True, faint=True)}O arquivo de configurações {r}{c('y')}'config.json'{r}{c('y', True, faint=True)} não foi encontrado no diretório.{r}"
        )
        print(
            f"{c('y', italic=True)} - As opções de criptografia padronizadas não estarão disponíveis.{r}"
        )
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
                    print(f"{c("g", italic=True)} - Configurações carregadas com sucesso.{r}")
                    return config
            except FileNotFoundError:
                print(
                    f" - {italic}Erro: O arquivo de configurações {r}{bold}'config.json' não foi encontrado no diretório.{r}"
                )
            except json.JSONDecodeError:
                print(
                    f" - {italic}Erro: Falha ao decodificar o arquivo {r}{bold}'config.json'.{r} Verifique sua integridade."
                )

    def verify_required_modules():
        dependencies = ["tkinter", "customtkinter", 'os', 'json', 'secrets', 'pathlib', 'datetime']
        for module in dependencies:
            if importlib.util.find_spec(module) is not None:
                print(f"{c('g')}Atualmente o módulo {bold}{module}{r}{c('g')} está instalado.{r}")
            else:
                print(
                    f"{c('r')}Atualmente o módulo {r}{c('r', bold=True)}{module} não está instalado{r}{c('r')}, rode o seguinte comando no terminal para instalar:{r} pip install {bold}{module}{r}"
                )
        has_dependencies = (
            True
            if all(
                importlib.util.find_spec(module) is not None for module in dependencies
            )
            else False
        )
        if not has_dependencies:
            print(
                f"{italic}\nPara instalar utilizando o {r}{bold}pip{r}{italic}, é necessário ter o pip {r}{bold}instalado e configurado no PATH do sistema.{r}"
            )
            print(
                f"\n {italic}- Por opção dos criadores, decidimos não forçar a instalação do pip e dos módulos necessários necessários para utilização a interface gráfica, pois, consideramos essa prática como {bold}intrusiva{r},{italic} e acreditamos que o usuário deve ter controle sobre o que é instalado em seu sistema."
            )

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
                print(
                    f"{r}{c('y', True)}Aviso: O arquivo de configurações 'config.json' não foi encontrado no diretório.{r}"
                )
            except json.JSONDecodeError:
                print(
                    f"{r}{c('r', True)}Erro: Falha ao decodificar o arquivo 'config.json'. Verifique sua integridade.{r}"
                )
        print(f"\n{r}{c(faint=True)}Programa encerrado.{r}\n")
        raise SystemExit

    def find_outputs_folder():
        """
        Procura a pasta 'outputs' a partir do diretório atual até encontrar.
        Retorna o caminho completo da pasta.
        """
        current_dir = os.getcwd()

        while True:
            for root, dirs, files in os.walk(current_dir):
                if 'outputs' in dirs:
                    return os.path.join(root, 'outputs')
            parent = os.path.dirname(current_dir)
            if parent == current_dir:
                print(f"{r}{c('r')}Erro: Pasta 'outputs' não encontrada.{r}")
                return None
            current_dir = parent

    def list_output_files():
        """
        Searches for the 'outputs' folder inside the project and returns
        a list with all file names inside it.
        """
        # Find project root (where 'HashChain---encryption' exists)
        current_dir = os.getcwd()
        while True:
            if "HashChain---encryption" in os.listdir(current_dir):
                project_root = os.path.join(current_dir, "HashChain---encryption")
                break
            parent = os.path.dirname(current_dir)
            if parent == current_dir:
                raise FileNotFoundError(f"{r}{c('r')}A pasta 'HashChain---encryption' não foi encontrada.{r}")
            current_dir = parent

        # Build path to outputs folder
        outputs_path = os.path.join(project_root, "outputs")

        if not os.path.exists(outputs_path):
            print(f"\n{r}{c('r')}A pasta 'outputs' não pode ser encontrada em seu diretório: {outputs_path}{r}")
            print(f"\nUtilize a encriptação e opte por salvar os resultados em um arquivo de log para que sua pasta seja criada.")
            return None

        # List files inside outputs
        files = [f for f in os.listdir(outputs_path)
                if os.path.isfile(os.path.join(outputs_path, f))]

        return files

    def ler_arquivo() -> str | None:
        # Criar janela principal (sem exibir)
        root = tk.Tk()
        root.withdraw()  # Esconde a janela principal
        root.attributes('-topmost', True)
        root.update()

        # Abrir janela de seleção de arquivo
        caminho_arquivo = filedialog.askopenfilename(
            title="Selecione um arquivo para ler",
            filetypes=(("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*"))
        )

        # Verificar se o usuário selecionou um arquivo
        if caminho_arquivo:
            print(f"Arquivo selecionado: {caminho_arquivo}")
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
            return conteudo
        else:
            return None
            # print(f"\n{r}{c('r', faint=True)}Nenhum arquivo selecionado.")

    def salvar_arquivo(text) -> None:
        # Cria a janela oculta do Tkinter
        root = tk.Tk()
        root.withdraw()  # Esconde a janela principal
        root.attributes('-topmost', True)  # Faz o diálogo aparecer na frente

        # Abre a janela de salvar
        caminho = filedialog.asksaveasfilename(
            title="Escolha onde salvar o arquivo",
            initialfile="output.txt", 
            defaultextension=".txt",
            filetypes=(("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*"))
        )

        # Fecha a janela raiz após o uso
        root.destroy()

        # --- Salvar o texto ---
        if caminho:
            try:
                with open(caminho, "w", encoding="utf-8") as arquivo:
                    arquivo.write(text)
                messagebox.showinfo("Sucesso", f"Arquivo salvo em:\n{caminho}")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar o arquivo:\n{e}")
        else:
            print(f"\n{r}{c('y')}Aviso: O arquivo não foi salvo, nenhum local foi selecionado.{r}")
            return None
        
        print(f'\n{r}{c('g')}Texte salvo com sucesso em: {italic}{Path(caminho)}{r}')
        return None

    def print_menu(menu_list: list[str]):
        for i, txt in enumerate(menu_list):
            print(f'{c(bold=True, faint=True)}{i + 1}. {r}{txt}{r}')


def c(color: str = "", bold: bool = False, italic: bool = False, underline: bool = False, faint: bool = False) -> str:
    color_aliases = {
        "r": "31m", # red
        "g": "32m", # green
        "y": "33m", # yellow
        "b": "34m", # blue
        "p": "35m", # purple
        "c": "36m", # cyan
        "w": "37m", # white
        "bl": "30m", # black
        "gr": "90m",  # gray
    }
    if color: color = color.lower()
    if not color and not bold and not italic and not underline and not faint:
        return f'\033[0m'
    elif not color:
        color = "37m"
    elif color in color_aliases:
        color = color_aliases[color]
        
    tipo = ""
    if bold: tipo += "1;"
    if faint: tipo += "2;"
    if italic: tipo += "3;"
    if underline: tipo += "4;"
    if tipo == "": tipo = "0;"
    
    # DEBUG
    # for i in range(90):
    #     print(f'\033[{tipo}{i}m Teste: {i}')
    
    return f"\033[{tipo}{color}"

def cprint(cor_tipo: str, texto: str) -> str:
    pass
