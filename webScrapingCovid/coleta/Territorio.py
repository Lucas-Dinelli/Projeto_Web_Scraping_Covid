class Territorio:

    nome = None
    casos = None
    mortes = None
    curados = None
    taxaDeLetalidade = None
    mortesPorMilhaoDeHabitantes = None

    def __init__(self, nome, casos, mortes, curados, taxaDeLetalidade, mortesPorMilhaoDeHabitantes):
        self.setNome(nome)
        self.setCasos(casos)
        self.setMortes(mortes)
        self.setCurados(curados)
        self.setTaxaDeLetalidade(taxaDeLetalidade)
        self.setMortesPorMilhaoDeHabitantes(mortesPorMilhaoDeHabitantes)


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
        if(nome == ""):
            nome = "Indonésia"

        self.nome = nome


    def setCasos(self, casos):
        try:
            casos = int(casos.replace(chr(160), ""))
        except:
            casos = 0

        self.casos = casos


    def setMortes(self, mortes):
        try:
            mortes = int(mortes.replace(chr(160), ""))
        except:
            mortes = 0

        self.mortes = mortes


    def setCurados(self, curados):
        try:
            curados = int(curados.replace(chr(160), ""))
        except:
            curados = 0

        self.curados = curados


    def setTaxaDeLetalidade(self, taxaDeLetalidade):
        try:
            taxaDeLetalidade = float(taxaDeLetalidade.replace(chr(160), "").replace("%", "").replace(",", "."))
        except:
            taxaDeLetalidade = 0

        self.taxaDeLetalidade = taxaDeLetalidade


    def setMortesPorMilhaoDeHabitantes(self, mortesPorMilhaoDeHabitantes):
        try:
            mortesPorMilhaoDeHabitantes = int(mortesPorMilhaoDeHabitantes.replace(chr(160), ""))
        except:
            mortesPorMilhaoDeHabitantes = 0

        self.mortesPorMilhaoDeHabitantes = mortesPorMilhaoDeHabitantes