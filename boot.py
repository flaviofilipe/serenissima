# https://python-googlesearch.readthedocs.io/en/latest/
from googlesearch import search, get_random_user_agent

def findSites(query, estado='', qnt=None, site='gov.br'):
    for result in search(
            query, lang='pt', num=20, start=0, stop= int(qnt) if qnt else None, pause=2,
            domains=site,
            user_agent=get_random_user_agent()):
        yield result
