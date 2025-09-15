# imports
import customtkinter as ctk

# variaveis
janela = ctk.CTk()
t_modo = ctk.BooleanVar(False)

# funcoes
def trocar_cor(self, *args):
    estado = "Ligado" if self.switch_var.get() else "Desligado"
    self.label.configure(text=f"Estado: {estado}")
    print(f"Switch alterado para: {estado}")

# janela princial
janela.minsize(300, 500)

# aparencia da janela principal
janela.geometry("480x800")
ctk.set_appearance_mode("system")

# configuracao frame principal
frame_principal = ctk.CTkFrame(master=janela)
frame_principal.pack(pady=10, padx=10, fill="both")

# criar widgets
trocar_modo = ctk.CTkSwitch(master=frame_principal, text="TrocarCor", variable=t_modo, command=trocar_cor("red"),)

frame_crypto = ctk.CTkFrame(master=frame_principal)
text_cryp = ctk.CTkEntry(master=frame_crypto)

frame_descrypto = ctk.CTkFrame(master=frame_principal)
text_descryp = ctk.CTkEntry(master=frame_descrypto)


# inicializa aplicação
janela.mainloop()