class Territorio:

    nome = None
    casos = None
    mortes = None
    curados = None
    taxaDeLetalidade = None
    mortesPorMilhaoDeHabitantes = None

    def __init__(self, nome, casos, mortes, curados, numeroTotalDaPopulacao):
        self.setNome(nome)
        self.setCasos(casos)
        self.setMortes(mortes)
        self.setCurados(curados)
        self.setTaxaDeLetalidade()
        self.setMortesPorMilhaoDeHabitantes(numeroTotalDaPopulacao)


    # Getters...

    def getNome(self):
        return self.nome

    def getCasos(self):
        return self.casos

    def getMortes(self):
        return self.mortes

    def getCurados(self):
        return self.curados

    def getTaxaDeLetalidade(self):
        return self.taxaDeLetalidade

    def getMortesPorMilhaoDeHabitantes(self):
        return self.mortesPorMilhaoDeHabitantes


    # ... Setters

    def setNome(self, nome):
        self.nome = nome


    def setCasos(self, casos):
        try:
            casos = int(self.ajustarValorString(casos))
        except:
            casos = 0

        self.casos = casos


    def setMortes(self, mortes):
        try:
            mortes = int(self.ajustarValorString(mortes))
        except:
            mortes = 0

        self.mortes = mortes


    def setCurados(self, curados):
        try:
            curados = int(self.ajustarValorString(curados))
        except:
            curados = 0

        self.curados = curados


    def setTaxaDeLetalidade(self):
        if self.getCasos() > 0:
            self.taxaDeLetalidade = (self.getMortes() / self.getCasos()) * 100
        else:
            self.taxaDeLetalidade = 0


    def setMortesPorMilhaoDeHabitantes(self, numeroTotalDaPopulacao):
        try:
            numeroTotalDaPopulacao = int(self.ajustarValorString(numeroTotalDaPopulacao))
            mortesPorMilhaoDeHabitantes = (self.getMortes() / numeroTotalDaPopulacao) * 1000000     # Fórmula
        except:
            mortesPorMilhaoDeHabitantes = 0

        self.mortesPorMilhaoDeHabitantes = round(mortesPorMilhaoDeHabitantes)   # Arredonda


    # Retira os caracteres não numéricos caso existam
    def ajustarValorString(self, valorString):
        novoValorString = valorString.replace(",", "")
        return novoValorString
