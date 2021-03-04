from controle import ControladorDados as controladorPai
from controle import ControladorGrafico as controladorGrafico
from apresentacao.tabela import Tabela


class ControladorTabela(controladorPai.ControladorDados):

    def __init__(self, listaDeTerritorios):
        super().__init__(listaDeTerritorios)
        super().setListaDeTerritoriosOrdenada("local")  # Inicia a lista de territórios ordenando-a pelo nome dos territórios
        Tabela.Tabela(self)

    # Chama o controlador do gráfico para iniciá-lo
    def iniciarGrafico(self, representacao, listaDeRepresentacoes):
        controladorGrafico.ControladorGrafico(super().getListaDeTerritorios(), representacao, listaDeRepresentacoes)