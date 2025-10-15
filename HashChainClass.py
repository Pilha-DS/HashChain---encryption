# ===== HashChainClass =====
#      --- Imports ---
import random
import os
from tables import gerar_tabelas


class HashChainEncryption:
    # Initializes all the atributes.
    def __init__(self):
        # Will recieve data in: [compressed_text, key, cipher_text, plain_text]
        self._info: list[str] | None = None

    # Prints the desired stored encrypted data
    def out(self, output: str | int = 0) -> None:
        # If no encryption has occurred, return None
        if self._info is None:
            print(None)

        # If the argument is a string interpret it as so
        elif isinstance(output, str):
            # Standardizes the argument
            output = output.lower()

            # Aliases for the keywords
            plain_text = ["p", "plain", "plain text", "plain_text", "text"]
            cipher_text = ["c", "cipher", "cipher text", "cipher_text"]
            compressed_text = [
                "cc",
                "compressed",
                "compressed text",
                "compressed_text",
                "compressed cipher text",
                "compressed_cipher_text",
                "compressed cipher",
                "compressed_cipher",
            ]
            key = ["key", "pass", "k"]

            # Prints the desired data
            if output in compressed_text:
                print(self._info[0])
            elif output in key:
                print(self._info[1])
            elif output in cipher_text:
                print(self._info[2])
            elif output in plain_text:
                print(self._info[3])

        # Else if the argument is an int
        elif isinstance(output, int):
            # If the int is in range print the desired data, if it is out of range print all the info
            if output >= 0 and output <= 3:
                print(self._info[output])
            else:
                print(
                    f"----- Compressed text\n{self._info[0]}\n----- Key\n{self._info[1]}\n----- Cipher text\n{self._info[2]}\n----- Plain text\n{self._info[3]}"
                )

    # The stadard get info method, retuns the stored data values from the last encryption
    def info(self, search: str = None) -> str:
        # If no parameter is given returns None
        if search is None:
            return None
        # If the parameter is a str returns the value using its matching keyword else returns the data by its position in the list
        if isinstance(search, str):
            search = search.lower()
            plain_text = ["p", "plain", "plain text", "plain_text", "text"]
            cipher_text = ["c", "cipher", "cipher text", "cipher_text"]
            compressed_text = [
                "cc",
                "compressed",
                "compressed text",
                "compressed_text",
                "compressed cipher text",
                "compressed_cipher_text",
                "compressed cipher",
                "compressed_cipher",
            ]
            key = ["key", "pass", "k"]
            return (
                self._info[0]
                if search in compressed_text
                else (
                    self._info[1]
                    if search in key
                    else (
                        self._info[2]
                        if search in cipher_text
                        else self._info[3] if search in plain_text else None
                    )
                )
            )
        elif isinstance(search, int):
            return self._info[search]

    # Receives a ciphered text and retuns a compressed ciphered text.
    def compression_(self, cipher_text: str) -> str:
        aux = cipher_text
        posicao = 0
        countZero = 0
        countUm = 0
        texto = ""
        caltStr = "10"

        while posicao < len(aux):
            i = aux[posicao]

            if i == "0":
                countUm = 0
                countZero += 1

                if countZero >= 2 and posicao + 1 < len(aux) and aux[posicao + 1] != i:
                    caltStr = str(countZero)
                    if len(caltStr) == 2:
                        if caltStr[0] == "1":
                            if caltStr[1] == "0":
                                texto += "X" + "Z"
                            else:
                                texto += "X" + caltStr[1]
                        elif caltStr[1] == "1":
                            texto += caltStr[0] + "X"
                        elif caltStr[1] == "0":
                            texto += caltStr[0] + "Z"
                    else:
                        texto += str(countZero)
                if posicao + 1 < len(aux) and aux[posicao + 1] != i:
                    texto += i

            else:
                countZero = 0
                countUm += 1

                if countUm >= 2 and posicao + 1 < len(aux) and aux[posicao + 1] != i:
                    caltStr = str(countUm)
                    if len(caltStr) == 2:
                        if caltStr[0] == "1":
                            if caltStr[1] == "0":
                                texto += "X" + "Z"
                            else:
                                texto += "X" + caltStr[1]
                        elif caltStr[1] == "1":
                            texto += caltStr[0] + "X"
                        elif caltStr[1] == "0":
                            texto += caltStr[0] + "Z"
                    else:
                        texto += str(countUm)
                if posicao + 1 < len(aux) and aux[posicao + 1] != i:
                    texto += i

            posicao += 1

        if countZero >= 2:
            texto += str(countZero) + "0"
        elif countUm >= 2:
            texto += str(countUm) + "1"

        return texto

    # Receives a compressed ciphered text and retuns the ciphered text.
    def decompression_(self, compressed_cipher_text: str) -> str:
        norm: str = compressed_cipher_text
        trad = {
            "Z": "0",
            "X": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
        }

        total: list[str] = []
        aux: list[str] = []

        for c in norm:
            if c in ["0", "1"] and not aux:
                total.append(c)
            elif c in ["Z", "X", "2", "3", "4", "5", "6", "7", "8", "9"]:
                aux.append(trad[c])
            else:
                total.append(c * int("".join(aux)))
                aux = []

        return "".join(total)

    # Receives a plain text and returns the compressed cipher text.
    def encrypt_(
        self,
        plaintext: str = "",
        pass_: list = None,
        seed: int = 0,
        no_salt: bool = False,
        debug_mode: bool = False,
        min_table_leng: int = 20,
        max_table_leng: int = 999,
    ):
        def gerar_seed_decimal_aleatoria(num_digitos: int = 64) -> int:
            """Gera seed de 64 caracteres por padrão"""
            # Gera bytes aleatórios seguros
            bytes_aleatorios = os.urandom(num_digitos // 2)  # cada byte ≈ 2 dígitos
            # Converte os bytes para inteiro
            large_number = int.from_bytes(bytes_aleatorios, "big")
            # Formata para garantir exatamente num_digitos
            seed_str = str(large_number).zfill(num_digitos)
            seed_str = seed_str[:num_digitos]
            return int(seed_str)

        """
        Criptografa texto utilizando tabelas de substituição geradas deterministicamente.

        Args:
            plaintext (str): Texto a ser criptografado (obrigatorio)
            pass_ (list): Lista de passes para geração de chave (opcional)
            seed (int): Seed para geração determinística (opcional)
            no_salt (bool): Gera o cipher text sem salt (opcional)
            debug_mode (bool): Retornas os valores em modo desenvolvedor a função
            min_table_leng (int): O tamanho minimo da tabela de substituição (opcional). Não pode sere inferior a (20)
            max_table_leng (int): O tamanho maximo da tabela de substituição (opcional). Não pode ultrapassar (999)

        Returns:
            list: Lista contendo [texto cifrado, chave]

        Raises:
            ValueError: Se o texto plano não for fornecido
        """
        # Inicialização de parâmetros opcionais
        if pass_ is None:
            pass_ = []

        cor = {
            "pad": "\033[0;0m",
            "red": "\033[1;31m",
            "gre": "\033[1;32m",
            "blu": "\033[1;34m",
            "yel": "\033[1;33m",
            "mag": "\033[1;35m",
            "cya": "\033[1;36m",
        }

        # Validação dos parâmetros obrigatórios
        if min_table_leng < 20:
            min_table_leng = 20
        if not plaintext:
            raise ValueError(
                "Parâmetro obrigatório: plaintext deve ser uma string não vazia"
            )

        # Geração de valores padrão se não informados
        if not seed:
            seed = gerar_seed_decimal_aleatoria(64)

        # Gera uma seed diferente para cada passe se não houver passes fornecidos
        if not pass_:
            p = len(plaintext)
            while p > 0:
                p -= 1
                pass_.append(random.randint(min_table_leng, max_table_leng))

        # GERAÇÃO DE SEEDS DIFERENTES PARA CADA PASSE
        seeds_por_passe = []
        dict_tables_por_passe = {}

        # Usa a seed principal para gerar seeds únicas para cada passe
        random.seed(seed)
        for i, passe in enumerate(pass_):
            # Gera uma seed única para este passe baseada na seed principal + índice do passe
            seed_passe = seed + (i * 1000000) + passe
            seeds_por_passe.append(seed_passe)

            # Gera tabelas específicas para este passe
            dict_tables_passe = gerar_tabelas(seed_passe, [passe])[0]
            dict_tables_por_passe[passe] = dict_tables_passe[passe]

        # Restaura o estado aleatório
        random.seed()

        # Variáveis principais
        crude_ciphertext_list = []
        invalid_characters_list = []
        control_index = 0
        control_key = len(pass_) - 1

        # Funções internas auxiliares
        def enciphering(caracter: str) -> None:
            """Mapeia um caractere para a substituição correspondente"""
            nonlocal control_index
            try:
                # Obtém o passe atual e suas tabelas correspondentes
                passe_atual = pass_[control_index]
                tabela_atual = dict_tables_por_passe[passe_atual]

                cipher_char = tabela_atual[caracter]
                if debug_mode:
                    crude_ciphertext_list.append(cor["gre"] + cipher_char + cor["pad"])
                else:
                    crude_ciphertext_list.append(cipher_char)
            except KeyError:
                invalid_characters_list.append(caracter)

        def create_salt(
            ciphertext_list: list, current_pass: list, current_seed: int
        ) -> tuple:
            """Insere salt no ciphertext para aumentar entropia usando seeds determinísticas"""
            salt_ciphertext_list = ciphertext_list.copy()
            salt_passes = current_pass.copy()
            posicoes = []
            salt_leng = random.randint(20, 20 + len(ciphertext_list))

            # Usa a seed principal para gerar seeds únicas para cada salt
            random.seed(current_seed)

            for salt_index in range(salt_leng):
                salt_pass = random.randint(min_table_leng, max_table_leng)
                posicao = random.randint(0, len(salt_ciphertext_list) - 1)

                # Gera seed única para este salt baseada na seed principal + índice do salt
                seed_salt = current_seed + (salt_index * 100000) + salt_pass + posicao

                # Gera tabelas específicas para este salt
                tb = gerar_tabelas(seed_salt, [salt_pass])
                random_char = chr(random.randint(65, 90))

                if debug_mode:
                    salt_passes.insert(
                        posicao, cor["red"] + str(salt_pass).zfill(3) + cor["pad"]
                    )
                    salt_ciphertext_list.insert(
                        posicao,
                        cor["red"] + tb[0][salt_pass][random_char] + cor["pad"],
                    )
                    posicoes.append(
                        cor["cya"] + str(len(str(posicao))).zfill(3) + cor["pad"]
                    )
                    posicoes.append(cor["yel"] + str(posicao) + cor["pad"])
                else:
                    salt_passes.insert(posicao, salt_pass)
                    salt_ciphertext_list.insert(posicao, tb[0][salt_pass][random_char])
                    posicoes.append(str(len(str(posicao))).zfill(3))
                    posicoes.append(str(posicao))

            # Restaura o estado aleatório
            random.seed()

            return salt_ciphertext_list, salt_passes, posicoes

        def key_generator(
            passes_list: list,
            current_seed: int,
            seeds_passes: list = None,
            salt_positions: list = None,
            padding: str = "",
        ) -> tuple:
            """Gera chave polida para descriptografia posterior"""
            if salt_positions is None:
                salt_positions = []
            if seeds_passes is None:
                seeds_passes = []

            # Prepara os passes
            poli_passes = [str(p).zfill(3) for p in passes_list]
            poli_seeds = (
                [str(s).zfill(20) for s in seeds_passes] if seeds_passes else []
            )
            poli_salt = [str(s) for s in salt_positions] if salt_positions else []

            # Prepara valores para a chave
            seed_value = str(current_seed)
            pl = str(len(poli_passes))
            lolp = str(len(pl)).zfill(3)
            sl = str(len(seed_value)).zfill(3)

            # Informações sobre seeds dos passes
            seeds_l = str(len(seeds_passes)) if seeds_passes else "000"
            lol_seeds = str(len(seeds_l)).zfill(3) if seeds_passes else "000"

            salt_l = [str(int(len(salt_positions) / 2))] if poli_salt else []
            lol_salt = [str(len(salt_l[0])).zfill(3)] if salt_l else []

            # Aplica cores se estiver em debug mode
            if debug_mode:
                seed_value = cor["blu"] + seed_value + cor["pad"]
                pl = cor["mag"] + pl + cor["pad"]
                lolp = cor["mag"] + lolp + cor["pad"]
                sl = cor["mag"] + sl + cor["pad"]
                salt_l = [cor["mag"] + s + cor["pad"] for s in salt_l]
                lol_salt = [cor["mag"] + s + cor["pad"] for s in lol_salt]
                poli_passes = [cor["gre"] + p + cor["pad"] for p in poli_passes]
                poli_seeds = [cor["yel"] + p + cor["pad"] for p in poli_seeds]
                poli_salt = [cor["red"] + p + cor["pad"] for p in poli_salt]

            # Gera chave detalhada (apenas para debug)
            crude_key = (
                f"\nseed principal: {seed_value}\n\n"
                f"salt: lol_salt: {', '.join(lol_salt)}, salt_l: {', '.join(salt_l)}, \n"
                f"posições salt: {', '.join(poli_salt)}\n\n"
                f"passes: lolp: {lolp}, pl: {pl}, \n"
                f"passes: {', '.join(poli_passes)}\n\n"
                f"padding: {padding}"
            )

            # Gera chave polida (para uso real)
            polished_key = "".join(
                [
                    "1" if no_salt else "2",
                    "".join(lol_salt),
                    "".join(salt_l),
                    "".join(poli_salt),
                    "".join(lolp),
                    "".join(pl),
                    "".join(poli_passes),
                    "".join(sl),
                    "".join(seed_value),
                    padding,
                ]
            )

            return poli_passes, polished_key, crude_key

        # Processo de criptografia principal
        for caracter in plaintext:
            enciphering(caracter)
            control_index = 0 if control_index == control_key else control_index + 1

        # Aplicação do salt e geração da chave
        if not no_salt:
            salt_result = create_salt(crude_ciphertext_list, pass_, seed)
            ciphertext = "".join(salt_result[0])

            if (len(ciphertext) % 20) == 0:
                key_result = key_generator(
                    passes_list=salt_result[1],
                    current_seed=seed,
                    seeds_passes=seeds_por_passe,
                    salt_positions=salt_result[2],
                )
            else:
                padding = ((len(ciphertext) % 20) - 20) * -1
                ciphertext += padding * "1"
                key_result = key_generator(
                    passes_list=salt_result[1],
                    current_seed=seed,
                    seeds_passes=seeds_por_passe,
                    salt_positions=salt_result[2],
                    padding=str(padding),
                )
        else:
            ciphertext = "".join(crude_ciphertext_list)
            if (len(ciphertext) % 20) == 0:
                key_result = key_generator(
                    passes_list=pass_,
                    current_seed=seed,
                    seeds_passes=seeds_por_passe,
                )
            else:
                padding = ((len(ciphertext) % 20) - 20) * -1
                ciphertext += padding * "1"
                key_result = key_generator(
                    passes_list=pass_,
                    current_seed=seed,
                    seeds_passes=seeds_por_passe,
                    padding=str(padding),
                )

        # Saída final
        if debug_mode:
            return (
                f"\nPlaintext: {cor['blu'] + plaintext + cor['pad']}\n\n"
                f"Ciphertext_list: {', '.join(p for p in crude_ciphertext_list) if no_salt else ', '.join(p for p in salt_result[0])}\n\n"
                f"Seeds por passe: {seeds_por_passe}\n\n"
                f"Crude key: {key_result[2]}\n\n"
                f"Polished key: {key_result[1]}\n\n"
                f"Invalid characters: {invalid_characters_list}\n\n"
                f"Ciphertext: {ciphertext}\n\n"
            )
        else:
            self._info = [
                self.compression_(ciphertext),
                key_result[1],
                ciphertext,
                plaintext,
            ]
            return [self.compression_(ciphertext), key_result[1]]

    # Receives a compressed cipher text and returns the decrypted text (plain text / original message).
    def decrypt_(self, ciphertext, key):
        ciphertext = self.decompression_(ciphertext)
        def dechaveador(ciphertext: str = "", key: str = ""):
            if not ciphertext:
                raise ValueError("Coloque um ciphertext valído")
            if not key:
                raise ValueError("Coloque uma chave valída")
            passes = []
            ciphertext_list = []
            if key[1] == '2':
                key = key[1:]
                lol_salt = int(key[0:3])
                index = 3 + lol_salt

                salt_l = int(key[3:index])
                posicoes = []

                for n in range(0, salt_l):
                    pn = int(key[index : index + 3])
                    index += 3
                    posicoes.append(int(key[index : index + pn]))
                    index += pn

                lol_p = int(key[index : index + 3])
                pl = int(key[index + 3 : index + 3 + lol_p])

                index += lol_p + 3
                for n in range(0, pl):
                    passes.append(int(key[index : index + 3]))
                    index += 3

                sl = int(key[index : index + 3])
                seed = int(key[index + 3 : sl + index + 3])

                index += sl + 3

                s_index = 0

                for n in range(0, len(passes)):
                    ciphertext_list.append(ciphertext[s_index : passes[n] + s_index])
                    s_index += passes[n]

                pad = -1
                for p in range(0, len(posicoes)):
                    del ciphertext_list[posicoes[pad]]
                    del passes[posicoes[pad]]
                    pad += -1

            elif key[2] == "1":
                key = key[1:]
                lol_p = int(key[0:3])
                index = 3 + lol_p
                pl = int(key[index + 3 : index + 3 + lol_p])

                index += lol_p + 3
                for n in range(0, pl):
                    passes.append(int(key[index : index + 3]))
                    index += 3

                sl = int(key[index : index + 3])
                seed = int(key[index + 3 : sl + index + 3])

                index += sl + 3

                s_index = 0
                for n in range(0, len(passes)):
                    ciphertext_list.append(ciphertext[s_index : passes[n] + s_index])
                    s_index += passes[n]

            return [passes, seed, ciphertext_list]
        desc = dechaveador(ciphertext, key)

        pass_ = desc[0]
        seed = desc[1]
        cipher = desc[2]

        plaintext = []

        # GERAÇÃO DE SEEDS DIFERENTES PARA CADA PASSE
        seeds_por_passe = []
        dict_tables_por_passe = {}

        # Usa a seed principal para gerar seeds únicas para cada passe
        for i, passe in enumerate(pass_):
            # Gera uma seed única para este passe baseada na seed principal + índice do passe
            seed_passe = seed + (i * 1000000) + passe
            seeds_por_passe.append(seed_passe)

            # Gera tabelas específicas para este passe
            dict_tables_passe = gerar_tabelas(seed_passe, [passe])[1]
            dict_tables_por_passe[passe] = dict_tables_passe[passe]

        for n, p in enumerate(pass_):
            try:
                plaintext.append(dict_tables_por_passe[p][cipher[n]])
            except:
                print("invalida")

        return "".join(plaintext)
