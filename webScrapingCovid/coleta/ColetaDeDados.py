import requests
from bs4 import BeautifulSoup
from coleta.Territorio import Territorio


class ColetaDeDados:

    listaDeTerritorios = []

    def __init__(self):
        tabelaCovid = self.requisitarConexao("https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data", 'table', 'wikitable')
        tabelaPopulacoes = self.requisitarConexao("https://www.worldometers.info/world-population/population-by-country", 'table', 'table')
        populacoes = self.organizarElementosPopulacionais(tabelaPopulacoes)
        self.organizarElementosCovid(tabelaCovid, populacoes)

    # Promove a conexão e a extração do conteúdo solicitado da Web
    def requisitarConexao(self, url, tipoDeElemento, className):
        requisicao = requests.get(url)
        soup = BeautifulSoup(requisicao.text, "html.parser")
        return soup.find_all(tipoDeElemento, class_=className)


    def adicionarTerritorioNaLista(self, territorio):
        self.listaDeTerritorios.append(territorio)

    def removerTerritorioDaLista(self, territorio):
        self.listaDeTerritorios.remove(territorio)

    def getListaDeTerritorios(self):
        return self.listaDeTerritorios


    # Pega os elementos da tabela coletada e retira somente o conjunto necessário de dados
    def organizarElementosPopulacionais(self, tabela):
        populacoes = {}
        for item in tabela:
            listaDeDados = item.find_all('td')
            salto = 12  # Valor referente ao salto que é dado na tabela para o próximo país
            for i in range(1, len(listaDeDados), salto):
                local = listaDeDados[i].text
                numeroDaPopulacao = listaDeDados[i + 1].text
                populacoes.__setitem__(local, numeroDaPopulacao)
        return populacoes


    # Pega os elementos da tabela coletada e retira somente o conjunto necessário de dados
    def organizarElementosCovid(self, tabela, populacoes):
        for item in tabela:
            listaDeValores = item.find_all('td')

            i = 0

            while listaDeValores[i].text == "":
                nomeTerritorio = self.retirarCaracteresIndesejados(listaDeValores[i+1].text)
                if not(nomeTerritorio.startswith("World") or nomeTerritorio.startswith("European")):
                    casos = listaDeValores[i+2].text
                    mortes = listaDeValores[i+3].text
                    numeroTotalDaPopulacao = populacoes.get(nomeTerritorio)

                    objetoTerritorio = Territorio(nomeTerritorio, casos, mortes, numeroTotalDaPopulacao)

                    self.adicionarTerritorioNaLista(objetoTerritorio)

                i = i + 4  # Salto para o próximo território

    def retirarCaracteresIndesejados(self, valorString:str):
        posicao = valorString.find("[")
        if(posicao > -1):
            return valorString[:posicao]
        return valorString