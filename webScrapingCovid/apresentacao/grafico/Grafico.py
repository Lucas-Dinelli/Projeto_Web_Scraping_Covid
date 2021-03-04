import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams["toolbar"] = "toolmanager"
from apresentacao.grafico import NewTool


class Grafico:

    listaDeAnotacoes = []

    def __init__(self, controlador):
        self.fig = plt.figure()
        self.controlador = controlador
        self.construirEstrutura(self.controlador.getListaDeNomesDosTerritorios(), self.controlador.getListaDeValores(), "", self.controlador.getLabelEixoY(), self.controlador.getRepresentacao(), "red")
        self.apresentarGrafico()


    def construirEstrutura(self, eixoX, eixoY, labelEixoX, labelEixoY, tituloDoGrafico, corDoGrafico):
        self.barras = plt.bar(eixoX, eixoY, color=corDoGrafico, width=0.3)
        plt.xticks(eixoX, rotation=25, horizontalalignment='right', fontsize=8)
        plt.xlabel(labelEixoX)
        plt.ylabel(labelEixoY)
        plt.title(tituloDoGrafico)

    # Responsável pelo aparecimento do valor da barra do gráfico cujo mouse está passando por cima
    def hover(self, event):
        if event.xdata != None:
            posicaoXDoMouse = event.xdata
            stringDaPosicaoXDoMouse = str(posicaoXDoMouse)
            stringDaPosicaoXDoMouse = stringDaPosicaoXDoMouse[:stringDaPosicaoXDoMouse.find(".") + 3]

            if len(stringDaPosicaoXDoMouse) < 4:
                stringDaPosicaoXDoMouse = stringDaPosicaoXDoMouse + "0"
            posicaoXDoMouse = float(stringDaPosicaoXDoMouse)

            for barra in self.barras:
                if posicaoXDoMouse >= barra.get_x() and posicaoXDoMouse <= barra.get_x() + \
                        barra.get_width() and event.ydata <= barra.get_height():
                    self.apagarAnotacoes()
                    valor = self.controlador.formatarApresentacaoDeDado(barra.get_height())
                    anotacao = plt.annotate(valor, xy=(event.xdata, event.ydata),
                                            xytext=(20, 20), textcoords="offset points",
                                            bbox=dict(boxstyle="round", fc="lightgreen", alpha=0.9),
                                            arrowprops=dict(arrowstyle="->"))
                    self.listaDeAnotacoes.append(anotacao)
                    self.fig.canvas.draw_idle()
                    break
                else:
                    self.apagarAnotacoes()
        else:
            self.apagarAnotacoes()

    # Torna invisível todas as anotações (valores das barras) da lista de anotações e, depois, limpa essa lista
    def apagarAnotacoes(self):
        for anotacao in self.listaDeAnotacoes:
            anotacao.set_visible(False)
        self.fig.canvas.draw_idle()
        self.listaDeAnotacoes.clear()

    # Insere o ícone Voltar na barra de ferramentas para que se possa retornar à tela anterior
    def inserirBotaoVoltar(self):
        novaFerramenta = NewTool.BotaoVoltar
        novaFerramenta.inserirParametro(novaFerramenta, self.controlador.getListaDeTerritorios())
        self.fig.canvas.manager.toolmanager.add_tool('voltar', novaFerramenta)
        self.fig.canvas.manager.toolbar.add_tool('voltar', 'toolgroup')

    # Insere o ícone Próximo na barra de ferramentas para que se possa passar para o gráfico seguinte
    def inserirBotaoProximoGrafico(self):
        novaFerramenta = NewTool.BotaoProximoGrafico
        novaFerramenta.indicarJanela(novaFerramenta, self)
        self.fig.canvas.manager.toolmanager.add_tool('proximo', novaFerramenta)
        self.fig.canvas.manager.toolbar.add_tool('proximo', 'toolgroup')

    # Remove ícones/botões da barra de ferramentas do matplotlib
    def removerBotoesDaToolbar(self, nomesDosBotoes):
        for nome in nomesDosBotoes:
            self.fig.canvas.manager.toolmanager.remove_tool(nome)


    def exibirValoresAoPassarOMouse(self):
        self.fig.canvas.mpl_connect("motion_notify_event", self.hover)  # Capta o evento ocorrido no gráfico

    # Desenha o novo gráfico na tela
    def passarParaOProximoGrafico(self):
        plt.cla()
        self.controlador.passarParaAProximaRepresentacao()
        self.controlador.organizar()
        self.construirEstrutura(self.controlador.getListaDeNomesDosTerritorios(), self.controlador.getListaDeValores(), "", self.controlador.getLabelEixoY(), self.controlador.getRepresentacao(), "red")
        plt.gcf().canvas.draw_idle()


    def apresentarGrafico(self):
        self.inserirBotaoProximoGrafico()
        self.inserirBotaoVoltar()
        self.removerBotoesDaToolbar(["subplots", "help"])
        self.exibirValoresAoPassarOMouse()
        plt.get_current_fig_manager().window.state('zoomed')   # Abre a janela de forma maximizada
        plt.show()
