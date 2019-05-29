from flask import render_template
from app import app

@app.route("/")
def index():
     result_search = [
          {
               'link': 'http://www.mctic.gov.br',
               'descricao': 'O MCTIC – Ministério da Ciência, Tecnologia, Inovações e Comunicações foi comunicado nesta quarta-feira (06.02.2019) que aplicativos potencialmente ...'
          },
          {
               'link': 'www.int.gov.br',
               'descricao': 'Instituto Nacional de Tecnologia. ... Instituto Nacional de Tecnologia. Ministério da Ciência, Tecnologia, Inovações e Comunicações ...'
          }
          
     ]

     context = {
         'title': 'Página Inicial',
         'result_search': result_search
    }
     return render_template('index.html', context=context)
