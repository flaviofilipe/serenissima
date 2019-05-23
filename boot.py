# https://python-googlesearch.readthedocs.io/en/latest/
from googlesearch import search, get_random_user_agent

def findSites(query, qnt=None, site=''):
    #site = site if site != '' else 'gov.br'
    site = [site if site else 'gov.br']
    for result in search(
            query, lang='pt', num=20, start=0, stop= int(qnt) if qnt else None, pause=1,
            domains=site,
            user_agent=get_random_user_agent()):
        yield result

def searchAll():
    query = input("Pesquisar: ")
    qnt = input("Quantidade de itens (em branco para exibir todos): ")
    return findSites(query, qnt)
    
def getSite():
    site = input('Site: ')
    if site[-6:] != 'gov.br':
        print("\nOpss!\nInforme um site governamental (ex: site.gov.br) ou pesquise em todos")
        return
    query = input('Pesquisar: ')
    quant = input("Quantidade de itens (em branco para exibir todos): ")
    return findSites(query, quant, site)

def getDocuments():
    return ['Disponívem em breve']