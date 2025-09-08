from tkinter import filedialog
from datetime import datetime

def salvar_arquivo_com_nome_padrao(para_salvar):
    """Função que salva em Arquivo .txt"""
    
    # Gerar nome padrão
    nome_padrao = f"Texto_Grafado_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.txt"
    
    # Conteúdo do arquivo
    conteudo = f"Arquivo criado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    
    # Abrir janela para salvar
    caminho = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Arquivos de Texto", "*.txt")],
        title="Salvar arquivo",
        initialfile=nome_padrao
    )
    
    if caminho:
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        print(f"Arquivo salvo: {caminho}")

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

# Como usar:
if __name__ == "__main__":
    conteudo = abrir_arquivo_personalizado()
    if conteudo:
        print("Arquivo lido com sucesso!")
    else:
        print("Nenhum arquivo selecionado.")