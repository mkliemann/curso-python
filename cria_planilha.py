"""
Módulo: cria_planilha
Requisito: Retorna um objeto planilha (openpyxl) que calcula o resultado a partir de título (string), receitas (lista) e despesas (lista).
Autor: Mário J. Kliemann
Data: 28-11-2022
Versão: 0.0.1
"""

from openpyxl import Workbook

def cria_planilha(titulo, receitas, despesas):
    wb = Workbook()
    plan = wb.active
    plan.title = titulo
    plan['A1'] = "Receitas"
    plan['B1'] = "Despesas"
    plan['C1'] = "Resultado"
    total = 0.0
    i = 2
    for v in receitas:
        plan['A'+str(i)] = v
        plan['A'+str(i)].number_format = "#,##0.00"
        total += v
        i += 1
    i = 2
    for v in despesas:
        plan['B'+str(i)] = v
        plan['B'+str(i)].number_format = "#,##0.00"
        total -= v
        i += 1
    # Insere a fórmula que calcula o resultado
    # Há um problema aqui - a biblioteca openpyxl tem uma importante limitação: embora permita a inserção de fórmulas, não é capaz de efetuar os cálculos (que somente serão efetuados quando a planilha for aberta no Excel). Então o clálculo preceisará ser feito 'manualmente'.
    # plan['C2'] = "=SUM($A$2:$A999)-SUM($B$2:$B$999)"
    plan['C2'] = total
    plan['C2'].number_format = "#,##0.00"
    return wb

