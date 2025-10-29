class InputCollector:
    def __init__(self):
        pass
        
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
                    raise Exception("Invalid user actions, must be [C] or [D] to proceed.")
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
            if len(str(passos)) <= 0: return False
            for _, passo in enumerate(passos):
                if not isinstance(passo, int) or passo < 20 or passo > 999: return False
            
            return True
        
        def conver_input_(raw_passos: str) -> list[int] | int:
            valid_chars: list[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]
            raw_passos += " "
            passos: list[int] = []
            aux: list[str] = []
            try:
                for char in raw_passos:
                    if char not in valid_chars: raise Exception("Caractere inválido.")
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
            raw_passos: str = input("Digite os passos separados por espaços, cada um sendo um inteiro de 20 a 999. (Exemplo: 20 450 999): ")
            passos: list[int] = conver_input_(raw_passos)
            if is_valid_pass_(passos):
                break
            print("Input inválido. Passes devem ser inteiros de 20 a 999. Tente novamente.")
            
        return passos