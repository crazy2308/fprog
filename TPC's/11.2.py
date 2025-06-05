# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 18:23:36 2025

@author: Utilizador
"""

def eh_ano_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def data_valida(dia, mes, ano):

    if mes < 1 or mes > 12:
        return False

    dias_no_mes = [31, 28, 31, 30, 31, 30,
                   31, 31, 30, 31, 30, 31]

    # Verifica se o dia está dentro do limite do mês
    if dia < 1 or dia > dias_no_mes[mes - 1]:
        return False

    return True


data = input("Digite uma data no formato dia/mês/ano: ")

try:
    partes = data.split('/')
    dia = int(partes[0])
    mes = int(partes[1])
    ano = int(partes[2])

    if data_valida(dia, mes, ano):
        print("A data é válida.")
    else:
        print("A data é inválida.")
except (ValueError, IndexError):
    print("Formato de data inválido. Use o formato dia/mês/ano.")
