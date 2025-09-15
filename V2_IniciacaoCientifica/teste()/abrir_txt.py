import tkinter as tk
from tkinter import filedialog

def abrir_arquivo_personalizado():
    """Abre uma janela para selecionar e ler um arquivo de texto"""
    
    # Esconder a janela principal do tkinter
    root = tk.Tk()
    root.withdraw()
    
    # Abrir janela para selecionar arquivo
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo de texto",
        filetypes=[
            ("Arquivos de Texto", "*.txt"),
            ("Todos os arquivos", "*.*")
        ]
    )
    
    if caminho_arquivo:
        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
            
            print(f"Arquivo aberto: {caminho_arquivo}")
            print("Conteúdo:")
            print("-" * 40)
            print(conteudo)
            print("-" * 40)
            
            return conteudo
            
        except Exception as e:
            print(f"Erro ao abrir arquivo: {e}")
            return None
    
    return None