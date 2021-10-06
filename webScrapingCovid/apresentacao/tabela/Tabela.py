from tkinter import *
from tkinter import ttk


class Tabela:

    janela = None

    listaDeNomesDasColunas = ["Local", "Casos", "Mortes", "Taxa de letalidade", "Mortes p/ milhão"]

    controlador = None

    pesquisaAnterior = ""


    def __init__(self, controlador):
        self.controlador = controlador
        self.exibirJanela()


    def exibirJanela(self):
        self.janela = Tk()
        self.janela.title("Covid-19 - Tabela de dados")
        self.janela.geometry("1200x730")            # ...("Largura x Altura")
        self.janela.resizable(width=0, height=0)    # Impede que a tela seja redimensionada
        self.construirTabela()
        self.inserirPesquisa()
        self.inserirLabelDeInstrucao()
        self.janela.mainloop()


    def construirTabela(self):
        self.tree = ttk.Treeview(self.janela, selectmode="browse", column=(self.listaDeNomesDasColunas), show='headings')

        # <--------------- Parte referente a barra de rolagem da tabela ----------------------->
        scroll = ttk.Scrollbar(self.janela, orient="vertical", command=self.tree.yview)
        scroll.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=scroll.set)
        # <------------------------------------------------------------------------------------>

        style = ttk.Style()
        style.configure('Treeview', rowheight=70)

        self.inserirColunas(178)

        self.inserirLinhasDeDados(self.controlador.getListaDeTerritorios())

        self.tree.pack(side='left')     # Deixa a tabela contida na parte esquerda da janela


    def inserirColunas(self, largura):
        for i in range(len(self.listaDeNomesDasColunas)):
            self.tree.column(self.listaDeNomesDasColunas[i], width=largura, minwidth=largura, stretch=NO)
            self.tree.heading("#" + str(i+1), text=self.listaDeNomesDasColunas[i])


    def inserirLinhasDeDados(self, listaDeTerritorios):
        for territorio in listaDeTerritorios:
            nome = territorio.getNome()
            casos = self.controlador.formatarApresentacaoDeDado(territorio.getCasos())
            mortes = self.controlador.formatarApresentacaoDeDado(territorio.getMortes())
            taxaDeLetalidade = self.controlador.formatarApresentacaoDeDado(territorio.getTaxaDeLetalidade())
            mortesPorMilhaoDeHabitantes = self.controlador.formatarApresentacaoDeDado(territorio.getMortesPorMilhaoDeHabitantes())

            self.tree.insert("", END, values=(nome, casos, mortes, taxaDeLetalidade, mortesPorMilhaoDeHabitantes))

        self.tree.bind("<Double-1>", self.clique)       # Capta a ação de se clicar na tabela

    # Insere a caixa de texto que permite ao usuário filtrar territórios na tabela
    def inserirPesquisa(self):
        Label(self.janela, text="Pesquisar:", foreground="brown", font="-weight bold -size 10").place(x=938, y=200, width=80, height=25)
        self.caixaDeTextoPesquisa = Entry(self.janela, font="-weight bold -size 10")
        self.caixaDeTextoPesquisa.place(x=1028, y=200, width=110, height=25)
        self.caixaDeTextoPesquisa.bind("<KeyRelease>", self.filtrarTerritoriosCorrespondentes)

    # Insere uma label que informa a abertura do gráfico ao se clicar duas vezes no nome de uma coluna
    def inserirLabelDeInstrucao(self):
        Label(self.janela, text="_" * 100, foreground="brown", font="-weight bold -size 10").place(x=920, y=300, width=250, height=25)
        Label(self.janela, text="Clique duas vezes no nome de", foreground="brown", font="-weight bold -size 10").place(x=950, y=400, width=200, height=25)
        Label(self.janela, text="uma coluna para abrir o gráfico", foreground="brown", font="-weight bold -size 10").place(x=945, y=420, width=210, height=25)

    # Filtra na tabela os territórios que correspondem ao nome digitado na caixa de texto de pesquisa
    def filtrarTerritoriosCorrespondentes(self, event):
        pesquisaAtual = self.caixaDeTextoPesquisa.get()

        if pesquisaAtual == "" and pesquisaAtual != self.pesquisaAnterior:
            self.tree.delete(*self.tree.get_children())
            self.inserirLinhasDeDados(self.controlador.getListaDeTerritorios())

        elif pesquisaAtual != self.pesquisaAnterior:
            self.tree.delete(*self.tree.get_children())
            primeiraPosicaoCompativel = -1
            ultimaPosicaoCompativel = -1
            for i in range(len(self.controlador.getListaDeTerritoriosOrdenada())):
                territorio = self.controlador.getListaDeTerritoriosOrdenada()[i]
                if territorio.getNome()[:len(pesquisaAtual)].lower() == pesquisaAtual.lower():
                    if primeiraPosicaoCompativel == -1:
                        primeiraPosicaoCompativel = i
                        ultimaPosicaoCompativel = i
                    else:
                        ultimaPosicaoCompativel = i
                elif primeiraPosicaoCompativel != -1:
                    break
            self.inserirLinhasDeDados(self.controlador.getListaDeTerritoriosOrdenada()[primeiraPosicaoCompativel:ultimaPosicaoCompativel + 1])

        self.pesquisaAnterior = pesquisaAtual

    # Recebe o evento e garante a ação apenas se for detectado que o duplo clique na tabela foi no nome de uma das colunas
    def clique(self, event):
        regiao = self.tree.identify("region", event.x, event.y)
        numeroDaColunaClicada = int(self.tree.identify_column(event.x)[1:])
        if regiao == "heading" and numeroDaColunaClicada > 1:
            self.janela.destroy()
            self.controlador.iniciarGrafico(self.listaDeNomesDasColunas[numeroDaColunaClicada-1], self.listaDeNomesDasColunas[1:])
