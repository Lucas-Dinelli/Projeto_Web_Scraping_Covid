from coleta import ColetaDeDados as coleta
from controle import ControladorTabela as controlador
from apresentacao.TelaDeAlerta import TelaDeAlerta


class ControladorInicial:
    def __init__(self):
        try:
            coletaDeDados = coleta.ColetaDeDados()

            controlador.ControladorTabela(coletaDeDados.getListaDeTerritorios())

        except Exception as excecao:
            mensagem = excecao
            TelaDeAlerta("Falha na Coleta", mensagem)
