import customtkinter as ctk

# ===============================
# Funções
# ===============================


# ===============================
# Configuração da Janela Principal
# ===============================
janela = ctk.CTk()

# Aparencia
janela.title("Code-Decode Criptografia")
janela._set_appearance_mode("system")

# Tamanhos
janela.geometry("350x550")
janela.maxsize(width=700, height=1100)
janela.minsize(width=175, height=275)


# ===============================
# Frames Principais
# ===============================
frame_principal = ctk.CTkFrame(master=janela)
frame_principal.pack(pady=15, padx=15, fill="both", expand=True)


# Informações (modo criptografar/descriptografar)
frame_infos = ctk.CTkFrame(master=frame_principal)
frame_infos.pack(pady=5, padx=5, fill="both", expand=True)


# Área de entrada/dados
frame_geral = ctk.CTkFrame(master=frame_principal)
frame_geral.pack(pady=5, padx=5, fill="both", expand=True)


# Área de resultados
frame_resultados = ctk.CTkFrame(master=frame_principal)
frame_resultados.pack(pady=5, padx=5, fill="both", expand=True)


# ===============================
# Widgets do Frame de Informações
# ===============================
switch_modo = ctk.CTkSwitch(master=frame_infos, text="")
nome_modo = ctk.CTkLabel(master=frame_infos, text="Cryptografar")

switch_modo.pack(pady=5, padx=5, anchor="nw", fill="both")
nome_modo.pack(pady=5, padx=5, anchor="center", fill="both")


# ===============================
# Widgets Encryptar
# ===============================



# ===============================
# Widgets Descryptar
# ===============================



# ===============================
# Inicialização
# ===============================
janela.mainloop()