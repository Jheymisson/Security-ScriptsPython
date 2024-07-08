import ipaddress

def calcular_redes(ip_cidr):
    network = ipaddress.ip_network(ip_cidr, strict=False)

    print('Endereco de rede: ', network.network_address)
    print('Endereco de broadcast: ', network.broadcast_address)
    print('Número total de enderecos: ', network.num_addresses)
    print('Máscara de sub-rede ', network.netmask)
    print('Enderecos utilizáveis: ', list(network.hosts()))

def main():
    ip_cidr = input('Digite o IP com a notacão CIDR (Ex: 192.168.0.1/24): ')
    calcular_redes(ip_cidr)

if __name__ == '__main__':
    main()