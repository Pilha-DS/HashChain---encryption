import customtkinter as ctk

def mudou_var(*args):
    if var.get() == 1:  # switch ligado
        botao.place(relx=150, rely=200)
    else:  # switch desligado
        botao.place_forget()
    print("Novo valor:", var.get())

app = ctk.CTk()
app.geometry("400x700")

var = ctk.IntVar(value=0)  # começa ligado

# eventos
var.trace_add("write", mudou_var)

botao = ctk.CTkButton(app, text='grafar')
botao.place(relx=150, rely=200)  # já aparece na tela

switch = ctk.CTkSwitch(app, text='', variable=var)
switch.pack(pady=20)

app.mainloop()

