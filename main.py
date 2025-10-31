# --- Imports ---
import secrets
import datetime
from pathlib import Path
from utils import Handler, InputCollector
from HashChainClass import HashChainEncryption

# Global use.
HashChain: HashChainEncryption = HashChainEncryption()
Collector: InputCollector = InputCollector
config_path = Handler.find_config_file()
config = Handler.load_config(config_path)
has_dependencies = None
Stable = True
reinicios = 0
yes_aliases = ["s", "sim", "y", "yes"]
no_aliases = ["n", "nao", "não", "no"]

# Terminal colors

# r = f'\e[0m' # Reset
# red = f'\e[0;31m' # Red
# green = f'\e[0;32m' # Green
# yellow = f'\e[0;33m' # Yellow
# blue = f'\e[0;34m' # Blue
# withe = f'\e[0;37m' # White
# black = f'\e[0;30m' # Black
# cyan = f'\e[0;36m' # Cyan
# purple = f'\e[0;35m' # Purple
# gray = f'\e[0;90m' # Gray
# bold = f'\e[1m' # Bold
# italic = f'\e[3m' # Italic
# underline = f'\e[4m' # Underline

# --- Functions ---

def close_program():
    global config, config_path
    Handler.save_config(config, config_path)

def restart_program():
    global reinicios
    if reinicios > 100:
        print("Numero de reinícios consecutivos excedido.")
        close_program()
    else:
        reinicios += 1
        main()

def check_action(user_input):
    if user_input == "r": restart_program()
    elif user_input == "e": close_program()

# Will handle user input, function calls and the interface (WiP).
def main():
    global has_dependencies
    
    print(f"\nBem-vindo ao sistema de criptografia HashChain.\n - Para usar a interface você deve ter as bibliotecas tkinter e customtkinter instaladas.")
    print(" - Para reiniciar ou sair a qualquer momento, digite 'R' ou 'E'.\n")
    has_dependencies = Handler.verify_required_modules()
    
    if config is None:
        print("\nO arquivo de configuração não foi carregado corretamente, as opções de criptografia padronizadas não estarão disponíveis.")
    
    while Stable:
        if config["terminal_mode"]:
            while Stable:
                terminal_mode_input = input("\nDeseja usar o modo terminal? Caso contrário a interface gráfica sera iniciada. (s/n): ").strip().lower()
                check_action(terminal_mode_input)
                if terminal_mode_input in yes_aliases + no_aliases:
                    break
                else:
                    print("Ação inválida. Tente novamente.")
                    continue
            config["terminal_mode"] = True if terminal_mode_input in yes_aliases else False
            if not config["terminal_mode"]:
                continue
              
            while Stable:
                action = input("\nEscolha uma ação:\n1. Criptografar Texto\n2. Descriptografar Texto\n3. Comprimir Texto\n4. Descomprimir Texto\n5. Sair\n\nDigite o número da ação desejada: ").strip()
                check_action(action)
                if action not in ["1", "2", "3", "4", "5"]:
                    print("\nAção inválida. Tente novamente.")
                    continue
                action = int(action)
                match action:
                    # Criptografar
                    case 1:
                        texto = input("\nDigite o texto a ser criptografado: ")
                        while Stable:
                            if config_path is None:
                                seed_type = input("\nTipo de seed desejada:\n1. Manual\n2. Automática\nDigite o número da ação desejada: ").strip()
                            else:
                                seed_type = input("\nTipo de seed desejada:\n1. Manual\n2. Automática\n3. Padronizada\nDigite o número da ação desejada: ").strip()
                            
                            check_action(seed_type)
                            
                            if config_path is None:
                                if seed_type not in ["1", "2"]:
                                    print("\nAção inválida. Tente novamente.")
                                    continue
                                else:
                                    break
                            elif config_path is not None:
                                if seed_type not in ["1", "2", "3"]:
                                    print("\nAção inválida. Tente novamente.")
                                    continue
                                else:
                                    break
                                
                        match seed_type:
                            case "1":
                                seed = Collector.get_seed_()
                            case "2":
                                num_digits = secrets.randbelow(65) + 64
                                seed = int("".join(str(secrets.randbelow(10)) for _ in range(num_digits)))
                            case "3":
                                seed = int(config["params"]["seed"])
                                
                        print(f"\nSeed escolhida: {seed}")
                        
                        while Stable:
                            if config_path is not None:
                                passo_type = input("\nTipo de passo desejado:\n1. Manual\n2. Automático\n3. Padronizado\nDigite o número da ação desejada: ").strip()
                            elif config_path is None:
                                passo_type = input("\nTipo de passo desejado:\n1. Manual\n2. Automático\nDigite o número da ação desejada: ").strip()
                            
                            check_action(passo_type)
                                
                            if config_path is None:
                                if passo_type not in ["1", "2"]:
                                    print("\nAção inválida. Tente novamente.")
                                    continue
                                else:
                                    break
                            elif config_path is not None:
                                if passo_type not in ["1", "2", "3"]:
                                    print("\nAção inválida. Tente novamente.")
                                    continue
                                else:
                                    break
                                
                        match passo_type:
                            case "1":
                                passo = Collector.get_passes_()
                            case "2":
                                num_passes = secrets.randbelow(64) + 8
                                passo = [secrets.randbelow(979) + 20 for _ in range(num_passes)]
                            case "3":
                                passo = config["params"]["passes"]
                                
                        print(f"\nPassos escolhidos: {passo}")
                        
                        while Stable:
                            print("\n - Salt é uma medida de segurança adicional que pode ser usada durante a criptografia para aumentar a aleatoriedade do processo, que adiciona sequências de caracteres e tamanhos aleatórios ao texto, ele transformara a chave para descriptografia em algo único para cada execução mesmo com os mesmos parâmetros.")
                            no_salt_input = input("\nDeseja usar salt na criptografia? (s/n): ").strip().lower()
                            
                            check_action(no_salt_input)
                            
                            if no_salt_input not in yes_aliases + no_aliases:
                                print("\nAção inválida. Tente novamente.")
                                continue
                            else:
                                break
                        no_salt = True if no_salt_input in yes_aliases else False   
                        HashChain.encrypt(texto, passo, seed, no_salt)
                        print("\nCriptografia realizada com sucesso.")
                        print("\nTexto criptografado:\n")
                        print(HashChain.info(0))
                        print("\n\nChave de descriptografia:\n")
                        print(HashChain.info(1))
                        while Stable:
                            salvar_input = input("\nCriptografia concluída, em alguns casos o texto pode ser grande demais para o terminal exibir, deseja salvar os salvar o texto gerado em um arquivo? (s/n): ").strip().lower()
                            
                            check_action(salvar_input)
                            
                            if salvar_input not in yes_aliases + no_aliases:
                                print("\nAção inválida. Tente novamente.")
                                continue
                            
                            if salvar_input in yes_aliases:
                                while Stable:
                                    tipo_salvamento = input("\nEscolha o tipo de salvamento:\n1. Texto criptografado e chave\n2. Salvar apenas o texto criptografado\n3. Salvar apenas a chave\nDigite o número da ação desejada: ").strip()
                                    
                                    check_action(tipo_salvamento)
                                    
                                    if tipo_salvamento not in ["1", "2", "3"]:
                                        print("\nAção inválida. Tente novamente.")
                                        continue
                                    match tipo_salvamento:
                                        case "2":
                                            texto_salvo = HashChain.info(0)
                                        case "3":
                                            texto_salvo = HashChain.info(1)
                                        case "1":
                                            texto_salvo = HashChain.info(0) + '\n' + HashChain.info(1)
                                    break
                                
                                try:
                                    project_root = next(
                                        (p for p in Path(__file__).resolve().parents if p.name == "HashChain---encryption"),
                                        None
                                    )

                                    if not project_root:
                                        raise FileNotFoundError("Diretório 'HashChain---encryption' não encontrado.")
                                    
                                    outputs_dir = project_root / "outputs"
                                    outputs_dir.mkdir(exist_ok=True)

                                    agora = datetime.datetime.now()
                                    milissegundos = int(agora.microsecond / 1000)
                                    file_name = agora.strftime(f"log_%Y-%m-%d_%H-%M-%S-{milissegundos:03d}.txt")
                                    log_path = outputs_dir / file_name

                                    # Cria e escreve o arquivo
                                    with open(log_path, "x", encoding="utf-8") as file:
                                        file.write(texto_salvo)

                                    print(f"\nLog salvo em: {log_path}")
                                    
                                except Exception as e:
                                    print("Erro: Ocorreu um erro ao tentar criar o arquivo: ", e)
                                    
                                print("\nO arquivo foi salvo no seguinte modelo: log_YYYY-MM-DD_HH-MM-SS-MMM.txt, e pode ser encontrado na pasta outputs.")
                                break
                            else:
                                break
                        while Stable:
                            recripto = input("\nCriptografia finalizada, deseja utilizar o programa novamente? (s/n): ")
                            check_action(recripto)
                            if recripto not in yes_aliases + no_aliases:
                                print("\nAção inválida. Tente novamente.")
                                continue
                            if recripto in yes_aliases:
                                break
                            else:
                                close_program()
                                break
                                        
                    # Descriptografar
                    case 2:
                        while Stable:
                            log_input = input("Deseja usar um arquivo de log para descriptografia? (s/n): ").strip().lower()
                            
                            check_action(log_input)
                            
                            if log_input not in yes_aliases + no_aliases:
                                print("\nAção inválida. Tente novamente.")
                                continue 
                            else:
                                break
                        log_input = True if log_input in yes_aliases else False
                        if log_input:
                            while Stable:
                                tipo_log = input("\nTipo de arquivo de log:\n1. Padrão (Primeira linha: texto, Segunda linha: chave)\n2. Só texto\n3. Só chave\nDigite o número da ação desejada: ").strip()
                                
                                check_action(tipo_log)
                                
                                if tipo_log not in ["1", "2", "3"]:
                                    print("\nAção inválida. Tente novamente.")
                                    continue
                                else:
                                    break      
                            while Stable:
                                file_path = input("Digite o caminho do arquivo de log: ").strip()
                                
                                check_action(file_path)
                                
                                try:
                                    with open(file_path, "r", encoding="utf-8") as file:
                                        if tipo_log == "1":
                                            # stardard quebrado
                                            """ content = file.read().splitlines()
                                            if len(content) < 2:
                                                print("O arquivo de log está incompleto ou inválido. Tente novamente.")
                                                continue
                                            texto = content[0]
                                            key = content[1] """
                                            # teste
                                            content = file.read()
                                            texto = []
                                            key = []
                                            line_break_passed = False
                                            for char in content:
                                                if char == '\n':
                                                    line_break_passed = True
                                                elif not line_break_passed:
                                                    texto.append(char)
                                                elif line_break_passed:
                                                    key.append(char)
                                            texto = ''.join(texto)
                                            key = ''.join(key)
                                            if '\n' in key or '\n' in texto:
                                                print("a" * 399)
                                        elif tipo_log == "2":
                                            texto = file.read()
                                            key = input("Digite a chave para descriptografia: ")
                                        elif tipo_log == "3":
                                            key = file.read()
                                            texto = input("Digite o texto a ser descriptografado: ")
                                except FileNotFoundError:
                                    print("Arquivo não encontrado. Tente novamente.")
                                    continue
                                HashChain.decrypt(texto, key)
                                print("Descriptografia realizada com sucesso.")
                                HashChain.out(3)
                                break
                        else:     
                            texto = input("Digite o texto a ser descriptografado: ")
                            key = input("Digite a chave para descriptografia: ")
                            HashChain.decrypt(texto, key)
                            print("Descriptografia realizada com sucesso.")
                            HashChain.out(3)
                        
                    # Compressão
                    case 3:
                        texto = input("Digite o texto a ser comprimido: ")
                        print("\nTexto comprimido:")
                        print(HashChain.compression(texto))
                        
                    # Descompressão
                    case 4:
                        texto = input("Digite o texto a ser descomprimido: ")
                        print("\nTexto descomprimido:")
                        print(HashChain.decompression(texto))
                        
                    # Sair
                    case 5:
                        close_program()
                        
                    case _:
                        print("FATAL ERROR")
                        close_program()
            
        elif not config["terminal_mode"]:
            if not has_dependencies:
                print("Não é possível iniciar a interface gráfica, pois as dependências necessárias não estão instaladas, instale-as e tente novamente.")
                config["terminal_mode"] = True
                break

            from interface import root, interface_menu
            interface_menu()
            root.mainloop()
    
# Handles key actions.
if __name__ == "__main__":
    main()
    close_program()
