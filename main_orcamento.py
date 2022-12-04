"""
Programa: Orcamento
Requisito: Cria uma planilha denominada orcamento.xlsx contendo o resultado do orçamento do mês de novembro.
Autor: Mário J. Kliemann
Data: 28-11-2022
Versão: 0.0.1
"""
from cria_planilha import *

def main():
    mes = "Novembro"
    receitas = [5000.0]  # Salário
    despesas = [1200.0, 230.0, 180.0]  # Alimentação, Energia, Transporte
    orcamento = cria_planilha(mes, receitas, despesas)
    orcamento.save("orcamento.xlsx")
    # print(f"A planilha orcamento.xlsx foi criada com sucesso.")
    print("O resultado do orçamento de {} foi de R$ {}.".format(mes, orcamento.active['C2'].value))
    return

if __name__ == "__main__":
    main()

