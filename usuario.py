import json
class usuario:
    def __init__(self,):
        pass
    def carregardados(self,):
        try:
            with open("savegame.json", "r") as arquivo:
                self.save_data = json.load(arquivo)
            return self.save_data
        except FileExistsError:
            pass
    def adicionarpontos(self,save_data):
        save_data["usuario"]["clique"] += save_data["usuario"]["power"]
        try:
            with open("savegame.json", "w") as arquivo:
                json.dump(save_data, arquivo)
        except FileExistsError:
            pass
    def upgrade(self,save_data,index):
        save_data["usuario"]["power"] += save_data["store"]["addpower"][index]
        try:
            with open("savegame.json", "w") as arquivo:
                json.dump(save_data, arquivo)
        except FileExistsError:
            pass

        


        