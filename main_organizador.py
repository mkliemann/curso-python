"""
Programa: organizador.py
Requisito: Aplicação que move os arquivos do diretório atual (CWD) para as pastas correspondetes à extansão do arquivo.
Autor: Mário J. Kliemann
Data: 01-12-2022
Versão: 0.0.1
"""

# Dependências

from classificador import *
import os

# Processamento

def main():
    arquivos = os.listdir()
    # print(arquivos)
    count = 0
    for arq in arquivos:
        # print(arq)
        count += ClassificaArquivo(arq)
    print(f"{count} arquivos movidos com sucesso.")
    return

    
if __name__ == "__main__":
    main()
    
