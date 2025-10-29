import customtkinter as ctk
from tkinter import messagebox, scrolledtext, filedialog
import random
import tables
from HashChainClass import HashChainEncryption

t: HashChainEncryption = HashChainEncryption()

def grafar(a, b, c):
    t.encrypt_(a, b, c)
    
def desgrafar(a, b, c):
    if a and b and c:
        t.decrypt_(a, b, c)

# Configuração inicial
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Cores
COLOR_BG = "#001f3f"        
COLOR_FRAME = "#003366" 
COLOR_TEXT = "#f2f2f2"      
COLOR_BTN = "#004080"      
COLOR_BTN_HOVER = "#0050a0"
COLOR_ENTRY = "#003366"    


# Variáveis globais
root = ctk.CTk()
seed_var = ctk.StringVar()
passo_var = ctk.StringVar()
modo_var = ctk.StringVar(value="manual")
cripto_resultado = ""
chave = ""

# Layout fixo

# content_frame = ctk.CTkFrame(root)
# content_frame.pack(side="right", fill="both", expand=True)

# menu_frame = ctk.CTkFrame(root, width=180, corner_radius=0)
# menu_frame.pack(side="left", pady=(20, 0), padx=10, fill="y")

content_frame = ctk.CTkFrame(root, fg_color=COLOR_BG)
content_frame.pack(side="right", fill="both", expand=True)

menu_frame = ctk.CTkFrame(root, width=200, fg_color=COLOR_FRAME, corner_radius=5)
menu_frame.pack(side="left", fill="y", padx=5, pady=5)


header_label = ctk.CTkLabel(content_frame, text="Sistema de Criptografia", font=("Arial", 22, "bold"))
header_label.pack(pady=(20, 10))

def limpar_content():
    for widget in content_frame.winfo_children():
        widget.destroy()

# INTERFACES
def interface_menu():
    limpar_content()
    ctk.CTkLabel(content_frame, text="Sistema de Criptografia", font=("Arial", 20, "bold")).pack(pady=20)

def interface_criptografar():
    limpar_content()

    ctk.CTkLabel(content_frame, text="Criptografar Texto", font=("Arial", 16, "bold")).pack(pady=10)

    texto_label = ctk.CTkLabel(content_frame, text="Texto para criptografar:")
    texto_label.pack(anchor="w", padx=20)
    texto_entry = ctk.CTkTextbox(content_frame, height=100)
    texto_entry.pack(padx=20, pady=5, fill="x")

    seed_label = ctk.CTkLabel(content_frame, text="Seed (opcional):")
    seed_label.pack(anchor="w", padx=20, pady=(10, 0))
    seed_entry = ctk.CTkEntry(content_frame, textvariable=seed_var)
    seed_entry.pack(padx=20, fill="x")

    def gerar_seed():
        seed_var.set(random.randint(10000000, 99999999999999999999999999999999))
    ctk.CTkButton(content_frame, text="Gerar Seed Aleatória", command=gerar_seed).pack(pady=5, padx=20)

    passo_label = ctk.CTkLabel(content_frame, text="Passo (opcional, separado por espaços):")
    passo_label.pack(anchor="w", padx=20, pady=(10, 0))
    passo_entry = ctk.CTkEntry(content_frame, textvariable=passo_var)
    passo_entry.pack(padx=20, fill="x")

    ctk.CTkButton(content_frame, text="Criptografar",
                  command=lambda: executar_criptografia(
                      texto_entry.get("1.0", "end-1c"), seed_var.get(), passo_var.get())
                  ).pack(pady=20)

def interface_descriptografar():
    limpar_content()

    ctk.CTkLabel(content_frame, text="Descriptografar Texto", font=("Arial", 16, "bold")).pack(pady=10)

    texto_label = ctk.CTkLabel(content_frame, text="Texto para descriptografar:")
    texto_label.pack(anchor="w", padx=20)
    texto_entry = ctk.CTkTextbox(content_frame, height=100)
    texto_entry.pack(padx=20, pady=5, fill="x")

    def carregar_txt():
        path = filedialog.askopenfilename(filetypes=[("TXT", "*.txt")])
        if path:
            with open(path, "r", encoding="utf-8") as f:
                texto_entry.delete("1.0", "end")
                texto_entry.insert("1.0", f.read())
    ctk.CTkButton(content_frame, text="Carregar de Arquivo TXT", command=carregar_txt).pack(pady=5, padx=20)

    def carregar_chave():
        path = filedialog.askopenfilename(filetypes=[("TXT", "*.txt")])
        if path:
            with open(path, "r", encoding="utf-8") as f:
                for line in f.read().splitlines():
                    if line.startswith("Passo:"):
                        passo_var.set(line.split(":")[1].strip())
                    elif line.startswith("Seed:"):
                        seed_var.set(line.split(":")[1].strip())
    ctk.CTkButton(content_frame, text="Carregar Chave", command=carregar_chave).pack(pady=5, padx=20)

    # ctk.CTkLabel(content_frame, text="Modo de descriptografia:").pack(anchor="w", padx=20, pady=(10, 0))
    # ctk.CTkRadioButton(content_frame, text="Automático", variable=modo_var, value="auto").pack(anchor="w", padx=20)
    # ctk.CTkRadioButton(content_frame, text="Manual", variable=modo_var, value="manual").pack(anchor="w", padx=20)

    ctk.CTkLabel(content_frame, text="Seed:").pack(anchor="w", padx=20, pady=(10, 0))
    ctk.CTkEntry(content_frame, textvariable=seed_var).pack(padx=20, fill="x")

    ctk.CTkLabel(content_frame, text="Passo:").pack(anchor="w", padx=20, pady=(10, 0))
    ctk.CTkEntry(content_frame, textvariable=passo_var).pack(padx=20, fill="x")

    ctk.CTkButton(content_frame, text="Descriptografar",
                  command=lambda: executar_descriptografia(
                      texto_entry.get("1.0", "end-1c"), modo_var.get(), seed_var.get(), passo_var.get())
                  ).pack(pady=20)

def mostrar_resultado(titulo, texto, is_cripto=False, chave_info=None):
    global cripto_resultado, chave
    limpar_content()

    ctk.CTkLabel(content_frame, text=titulo, font=("Arial", 16, "bold")).pack(pady=10)

    result_box = scrolledtext.ScrolledText(content_frame, height=12, font=("Consolas", 12))
    result_box.pack(padx=20, pady=10, fill="both", expand=True)
    result_box.insert("1.0", texto)
    result_box.configure(state="disabled")

    if is_cripto:
        cripto_resultado, chave = texto, chave_info
        ctk.CTkButton(content_frame, text="Salvar Arquivos", command=salvar_em_arquivos).pack(pady=10)

# PROCESSAMENTO
def executar_criptografia(texto, seed, passo_str):
    if not texto:
        messagebox.showerror("Erro", "Digite um texto.")
        return
    try:
        seed_val = int(seed) if seed else int("".join([str(random.randint(0,9)) for _ in range(8)]))
        passo = [int(x) for x in passo_str.split()] if passo_str else [0]
        menor, maior = min(passo), max(passo)
        tabela = tables.gerar_tabelas(seed_val, menor, maior) if passo != [0] else tables.gerar_tabelas(seed_val)
        grafo = grafar(texto, tabela, passo, True, seed_val)
        mostrar_resultado("Texto Criptografado", grafo[0], True, f"Passo: {grafo[1]}\nSeed: {grafo[-1]}")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def executar_descriptografia(texto, modo, seed, passo_str):
    if not texto:
        messagebox.showerror("Erro", "Digite um texto.")
        return
    try:
        seed_val = int(seed)
        #passo = [int(x) for x in passo_str.split()]
        passo = [int(x) for x in passo_str.split()] if passo_str else [0]
        menor, maior = min(passo), max(passo)
        tabela = tables.gerar_tabelas(seed_val, menor, maior)
        t_inv = {k: {v: kk for kk, v in d.items()} for k, d in tabela.items()}
        desgrafo = desgrafar(texto, passo, t_inv)
        mostrar_resultado("Texto Descriptografado", desgrafo)
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def salvar_em_arquivos():
    global cripto_resultado, chave
    if not cripto_resultado or not chave:
        return
    texto_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if texto_path:
        with open(texto_path, "w", encoding="utf-8") as f:
            f.write(cripto_resultado)
    chave_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if chave_path:
        with open(chave_path, "w", encoding="utf-8") as f:
            f.write(chave)

# MENU
ctk.CTkButton(menu_frame, text="Início", command=interface_menu).pack(pady=10, padx=5, fill="x")
ctk.CTkButton(menu_frame, text="Criptografar", command=interface_criptografar).pack(pady=10, padx=5, fill="x")
ctk.CTkButton(menu_frame, text="Descriptografar", command=interface_descriptografar).pack(pady=10, padx=5, fill="x")

# INICIALIZAÇÃO
root.title("Sistema de Criptografia")

screenX, screenY = root.winfo_screenwidth(), root.winfo_screenheight()

screenSizeX = int(screenX * 0.5)
screenSizeY = int(screenY * 0.55)

root.minsize(screenSizeX, screenSizeY)
root.maxsize(screenX, screenY)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

frame = ctk.CTkFrame(root, fg_color="#001f3f")  # azul marinho
label = ctk.CTkLabel(root, text="Título", text_color="#f2f2f2")
button = ctk.CTkButton(root, text="Ação", fg_color="#003366", hover_color="#004080")
entry = ctk.CTkEntry(root, fg_color="#003366", text_color="#f2f2f2", placeholder_text_color="#cccccc")


interface_menu()
root.mainloop()
    