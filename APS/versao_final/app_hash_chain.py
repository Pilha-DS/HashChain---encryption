# imports
import customtkinter as ctk

# variaveis
janela = ctk.CTk()
modo = 0

# funcoes
def trocar_modo(prin:list, widget:list, modo_:int ):
    """ parametros:
        prin: [objeto_principal, cor_para_mudar, cor_padrao, cor_hover, cor_padrao_hover, objeto_secundario]
        widget: [objeto_a_mudar, cor_para_mudar, cor_hover, objeto_secundario_a_mudar]
    """
    global modo
    if modo == modo_:
        prin[5].grid_remove()
        modo = 0
        prin[0].configure(fg_color=prin[2], hover_color=prin[4])
    else:
        modo = modo_
        prin[5].grid()
        prin[0].configure(fg_color=prin[1], hover_color=prin[3])
        widget[3].grid_remove()
        widget[0].configure(fg_color=widget[1], hover_color=widget[2])

# janela princial
janela.minsize(420, 700)
janela.maxsize(420, 700)


# aparencia da janela principal
janela.geometry("420x700")
ctk.set_appearance_mode("system")

# configuracao frame principal
frame_principal = ctk.CTkFrame(master=janela)
frame_principal.pack(pady=10, padx=10, fill="both", expand=True)

# botoes de troca de modo
frame_botoes = ctk.CTkFrame(frame_principal)
frame_botoes.pack(padx=10, pady=10)

modo_descrypto = ctk.CTkButton(master=frame_botoes, text="Descryptografar", command=lambda: trocar_modo(prin=[modo_descrypto, "#AC0006", "#00548B", "#6C0004", "#00365A", frame_descrypto], widget=[modo_crypto, "#00548B", "#00365A", frame_crypto], modo_=2))
modo_crypto = ctk.CTkButton(master=frame_botoes, text="Cryptografar", command=lambda: trocar_modo(prin=[modo_crypto, "#AC0006", "#00548B", "#6C0004", "#00365A", frame_crypto], widget=[modo_descrypto, "#00548B", "#00365A", frame_descrypto], modo_=1))

modo_crypto.configure(fg_color="#00548B", hover_color="#00365A")
modo_descrypto.configure(fg_color="#00548B", hover_color="#00365A")

# frame de controle
frame_controle = ctk.CTkFrame(master=frame_principal)
frame_controle.pack(padx=10, pady=10, expand=True, fill="both")
frame_controle.configure(fg_color="transparent")

frame_controle.grid_rowconfigure(0, weight=1)
frame_controle.grid_columnconfigure(0, weight=1)

modo_crypto.grid(row=0, column=0, pady=5, padx=5)
modo_descrypto.grid(row=0, column=1, pady=5, padx=5)

# frames dos modos
frame_crypto = ctk.CTkFrame(master=frame_controle)
frame_crypto.grid(row=0, column=0, sticky="nsew")
frame_crypto.grid_remove()

frame_descrypto = ctk.CTkFrame(master=frame_controle)
frame_descrypto.grid(row=0, column=0, sticky="nsew")
frame_descrypto.grid_remove()

#------------#
#---Crypto---#
#------------#
text_crypto = ctk.CTkLabel(master=frame_crypto, text="Cryptografar")
text_crypto.pack(pady=5, padx=5)



# inicializa aplicação
janela.mainloop()