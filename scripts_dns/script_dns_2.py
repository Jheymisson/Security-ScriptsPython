import dns.resolver

dominio = input('Alvo: ')
registros = ['AAAA', 'A', 'MX', 'NS']

for registro in registros:
    try:
        resultado = dns.resolver.resolve(dominio, registro, raise_on_no_answer=False)
        if resultado.rrset is not None:
            print(resultado.rrset)
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.exception.Timeout):
        print(f"Não foi possível obter registros {registro} para {dominio}")
    except Exception as e:
        print(f"Erro ao consultar {registro} para {dominio}: {e}")
