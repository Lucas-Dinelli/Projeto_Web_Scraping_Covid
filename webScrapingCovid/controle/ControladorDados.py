from coleta import Territorio as territorio

class ControladorDados:

    listaDeTerritorios = None

    listaDeTerritoriosOrdenada = None


    def __init__(self, listaDeTerritorios):
        self.setListaDeTerritorios(listaDeTerritorios)


    def getListaDeTerritorios(self):
        return self.listaDeTerritorios


    def setListaDeTerritorios(self, listaDeTerritorios):
        self.listaDeTerritorios = listaDeTerritorios


    def getListaDeTerritoriosOrdenada(self):
        return self.listaDeTerritoriosOrdenada

    # Reordena os elementos da lista de territórios de acordo com o critério escolhido
    def setListaDeTerritoriosOrdenada(self, criterioDeOrdenacao):
        criterioDeOrdenacao = criterioDeOrdenacao.lower()

        if criterioDeOrdenacao == "nome" or criterioDeOrdenacao == "local":
            self.listaDeTerritoriosOrdenada = sorted(self.getListaDeTerritorios(), key=territorio.Territorio.getNome)

        elif criterioDeOrdenacao == "caso" or criterioDeOrdenacao == "casos":
            self.listaDeTerritoriosOrdenada = sorted(self.getListaDeTerritorios(), key=territorio.Territorio.getCasos)

        elif criterioDeOrdenacao == "morte" or criterioDeOrdenacao == "mortes":
            self.listaDeTerritoriosOrdenada = sorted(self.getListaDeTerritorios(), key=territorio.Territorio.getMortes)

        elif criterioDeOrdenacao == "curado" or criterioDeOrdenacao == "curados":
            self.listaDeTerritoriosOrdenada = sorted(self.getListaDeTerritorios(), key=territorio.Territorio.getCurados)

        elif criterioDeOrdenacao == "taxa de letalidade":
            self.listaDeTerritoriosOrdenada = sorted(self.getListaDeTerritorios(), key=territorio.Territorio.getTaxaDeLetalidade)

        else:
            self.listaDeTerritoriosOrdenada = sorted(self.getListaDeTerritorios(), key=territorio.Territorio.getMortesPorMilhaoDeHabitantes)

    # Formata o dado, conforme seu tipo, para que ele possa ser apresentado de uma forma mais amigável
    def formatarApresentacaoDeDado(self, dado):
        dado = str(dado)
        dadoFormatado = ""

        if dado == "0":
            dadoFormatado = "_"
        elif dado.find(".") == -1:
            while len(dado) > 3:
                centena = dado[len(dado)-3:]
                dado = dado[:len(dado)-3]
                dadoFormatado = (centena + " " + dadoFormatado).strip()
            dadoFormatado = dado + " " + dadoFormatado
        else:
            dadoFormatado = dado.replace(".", ",") + " %"

        return dadoFormatado
