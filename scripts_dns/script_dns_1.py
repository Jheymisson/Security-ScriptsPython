import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

def nomes_invalidos(nome):
    MAX_LABEL_LENGTH = 63
    try:
        nome_idna = nome.encode('idna').decode()
        labels = nome_idna.split('.')
        return all(0 < len(label) <= MAX_LABEL_LENGTH for label in labels)
    except UnicodeError:
        return False

def verifica_subdominio(nome):
    if not nomes_invalidos(DNS):
        return f"Nome inválido ou problema de codificação: {nome}"
    try:
        endereco_ip = socket.gethostbyname(nome)
        return f"Resolvido: {nome} -> {endereco_ip}"
    except socket.gaierror:
        return f"Não encontrado: {nome}"
    except UnicodeError as e:
        return f"Erro ao processar {nome}: {e}"

dominio = input('Alvo: ')
listaBrute = '../wordlists/wordlist_small.txt'

print(f"Iniciando busca por subdomínios de: {dominio}")

tarefas = []

with ThreadPoolExecutor(max_workers=5) as executor:
    with open(listaBrute, 'r') as arquivo:
        for nome in arquivo:
            nome = nome.strip() 
            if nome:  
                DNS = nome + '.' + dominio
                tarefa = executor.submit(verifica_subdominio, DNS)
                tarefas.append(tarefa)


for tarefas_completas in as_completed(tarefas):
    print(tarefas_completas.result())

print("Busca concluída.")
