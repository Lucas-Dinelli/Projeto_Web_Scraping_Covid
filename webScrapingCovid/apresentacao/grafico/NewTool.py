import matplotlib.pyplot as plt
from matplotlib.backend_tools import ToolBase
from controle import ControladorTabela

# Classe que possibilita a criação de um novo ícone para a barra de ferramentas do matplotlib
class BotaoVoltar(ToolBase):
    image = r"..\img\voltar.png"
    description = 'Voltar para a tela anterior'

    def inserirParametro(self, lista):
        self.lista = lista

    # Detecta um clique sobre o ícone Voltar
    def trigger(self, *args, **kwargs):
        plt.close()
        ControladorTabela.ControladorTabela(self.lista)


# Classe que possibilita a criação de um novo ícone para a barra de ferramentas do matplotlib
class BotaoProximoGrafico(ToolBase):
    image = r"..\img\proximo.png"
    description = "Próximo gráfico"

    def indicarJanela(self, janela):
        self.janela = janela

    # Detecta um clique sobre o ícone Próximo
    def trigger(self, *args, **kwargs):
        self.janela.passarParaOProximoGrafico()