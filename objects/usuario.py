import json
class usuario:
    def __init__(self,):
        pass
    def carregardados(self,):
        try:
            with open("database/savegame.json", "r") as arquivo:
                self.save_data = json.load(arquivo)
            return self.save_data
        except FileExistsError:
            pass
    def adicionarpontos(self,save_data):
        if save_data["user"]["rebirth"] > 0:
            save_data["user"]["points"] += (save_data["user"]["power"] * (save_data["Rebirth"]["multiply"]*save_data["user"]["rebirth"]))
        else:
            save_data["user"]["points"] += save_data["user"]["power"]
        try:
            with open("database/savegame.json", "w") as arquivo:
                json.dump(save_data, arquivo)
        except FileExistsError:
            pass
    def upgrade(self,save_data,index):
        save_data["user"]["power"] += save_data["store"]["addpower"][index]
        try:
            with open("database/savegame.json", "w") as arquivo:
                json.dump(save_data, arquivo)
        except FileExistsError:
            pass
    def rebirthupgrade(self,save_data):
        rebirth = save_data["user"]["rebirth"]
        rebirth_require= save_data["Rebirth"]["require"]
        print("attempting to modify the data")
        try:
            with open("database/database+store.json", "r") as arquivo:
                novo_save = json.load(arquivo)
                save_data = novo_save
                save_data["user"]["rebirth"] += rebirth + 1
                save_data["Rebirth"]["require"] = rebirth_require
                print("data has been updated")
                return save_data
        except:
            pass

    

        


        