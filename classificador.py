"""
Módulo: classificador.py
Requisito: Função modular que move o arquivo fornecido para a pasta 'documentos' ou 'planilhas' de acordo com sua extensão. Se a pasta não existir, ela é criada.
Autor: Mário J. Kliemann
Data: 01-12-2022
Versão: 0.0.1
"""

# Dependências

import os
import shutil

# Funções

def ClassificaArquivo(arq):
    destino = ""
    nome, extensao = os.path.splitext(arq)
    # print(f"Arquivo <{nome}> -- <{extensao}>")
    match extensao:
        case ".doc" | ".docx":
            destino = "documentos"
        case ".xls" | ".xlsx":
            destino = "planilhas"
        case _:
            return False
    if not os.path.isdir(destino):
        print(f"Criando a pasta '{destino}'")
        os.mkdir(".\\"+destino)
    try:
        print(f"Movendo arquivo '{arq}' para a pasta '{destino}'")
        shutil.move(arq, ".\\"+destino)
    except:
        print("*** Falha ao tentar mover esse arquivo!")
        return False
    return True
    
    