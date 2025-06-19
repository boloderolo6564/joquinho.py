import tkinter as tk
from tkinter import PhotoImage
from objects.usuario import usuario
from objects.interface import interface
from objects.store import store
from objects.rebirth import rebirth

if __name__ == "__main__":
    root = tk.Tk()
    root.title("joquinho.py")
    root.geometry("600x400")
    icon = PhotoImage(file="assets/icone/icone.png")  
    root.iconphoto(False, icon)
    root.configure(bg="#1C1616")
    root.resizable(False, False)

    jogador = usuario()
    data_save = jogador.carregardados()
    loja = store()
    Rebirth = rebirth()
    Interface = interface(root, jogador, loja,data_save,rebirth)

    root.mainloop()

