import tkinter as tk
from usuario import usuario
from interface import interface
from store import store

if __name__ == "__main__":
    root = tk.Tk()
    root.title("joquinho.py")
    root.geometry("600x400")
    root.configure(bg="#1C1616")
    root.resizable(False, False)

    jogador = usuario()
    data_save = jogador.carregardados()
    loja = store()
    Interface = interface(root, jogador, loja,data_save)

    root.mainloop()

