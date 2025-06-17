import json
class store:
    def __init__(self):
        pass
    def buy(self,data_save,item):
        for index,(i) in enumerate(zip(data_save["store"]["itens"])):
            if(i[0] == item):
                if(data_save["usuario"]["clique"] >= data_save["store"]["price"][index]):
                    data_save["usuario"]["clique"] -= data_save["store"]["price"][index]
                    data_save["store"]["price"][index] *= 1.5
                    try:
                        with open("savegame.json", "w") as arquivo:
                            json.dump(data_save, arquivo)
                    except FileExistsError:
                        pass
                    return index
                else:
                    index = None
                    return index
