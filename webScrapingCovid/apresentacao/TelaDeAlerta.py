import tkinter
from tkinter import messagebox

class TelaDeAlerta:
    def __init__(self, titulo, mensagem):
        root = tkinter.Tk()
        root.withdraw()

        # Caixa de Mensagem
        messagebox.showwarning(titulo, mensagem)