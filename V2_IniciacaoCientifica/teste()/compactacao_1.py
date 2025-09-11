# Sequencia 1 = entrada : ############***********#*#*#*#*#*#*#*#,  saida :  6A5BE7CE
# Sequencia 2 = entrada : 6A5B1E7C1E,  saida : 6152157315 6A5B8D1F

def compactador_seq(compactar,):
    sequencia_tabela1 = {"A": "##", "B": "**", "C": "#*", "D": "*#", "E": "#", "F": "*"}
    sequencia_inversa = {v: k for k, v in sequencia_tabela1.items()}
    char_anterior = ''
    quant_rep = 1
    sequencia = []

    for i in range(0, len(compactar), 2):
        if char_anterior == '':
            char_anterior = compactar[i:i+2]
        elif char_anterior == compactar[i:i+2]:
            char_anterior = compactar[i:i+2]
            quant_rep += 1
        else:
            sequencia.append(str(quant_rep))
            sequencia.append(sequencia_inversa[char_anterior])
            char_anterior = compactar[i:i+2]
            quant_rep = 1
    else:
        sequencia.append(str(quant_rep))
        sequencia.append(sequencia_inversa[char_anterior])
        key = ''.join(sequencia)
        print(key)
        print(" '")
        return key

def numeraliazdor(compactar):
    valor = compactador_seq(compactar)
    valo_cal = {"A": "1", "B": "2", "C": "3", "D": "4", "E": "5", "F": "6"}
    sequencia = []

    for char in valor:
        if char in valo_cal:
            sequencia.append(valo_cal[char])
        else:
            sequencia.append(char)
    else:
        arc = ''.join(sequencia)
        print(arc)
        print(" ")
        return arc
    
""" def compactador(compactar):
    valor = int(numeraliazdor(compactar))
    binario = ""
    if valor !=  0:
        while valor > 0:
            binario = str(valor % 2) + binario
            valor = valor // 2
        return binario
    else:
        raise type("Coloque um valor criptografado.") """
def compactador(compactar):
    numero = int(numeraliazdor(compactar))
    if numero == 0:
        return "0"
    
    hex_chars = []
    hex_chars.extend([chr(i) for i in range(0, 127)])

    hexadecimal = ""
    num = abs(numero)
    base = len(hex_chars)
    
    while num > 0:
        resto = num % base
        hexadecimal = hex_chars[resto] + hexadecimal
        num = num // base
    
    return hexadecimal
    
value = "###***###*#**######*#*****#*####***##***#****#*#*#*#*#*****#***#*#***####*#**#*##***#***#**#**#*#*#*#*#*#**##*#####*#**#****#***#****#***##*#*#*#****#****#*####*****#***####****####********####**"
banana = compactador(value)
print(value)
print(" ")
print(banana)