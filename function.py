import json
from tkinter import*
def clicado(save_data):
    save_data["usuario"]["clique"] +=1
    try:
        with open("savegame.json", "w") as arquivo:
            json.dump(save_data, arquivo)
    except FileExistsError:
        pass
def ler():
    try:
        with open("savegame.json", "r") as arquivo:
            save_data = json.load(arquivo)
        return save_data
    except FileExistsError:
        pass

def escrever(save_data):
    try:
        with open("savegame.json", "w") as arquivo:
            json.dump(save_data, arquivo)
    except FileExistsError:
        pass