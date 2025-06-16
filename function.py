import json
from tkinter import*
def clicado(save_data,power):
    save_data["usuario"]["clique"] += power
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
def compra(save_data,item):
    for index,(i) in enumerate(zip(save_data["store"]["itens"])):
        
        if(i[0] == item):
            price = save_data["store"]["price"][0]
            if(price > save_data["usuario"]["clique"]):
                return
            else:
                save_data["usuario"]["clique"] -= price

                try:
                    with open("savegame.json", "w") as arquivo:
                        json.dump(save_data, arquivo)
                except FileExistsError:
                    pass
                increasepower(save_data,item)
        else:
            print("deu errado")
def increasepower(save_data,item):
    match item:
        case "simple click":
            save_data["usuario"]["power"] +=1
        case "click+":
            save_data["usuario"]["power"] +=2
    try:
        with open("savegame.json", "w") as arquivo:
            json.dump(save_data, arquivo)
    except FileExistsError:
        pass