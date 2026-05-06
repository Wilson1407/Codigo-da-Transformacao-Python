# TXT - Criar e ler arquivo

def criar_arquivo(nome_arquivo, conteudo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)
    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")
       
# função para ler o conteúdo de um arquivo
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            return conteudo
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")

# JSON - Salvar e carregar dicionário

import json 

def salvar_dicionario_em_json(nome_arquivo, dicionario):
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dicionario, arquivo)
    print(f"Dicionario salvo em '{nome_arquivo}' com sucesso!")
        
def carregar_dicionario_de_json(nome_arquivo):
    try:
        with open(nome_arquivo, 'r')as arquivo:
            dicionario = json.load(arquivo)
            return dicionario
    except FileNotFoundError:
        print(f"Erro: O arquivo ' {nome_arquivo}' não foi encontrado.")

# CSV - Sistema de notas

import csv

def salvar_notas_em_csv(nome_arquivo, notas):
    with open(nome_arquivo, 'w', newline='')as arquivo:
        escritor_csv = csv.writer(arquivo)
        escritor_csv.writerows(notas)
    print(f"Notas salvas em '{nome_arquivo}' com sucesso!")
        
def carregar_notas_de_csv(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            leitor_csv = csv.reader(arquivo)
            notas = list(leitor_csv)
            return notas
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")

#Backup de arquivos

import shutil

def criar_backup(arquivo_origem, arquivo_destino):
    try:
        shutil.copy(arquivo_origem, arquivo_destino)
        print(f"Backup criado com sucesso de '{arquivo_origem}' para '{arquivo_destino}'!")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_origem}' não foi encontrado.")

# Execução (Testes)

# TXT
criar_arquivo("teste.txt", "Olá mundo!")
print(ler_arquivo("teste.txt"))

# JSON
clientes = {"Ana": 25, "João": 30}
salvar_dicionario_em_json("clientes.json", clientes)
print(carregar_dicionario_de_json("clientes.json"))

# CSV
notas = [["Ana", 8], ["João", 9]]
salvar_notas_em_csv("notas.csv", notas)
print(carregar_notas_de_csv("notas.csv"))

# Backup
criar_backup("teste.txt", "backup_teste.txt")