from coleta import ColetaDeDados as coleta
from controle import ControladorTabela as controlador
from apresentacao.TelaDeAlerta import TelaDeAlerta


class ControladorInicial:
    def __init__(self):
        try:
            coletaDeDados = coleta.ColetaDeDados("https://pt.wikipedia.org/wiki/Predefini%C3%A7%C3%A3o:Dados_da_pandemia_de_COVID-19")

            controlador.ControladorTabela(coletaDeDados.getListaDeTerritorios())

        except Exception as excecao:
            mensagem = "Verifique sua conexão!"
            TelaDeAlerta("Falha na Coleta", mensagem)