import tkinter as tk
from usuario import usuario
from interface import interface
from store import store
from rebirth import rebirth

if __name__ == "__main__":
    root = tk.Tk()
    root.title("joquinho.py")
    root.geometry("600x400")
    root.configure(bg="#1C1616")
    root.resizable(False, False)

    jogador = usuario()
    data_save = jogador.carregardados()
    loja = store()
    Rebirth = rebirth()
    Interface = interface(root, jogador, loja,data_save,rebirth)

    root.mainloop()

