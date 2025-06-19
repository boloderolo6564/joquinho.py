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
        if save_data["usuario"]["rebirth"] > 0:
            save_data["usuario"]["pontos"] += (save_data["usuario"]["power"] * (save_data["Rebirth"]["multiplicador"]*save_data["usuario"]["rebirth"]))
        else:
            save_data["usuario"]["pontos"] += save_data["usuario"]["power"]
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
    def rebirthupgrade(self,save_data):
        rebirth = save_data["usuario"]["rebirth"]
        print("tentando alterar dados")
        try:
            with open("./reset/database+store.json", "r") as arquivo:
                novo_save = json.load(arquivo)
                save_data = novo_save
                save_data["usuario"]["rebirth"] += rebirth + 1
                print("dados alterados")
                return save_data
        except:
            pass

    

        


        