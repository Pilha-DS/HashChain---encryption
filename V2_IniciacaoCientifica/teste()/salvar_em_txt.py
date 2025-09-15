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