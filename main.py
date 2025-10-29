# --- Imports ---
import json
import secrets
import datetime
import importlib.util
from HashChainClass import HashChainEncryption
from input_colectors import InputCollector

# Global use.
HashChain: HashChainEncryption = HashChainEncryption()
Collector: InputCollector = InputCollector
config = None
has_dependencies = None
Stable = True
yes_aliases = ["s", "sim", "y", "yes"]
no_aliases = ["n", "nao", "não", "no"]

# --- Functions ---
def load_config():
    global config
    try:
        with open("HashChain/gitHash/HashChain---encryption/config.json", "r") as config_file:
            config = json.load(config_file)
            print("Configurações carregadas com sucesso.")
    except FileNotFoundError:
        print("Erro: O arquivo de configurações 'config.json' não foi encontrado no diretório.")
    except json.JSONDecodeError:
        print("Erro: Falha ao decodificar o arquivo 'config.json'. Verifique sua integridade.")


def close_program():
    if not config is None:
        try:
            with open("HashChain/gitHash/HashChain---encryption/config.json", "w") as config_file:
                json.dump(config, config_file, indent=4)
        except FileNotFoundError:
            print("Erro: O arquivo de configurações 'config.json' não foi encontrado no diretório.")
        except json.JSONDecodeError:
            print("Erro: Falha ao decodificar o arquivo 'config.json'. Verifique sua integridade.")
    print("Programa encerrado.")
    raise SystemExit

def verify_required_modules():
    global has_dependencies

    dependencies = ["tkinter", "customtkinter"]
    for module in dependencies:
        if importlib.util.find_spec(module) is not None:
            print(f"Atualemte o módulo {module} está instalado.")
        else:
            print(f"Atualemte o módulo {module} não está instalado, rode o seguinte comando no terminal para instalar:\npip install {module}")
    has_dependencies = True if all(importlib.util.find_spec(module) is not None for module in dependencies) else False

def reiniciar_programa():
    main()

# Will handle user input, function calls and the interface (WiP).
def main():
    print(f"Bem-vindo ao sistema de criptografia HashChain.\n - Para usar a interface você deve ter as bibliotecas tkinter e customtkinter instaladas.")
    print(" - Para reiniciar ou sair a qualquer momento, digite 'R' ou 'E'.")
    verify_required_modules()
    
    while Stable:
        if config["terminal_mode"]:
            while Stable:
                terminal_mode_input = input("Deseja usar o modo terminal? Caso contrário a interface gráfica sera iniciada. (s/n): ").strip().lower()
                if terminal_mode_input == "r": 
                    reiniciar_programa()
                elif terminal_mode_input == "e":
                    close_program()
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
                if action == "r": 
                    reiniciar_programa()
                elif action == "e":
                    close_program()
                if action not in ["1", "2", "3", "4", "5"]:
                    print("\nAção inválida. Tente novamente.")
                    continue
                action = int(action)
                match action:
                    # Criptografar
                    case 1:
                        texto = input("Digite o texto a ser criptografado: ")
                        while Stable:
                            seed_type = input("\nTipo de seed desejada:\n1. Manual\n2. Automática\n3. Padronizada\nDigite o número da ação desejada: ").strip()
                            if seed_type == "r": 
                                reiniciar_programa()
                            elif seed_type == "e":
                                close_program()
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
                        print(f"Seed escolhida: {seed}")
                        while Stable:
                            passo_type = input("\nTipo de passo desejado:\n1. Manual\n2. Automático\n3. Padronizado\nDigite o número da ação desejada: ").strip()
                            if passo_type == "r":   
                                reiniciar_programa()
                            elif passo_type == "e":
                                close_program()
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
                        print(f"Passos escolhidos: {passo}")
                        while Stable:
                            no_salt_input = input("\nDeseja usar salt na criptografia? (s/n): ").strip().lower()
                            if no_salt_input == "r":   
                                reiniciar_programa()
                            elif no_salt_input == "e":
                                close_program()
                            if no_salt_input not in yes_aliases + no_aliases:
                                print("\nAção inválida. Tente novamente.")
                                continue
                            else:
                                break
                        no_salt = True if no_salt_input in yes_aliases else False   
                        HashChain.encrypt_(texto, passo, seed, no_salt)
                        print("Criptografia realizada com sucesso.")
                        print("\nTexto criptografado:")
                        HashChain.out(0)
                        print("\nChave de descriptografia:")
                        HashChain.out(1)
                        while Stable:
                            salvar_input = input("Criptografia concluída, em alguns casos o texto pode ser grande demais para o terminal exibir, deseja salvar os salvar o texto gerado em um arquivo? (s/n): ").strip().lower()
                            if salvar_input == "r":   
                                reiniciar_programa()
                            elif salvar_input == "e":
                                close_program()
                            if salvar_input not in yes_aliases + no_aliases:
                                print("\nAção inválida. Tente novamente.")
                                continue
                            if salvar_input in yes_aliases:
                                while Stable:
                                    tipo_salvamento = input("Escolha o tipo de salvamento:\n1. Salvar texto criptografado\n2. Salvar chave de descriptografia\n3. Salvar ambos\nDigite o número da ação desejada: ").strip()
                                    if tipo_salvamento not in ["1", "2", "3"]:
                                        print("\nAção inválida. Tente novamente.")
                                        continue
                                    match tipo_salvamento:
                                        case "1":
                                            texto_salvo = HashChain.info(0)
                                        case "2":
                                            texto_salvo = HashChain.info(1)
                                        case "3":
                                            texto_salvo = HashChain.info(0) + '\n' + HashChain.info(1)
                                    break
                                
                                try:
                                    agora = datetime.datetime.now()
                                    milissegundos = int(agora.microsecond / 1000)
                                    file_name = agora.strftime(f"HashChain/gitHash/HashChain---encryption/outputs/log_%Y-%m-%d_%H-%M-%S-{milissegundos:03d}.txt")

                                    with open(file_name, "x", encoding="utf-8") as file:
                                        file.write(texto_salvo)
     
                                except Exception as e:
                                    print("Erro: Ocorreu um erro ao tentar criar o arquivo: ", e)
                                    
                                print(f"Arquivo criado: {file_name}")
                                print("O arquivo foi salvo no seguinte modelo: log_YYYY-MM-DD_HH-MM-SS-MMM.txt, e pode ser encontrado na pasta outputs.")
                                break
                            else:
                                break
                        while Stable:
                            recripto = input("Criptografia finalizada, deseja utilizar o programa novamente? (s/n): ")
                            if recripto == "r":   
                                reiniciar_programa()
                            elif recripto == "e":
                                close_program()
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
                            if log_input == "r":    
                                reiniciar_programa()
                            elif log_input == "e":
                                close_program()
                            if log_input not in yes_aliases + no_aliases:
                                print("\nAção inválida. Tente novamente.")
                                continue 
                            else:
                                break
                        log_input = True if log_input in yes_aliases else False
                        if log_input:
                            while Stable:
                                tipo_log = input("\nTipo de arquivo de log:\n1. Padrão (Primeira linha: texto, Segunda linha: chave)\n2. Só texto\n3. Só chave\nDigite o número da ação desejada: ").strip()
                                if tipo_log not in ["1", "2", "3"]:
                                    print("\nAção inválida. Tente novamente.")
                                    continue
                                else:
                                    break      
                            while Stable:
                                file_path = input("Digite o caminho do arquivo de log: ").strip()
                                try:
                                    with open(file_path, "r", encoding="utf-8") as file:
                                        if tipo_log == "1":
                                            content = file.read().splitlines()
                                            if len(content) < 2:
                                                print("O arquivo de log está incompleto ou inválido. Tente novamente.")
                                                continue
                                            texto = content[0]
                                            key = content[1]
                                            break
                                        elif tipo_log == "2":
                                            texto = file.read()
                                            key = input("Digite a chave para descriptografia: ")
                                            break
                                        elif tipo_log == "3":
                                            key = file.read()
                                            texto = input("Digite o texto a ser descriptografado: ")
                                            break
                                except FileNotFoundError:
                                    print("Arquivo não encontrado. Tente novamente.")
                                    continue
                            HashChain.decrypt_(texto, key)
                            print("Descriptografia realizada com sucesso.")
                            print(HashChain.decrypt_(texto, key))
                        else:     
                            texto = input("Digite o texto a ser descriptografado: ")
                            key = input("Digite a chave para descriptografia: ")
                            HashChain.decrypt_(texto, key)
                            print("Descriptografia realizada com sucesso.")
                            HashChain.out(3)
                        
                    # Compressão
                    case 3:
                        texto = input("Digite o texto a ser comprimido: ")
                        print("\nTexto comprimido:")
                        print(HashChain.compression_(texto))
                        
                    # Descompressão
                    case 4:
                        texto = input("Digite o texto a ser descomprimido: ")
                        print("\nTexto descomprimido:")
                        print(HashChain.decompression_(texto))
                        
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
                close_program()

            from interface import root, interface_menu
            interface_menu()
            root.mainloop()
    
# Handles key actions.
if __name__ == "__main__":
    load_config()
    main()
    close_program()