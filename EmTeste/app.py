import customtkinter as ctk

# Configuração inicial
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


# Funções de exemplo (substitua pela lógica real)
def encriptar():
    texto = texto_encriptar.get()
    seed = seed_encriptar.get()
    passo = passo_encriptar.get()
    resultado_encriptar.configure(text=f"Encriptado: {texto} | Seed: {seed} | Passo: {passo}")

def descriptar():
    texto = texto_descriptar.get()
    seed = seed_descriptar.get()
    passo = passo_descriptar.get()
    resultado_descriptar.configure(text=f"Descriptado: {texto} | Seed: {seed} | Passo: {passo}")

# Funções para zerar os campos
def zerar_encriptar():
    texto_encriptar.delete(0, ctk.END)
    seed_encriptar.delete(0, ctk.END)
    passo_encriptar.delete(0, ctk.END)
    resultado_encriptar.configure(text="")

def zerar_descriptar():
    texto_descriptar.delete(0, ctk.END)
    seed_descriptar.delete(0, ctk.END)
    passo_descriptar.delete(0, ctk.END)
    resultado_descriptar.configure(text="")

# Alternar entre painéis
def alternar():
    if switch_var.get() == 1:
        frame_encriptar.pack_forget()
        frame_descriptar.pack(pady=20)
    else:
        frame_descriptar.pack_forget()
        frame_encriptar.pack(pady=20)

# Janela principal
app = ctk.CTk()
app.geometry("300x500")
app.title("Encriptador / Descriptador")

# Switch
switch_var = ctk.IntVar(value=0)
switch = ctk.CTkSwitch(app, text="Alternar Encriptador/Descriptador", variable=switch_var, command=alternar)
switch.place(relx=0.1, rely=0.5 - 0.9/2 - 0.05,)

# ===== FRAME ENCRIPTADOR =====
frame_encriptar = ctk.CTkFrame(app)
frame_encriptar.place(relx=0.5, rely=0.5, relwidth=0.9, relheight=0.9, anchor="center")

texto_encriptar = ctk.CTkEntry(frame_encriptar, placeholder_text="Texto a encriptar", width=300)
texto_encriptar.pack(pady=5)

seed_encriptar = ctk.CTkEntry(frame_encriptar, placeholder_text="Seed", width=300)
seed_encriptar.pack(pady=5)

passo_encriptar = ctk.CTkEntry(frame_encriptar, placeholder_text="Passo", width=300)    
passo_encriptar.pack(pady=5)

botao_encriptar = ctk.CTkButton(frame_encriptar, text="Encriptar", command=encriptar)
botao_encriptar.pack(pady=10)

botao_zerar_encriptar = ctk.CTkButton(frame_encriptar, text="Zerar Campos", command=zerar_encriptar)
botao_zerar_encriptar.pack(pady=5)

resultado_encriptar = ctk.CTkLabel(frame_encriptar, text="", wraplength=400)
resultado_encriptar.pack(pady=5)

# ===== FRAME DESCRIPTADOR =====
frame_descriptar = ctk.CTkFrame(app)

texto_descriptar = ctk.CTkEntry(frame_descriptar, placeholder_text="Texto a descriptar", width=300)
texto_descriptar.pack(pady=5)

seed_descriptar = ctk.CTkEntry(frame_descriptar, placeholder_text="Seed", width=300)
seed_descriptar.pack(pady=5)

passo_descriptar = ctk.CTkEntry(frame_descriptar, placeholder_text="Passo", width=300)
passo_descriptar.pack(pady=5)

botao_descriptar = ctk.CTkButton(frame_descriptar, text="Descriptar", command=descriptar)
botao_descriptar.pack(pady=10)

botao_zerar_descriptar = ctk.CTkButton(frame_descriptar, text="Zerar Campos", command=zerar_descriptar)
botao_zerar_descriptar.pack(pady=5)

resultado_descriptar = ctk.CTkLabel(frame_descriptar, text="", wraplength=400)
resultado_descriptar.pack(pady=5)

app.mainloop()
