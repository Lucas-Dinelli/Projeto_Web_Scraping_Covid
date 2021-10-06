from controle import ControladorDados as controladorPai
from apresentacao.grafico import Grafico


class ControladorGrafico(controladorPai.ControladorDados):

    listaDeNomesDosTerritorios = []

    listaDeValores = []

    labelEixoY = None

    representacao = None

    listaDeRepresentacoes = []


    def __init__(self, listaDeTerritorios, representacao, listaDeRepresentacoes):
        super().__init__(listaDeTerritorios)
        self.setRepresentacao(representacao)
        self.setListaDeRepresentacoes(listaDeRepresentacoes)
        self.organizar()
        Grafico.Grafico(self)           # Chama a tela do Gráfico


    def getListaDeNomesDosTerritorios(self):
        return self.listaDeNomesDosTerritorios


    def getListaDeValores(self):
        return self.listaDeValores


    def getLabelEixoY(self):
        return self.labelEixoY


    def getRepresentacao(self):
        return self.representacao


    def getListaDeRepresentacoes(self):
        return self.listaDeRepresentacoes


    def setListaDeNomesDosTerritorios(self, listaDeNomesDosTerritorios):
        self.listaDeNomesDosTerritorios = listaDeNomesDosTerritorios


    def setListaDeValores(self, listaDeValores):
        self.listaDeValores = listaDeValores


    def setLabelEixoY(self, labelEixoY):
        self.labelEixoY = labelEixoY


    def setRepresentacao(self, representacao):
        self.representacao = representacao


    def setListaDeRepresentacoes(self, listaDeRepresentacoes):
        self.listaDeRepresentacoes = listaDeRepresentacoes

    # Pega e organiza os componentes para o gráfico (como os valores do Eixo X e as labels do Eixo Y) a partir da lista de territórios ordenada de acordo com a representação selecionada
    def organizar(self):
        self.setListaDeTerritoriosOrdenada(self.getRepresentacao())
        tamanho = len(self.getListaDeTerritoriosOrdenada())
        listaDeNomesDosTerritorios = []
        listaDeValores = []

        for i in range(tamanho-1, tamanho-21, -1):

            territorio = self.getListaDeTerritoriosOrdenada()[i]

            listaDeNomesDosTerritorios.append(territorio.getNome())

            if self.getRepresentacao().lower() == "casos":
                listaDeValores.append(territorio.getCasos())
                self.setLabelEixoY("")

            elif self.getRepresentacao().lower() == "mortes":
                listaDeValores.append(territorio.getMortes())
                self.setLabelEixoY("")

            elif self.getRepresentacao().lower() == "taxa de letalidade":
                listaDeValores.append(territorio.getTaxaDeLetalidade())
                self.setLabelEixoY("Porcentagem (%)")

            elif self.getRepresentacao().lower() != "local":
                listaDeValores.append(territorio.getMortesPorMilhaoDeHabitantes())
                self.setLabelEixoY("")

        self.setListaDeNomesDosTerritorios(listaDeNomesDosTerritorios)
        self.setListaDeValores(listaDeValores)

    # Possibilita mudar da representação atual para a seguinte na lista de representações
    def passarParaAProximaRepresentacao(self):
        indiceAtual = self.getListaDeRepresentacoes().index(self.getRepresentacao())

        if indiceAtual == len(self.getListaDeRepresentacoes())-1:
            self.setRepresentacao(self.getListaDeRepresentacoes()[0])

        else:
            self.setRepresentacao(self.getListaDeRepresentacoes()[indiceAtual+1])




