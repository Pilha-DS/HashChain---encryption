import customtkinter as ctk
from tkinter import messagebox, scrolledtext, filedialog
import tables
from grafador import grafar
import random
from desgrafar import desgrafar
import os

# Configuração inicial
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Variáveis globais
root = ctk.CTk()
current_frame = None
seed_var = ctk.StringVar()
passo_var = ctk.StringVar()
texto_var = ctk.StringVar()
resultado_var = ctk.StringVar()
modo_var = ctk.StringVar(value="auto")
cripto_resultado = ""  # Para armazenar o resultado da criptografia
chave = ""  # armazenar a chave para descriptografia

# Dicionário de ações possíveis
possiveis_acoes = {
    "dcri": {"d", "D", "Descriptografar", "descriptografar", "Desgrafar", "desgrafar"},
    "crip": {"c", "C", "Criptografar", "criptografar", "Grafar", "grafar"},
    "comp": {"Compactar", "compactar", "com", "Com", "COM"},
    "desc": {"Descompactar", "descompactar", "des", "Des", "DES"},
    "sim": {"sim", "SIM", "Sim", "s", "S"},
    "nao": {"NAO", "NÃO", "Não", "Nao", "nao", "não", "N", "n"},
    "auto": {"a", "A", "Auto", "auto", "automatica", "Automatica", "AUTO"},
    "manual": {"M", "m", "Manual", "manual", "MANUAL"}
}

# Funções auxiliares
def limpar_frame():
    global current_frame
    if current_frame:
        current_frame.destroy()
    current_frame = ctk.CTkFrame(root)
    current_frame.pack(fill="both", expand=True, padx=20, pady=20)

def voltar_menu_principal():
    limpar_frame()
    criar_menu_principal()

def mostrar_resultado(titulo, texto, is_cripto=False, chave_info=None):
    global cripto_resultado, chave
    limpar_frame()
    
    titulo_label = ctk.CTkLabel(current_frame, text=titulo, font=("Arial", 16, "bold"))
    titulo_label.pack(pady=10)
    
    resultado_text = scrolledtext.ScrolledText(current_frame, height=10, width=60, font=("Consolas", 12))
    resultado_text.pack(pady=10, padx=10, fill="both", expand=True)
    resultado_text.insert("1.0", texto)
    resultado_text.configure(state="disabled")
    
    # Se for resultado de criptografia, adicionar botão para salvar
    if is_cripto:
        cripto_resultado = texto
        chave = chave_info
        btn_salvar = ctk.CTkButton(current_frame, text="Salvar em Arquivos Separados", 
                                  command=salvar_em_arquivos_separados, fg_color="#28a745")
        btn_salvar.pack(pady=5)
    
    btn_voltar = ctk.CTkButton(current_frame, text="Voltar ao Menu", command=voltar_menu_principal)
    btn_voltar.pack(pady=10)

def salvar_em_arquivos_separados():
    global cripto_resultado, chave
    if not cripto_resultado or not chave:
        messagebox.showwarning("Aviso", "Nenhum resultado para salvar.")
        return
    
    # Salvar texto criptografado
    texto_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")],
        title="Salvar texto criptografado",
        initialfile="texto_criptografado"
    )
    
    if texto_path:
        try:
            # Salvar apenas o texto criptografado (sem o cabeçalho)
            with open(texto_path, 'w', encoding='utf-8') as file:
                file.write(cripto_resultado)
            
            # Salvar chave (apenas seed e passo)
            chave_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")],
                title="Salvar chave de criptografia",
                initialfile="chave"
            )
            
            if chave_path:
                with open(chave_path, 'w', encoding='utf-8') as file:
                    file.write(chave)
                
                messagebox.showinfo("Sucesso", f"Arquivos salvos com sucesso:\nTexto: {texto_path}\nChave: {chave_path}")
            else:
                messagebox.showinfo("Info", "Arquivo de texto salvo, mas operação de salvar chave cancelada.")
                
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao salvar arquivos:\n{str(e)}")

# Funções de interface
def criar_menu_principal():
    limpar_frame()
    
    titulo = ctk.CTkLabel(current_frame, text="Sistema de Criptografia", font=("Arial", 20, "bold"))
    titulo.pack(pady=20)
    
    btn_cripto = ctk.CTkButton(current_frame, text="Criptografar", command=interface_criptografar, 
                              height=40, font=("Arial", 14))
    btn_cripto.pack(pady=10, fill="x", padx=50)
    
    btn_descripto = ctk.CTkButton(current_frame, text="Descriptografar", command=interface_descriptografar, 
                                 height=40, font=("Arial", 14))
    btn_descripto.pack(pady=10, fill="x", padx=50)
    
    btn_sair = ctk.CTkButton(current_frame, text="Sair", command=root.destroy, 
                            height=40, font=("Arial", 14), fg_color="#d9534f")
    btn_sair.pack(pady=10, fill="x", padx=50)

def interface_criptografar():
    limpar_frame()
    
    titulo = ctk.CTkLabel(current_frame, text="Criptografar Texto", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)
    
    # Campo de texto
    texto_label = ctk.CTkLabel(current_frame, text="Texto para criptografar:")
    texto_label.pack(pady=(20, 5))
    
    texto_entry = ctk.CTkTextbox(current_frame, height=100)
    texto_entry.pack(pady=5, padx=50, fill="x")
    
    # Frame para seed
    seed_frame = ctk.CTkFrame(current_frame)
    seed_frame.pack(pady=10, padx=50, fill="x")
    
    seed_label = ctk.CTkLabel(seed_frame, text="Seed (opcional):")
    seed_label.pack(pady=5, anchor="w")
    
    seed_entry = ctk.CTkEntry(seed_frame, textvariable=seed_var)
    seed_entry.pack(pady=5, fill="x")
    
    # Botão para gerar seed aleatória
    def gerar_seed_aleatoria():
        sed = [str(random.randint(0, 9)) for _ in range(8)]
        seed_var.set("".join(sed))
    
    btn_gerar_seed = ctk.CTkButton(seed_frame, text="Gerar Seed Aleatória", 
                                  command=gerar_seed_aleatoria, width=150)
    btn_gerar_seed.pack(pady=5)
    
    # Frame para passo
    passo_frame = ctk.CTkFrame(current_frame)
    passo_frame.pack(pady=10, padx=50, fill="x")
    
    passo_label = ctk.CTkLabel(passo_frame, text="Passo (opcional, separado por espaços):")
    passo_label.pack(pady=5, anchor="w")
    
    passo_entry = ctk.CTkEntry(passo_frame, textvariable=passo_var)
    passo_entry.pack(pady=5, fill="x")
    
    # Botões
    btn_frame = ctk.CTkFrame(current_frame)
    btn_frame.pack(pady=20, fill="x", padx=50)
    
    btn_voltar = ctk.CTkButton(btn_frame, text="Voltar", command=voltar_menu_principal)
    btn_voltar.pack(side="left", padx=10)
    
    btn_cripto = ctk.CTkButton(btn_frame, text="Criptografar", command=lambda: executar_criptografia(
        texto_entry.get("1.0", "end-1c"), seed_var.get(), passo_var.get()))
    btn_cripto.pack(side="right", padx=10)

def interface_descriptografar():
    limpar_frame()
    
    titulo = ctk.CTkLabel(current_frame, text="Descriptografar Texto", font=("Arial", 16, "bold"))
    titulo.pack(pady=10)
    
    # Campo de texto
    texto_label = ctk.CTkLabel(current_frame, text="Texto para descriptografar:")
    texto_label.pack(pady=(20, 5))
    
    texto_entry = ctk.CTkTextbox(current_frame, height=100)
    texto_entry.pack(pady=5, padx=50, fill="x")
    
    # Opção para carregar de arquivo
    def carregar_de_arquivo():
        file_path = filedialog.askopenfilename(
            filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")],
            title="Selecionar arquivo criptografado"
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    conteudo = file.read()
                    texto_entry.delete("1.0", "end")
                    texto_entry.insert("1.0", conteudo)
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao carregar arquivo:\n{str(e)}")
    
    btn_carregar = ctk.CTkButton(current_frame, text="Carregar de Arquivo TXT", 
                                command=carregar_de_arquivo, width=200)
    btn_carregar.pack(pady=5)
    
    # Opção para carregar chave
    def carregar_chave():
        file_path = filedialog.askopenfilename(
            filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")],
            title="Selecionar arquivo de chave"
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    conteudo = file.read()
                    # Extrair seed e passo do conteúdo da chave
                    lines = conteudo.strip().split('\n')
                    for line in lines:
                        if line.startswith('Passo:'):
                            passo_var.set(line.split(':')[1].strip())
                        elif line.startswith('Seed:'):
                            seed_var.set(line.split(':')[1].strip())
            except Exception as e:
                messagebox.showerror("Erro", f"Falha ao carregar chave:\n{str(e)}")
    
    btn_carregar_chave = ctk.CTkButton(current_frame, text="Carregar Chave", 
                                      command=carregar_chave, width=200)
    btn_carregar_chave.pack(pady=5)
    
    # Modo de operação
    modo_frame = ctk.CTkFrame(current_frame)
    modo_frame.pack(pady=10, padx=50, fill="x")
    
    modo_label = ctk.CTkLabel(modo_frame, text="Modo de descriptografia:")
    modo_label.pack(pady=5, anchor="w")
    
    auto_radio = ctk.CTkRadioButton(modo_frame, text="Automático", variable=modo_var, value="auto")
    auto_radio.pack(pady=5, anchor="w")
    
    manual_radio = ctk.CTkRadioButton(modo_frame, text="Manual", variable=modo_var, value="manual")
    manual_radio.pack(pady=5, anchor="w")
    
    # Frame para seed (visível apenas no modo manual)
    seed_frame = ctk.CTkFrame(current_frame)
    seed_frame.pack(pady=10, padx=50, fill="x")
    
    seed_label = ctk.CTkLabel(seed_frame, text="Seed:")
    seed_label.pack(pady=5, anchor="w")
    
    seed_entry = ctk.CTkEntry(seed_frame, textvariable=seed_var)
    seed_entry.pack(pady=5, fill="x")
    
    # Frame para passo (visível apenas no modo manual)
    passo_frame = ctk.CTkFrame(current_frame)
    passo_frame.pack(pady=10, padx=50, fill="x")
    
    passo_label = ctk.CTkLabel(passo_frame, text="Passo (separado por espaços):")
    passo_label.pack(pady=5, anchor="w")
    
    passo_entry = ctk.CTkEntry(passo_frame, textvariable=passo_var)
    passo_entry.pack(pady=5, fill="x")
    
    # Botões
    btn_frame = ctk.CTkFrame(current_frame)
    btn_frame.pack(pady=20, fill="x", padx=50)
    
    btn_voltar = ctk.CTkButton(btn_frame, text="Voltar", command=voltar_menu_principal)
    btn_voltar.pack(side="left", padx=10)
    
    btn_descripto = ctk.CTkButton(btn_frame, text="Descriptografar", command=lambda: executar_descriptografia(
        texto_entry.get("1.0", "end-1c"), modo_var.get(), seed_var.get(), passo_var.get()))
    btn_descripto.pack(side="right", padx=10)

# Funções de processamento
def executar_criptografia(texto, seed, passo_str):
    if not texto:
        messagebox.showerror("Erro", "Por favor, insira um texto para criptografar.")
        return
    
    try:
        # Processar seed
        if seed:
            seed_val = int(seed)
        else:
            # Gerar seed aleatória
            sed = []
            for c in range(1, 9):
                sed.append(str(random.randint(0, 9)))
            seed_val = int("".join(sed))
        
        # Processar passos
        pas = []
        passo = []
        if passo_str:
            for c in passo_str:
                if c != " ":
                    pas.append(c)
                elif c == " ":
                    passo.append(int("".join(pas)))
                    pas.clear()
            if pas:
                passo.append(int("".join(pas)))
        else:
            passo = [0]
        
        # Encontrar menor e maior passo
        menor_passo = min(passo) if passo else 0
        maior_passo = max(passo) if passo else 0
        
        # Criar tabela
        if passo == [0]:
            tabela = tables.gerar_tabelas(seed_val)
        else:
            tabela = tables.gerar_tabelas(seed_val, menor_passo, maior_passo)
        
        # Criptografar
        grafo = grafar(texto, tabela, passo, True, int(seed_val))
        
        # Formatar resultado para exibição
        resultado_exibicao = grafo[0]
        
        # Criar informação da chave para salvar em arquivo separado (apenas passo e seed)
        chave_info = f"Passo: {grafo[1]}\nSeed: {grafo[-1]}"
        
        # Mostrar resultado com opção de salvar
        mostrar_resultado("Texto Criptografado com Sucesso", resultado_exibicao, is_cripto=True, chave_info=chave_info)
        
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro durante a criptografia:\n{str(e)}")

def executar_descriptografia(texto, modo, seed, passo_str):
    if not texto:
        messagebox.showerror("Erro", "Por favor, insira um texto para descriptografar.")
        return
    
    try:
        if modo == "manual":
            if not seed:
                messagebox.showerror("Erro", "No modo manual, é necessário informar a seed.")
                return
            
            seed_val = int(seed)
            
            # Processar passos
            pas = []
            passo = []
            if passo_str:
                for c in passo_str:
                    if c != " ":
                        pas.append(c)
                    elif c == " ":
                        passo.append(int("".join(pas)))
                        pas.clear()
                if pas:
                    passo.append(int("".join(pas)))
            else:
                messagebox.showerror("Erro", "No modo manual, é necessário informar o passo.")
                return
            
            # Encontrar menor e maior passo
            menor_passo = min(passo) if passo else 0
            maior_passo = max(passo) if passo else 0
            
            # Criar tabela
            tabela = tables.gerar_tabelas(seed_val, menor_passo, maior_passo)
            
            # Inverter tabela
            t_invertida = {k: {v: kk for kk, v in d.items()} for k, d in tabela.items()}
            
            # Descriptografar
            desgrafo = desgrafar(texto, passo, t_invertida)
            
            # Mostrar resultado
            mostrar_resultado("Texto Descriptografado com Sucesso", desgrafo)
            
        else:
            # Modo automático (implementar lógica de detecção automática)
            messagebox.showinfo("Info", "Modo automático selecionado. Esta funcionalidade será implementada em breve.")
            
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro durante a descriptografia:\n{str(e)}")

# Inicialização da aplicação
def iniciar_aplicacao():
    global root
    root.title("Sistema de Criptografia")
    root.geometry("600x700")
    root.minsize(600, 700)
    
    criar_menu_principal()
    root.mainloop()

# Iniciar a aplicação
if __name__ == "__main__":
    iniciar_aplicacao()