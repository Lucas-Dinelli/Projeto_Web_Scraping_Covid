import requests
from bs4 import BeautifulSoup
from coleta.Territorio import Territorio


class ColetaDeDados:

    requisicao = None

    listaDeTerritorios = []

    def __init__(self, url):
        tabela = self.requisitarConexao(url)
        self.organizarElementos(tabela)

    # Promove a conexão e a extração do conteúdo solicitado da Web
    def requisitarConexao(self, url):
        self.requisicao = requests.get(url)
        soup = BeautifulSoup(self.requisicao.text, "html.parser")
        return soup.find_all('table', class_='wikitable sortable mw-collapsible')


    def adicionarTerritorioNaLista(self, territorio):
        self.listaDeTerritorios.append(territorio)

    def removerTerritorioDaLista(self, territorio):
        self.listaDeTerritorios.remove(territorio)

    def getListaDeTerritorios(self):
        return self.listaDeTerritorios

    # Pega os elementos da tabela coletada e retira somente o conjunto de dados necessário
    def organizarElementos(self, tabela):
        for item in tabela:
            listaDeItens = item.find_all('td')
            i = 0

            while i < len(listaDeItens)-1:
                nomeDoterritorio = listaDeItens[i].text.strip()

                if nomeDoterritorio.find("[") > -1:
                    nomeDoterritorio = nomeDoterritorio[:nomeDoterritorio.find("[")]

                if nomeDoterritorio.replace(" ", "").isalpha() or listaDeItens[i].text == "":
                    objetoTerritorio = Territorio(nomeDoterritorio, listaDeItens[i+1].text, listaDeItens[i+2].text,
                                                  listaDeItens[i+3].text, listaDeItens[i+4].text,
                                                  listaDeItens[i+5].text)

                    self.adicionarTerritorioNaLista(objetoTerritorio)
                    i = i + 5   # Salto para o próximo território
                elif not nomeDoterritorio.replace(" ", "").isalpha():
                    i = i + 1
