import boot

query = input("Pesquisar sites do governo: ")
estado = input("Estado especififico (ex: ba): ")
quant = input("Quantidade de itens (em branco para exibir todos): ")
site = [estado + '.gov.br' if estado else 'gov.br']

def main():
    results = boot.findSites(query, estado, quant, site)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()