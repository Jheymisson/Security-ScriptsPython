import whois 

try:
    alvo = input('Alvo: ')
    w = whois.whois(alvo)
    print(w)
    print(w.name_server)
except whois.parser.PywhoisError as e:
    print(f'Erro ao buscar informacoes: {e}')
except Exception as e:
    print(f'Ocorreu um erro inesperado: {e}')