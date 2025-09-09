import customtkinter as ctk

# variaveis,
janela = ctk.CTk()
modo_c_d = 0

# funcoes
def trocar_cor(self, other, color, color2, p_color, modo_):
        global modo_c_d
        if modo_c_d == modo_:
            modo_c_d = 0
            self.configure(fg_color=p_color)
        else:
            modo_c_d = modo_
            self.configure(fg_color=color)
            other.configure(fg_color=color2)

# aparencia da janela
janela.geometry("400x650")
janela.minsize(300, 500)
janela.title("software de cryptografia")
janela._set_appearance_mode("system")

# cria o frame principal da aplicacao
frame_principal = ctk.CTkFrame(master=janela)
frame_principal.pack(pady=10, padx=10, expand=True, fill="both")

# cria os widgets principais.
frame_botoes = ctk.CTkFrame(master=frame_principal)
frame_botoes.pack(pady=10, padx=5, anchor="n")

modo_crypto = ctk.CTkButton(master=frame_botoes, text="encryptar")
modo_descrypto = ctk.CTkButton(master=frame_botoes, text="descryptar")

modo_crypto.grid(row=0, column=1, padx=5)
modo_crypto.configure(fg_color="green", hover_color="darkgreen", command=lambda: trocar_cor(modo_crypto, modo_descrypto, "red", "blue", "green", 1))

modo_descrypto.grid(row=0, column=0, padx=5)
modo_descrypto.configure(fg_color="blue", hover_color="darkblue", command=lambda: trocar_cor(modo_descrypto, modo_crypto, "red", "green", "blue", 2))

# inicializa aplicacao
janela.mainloop()