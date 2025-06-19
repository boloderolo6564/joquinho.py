import json
class rebirth:
    def __init__(self,):

        pass
    def verificarebirth(self,data_save):
        if(data_save["user"]["points"]>=data_save["Rebirth"]["require"]):
            return True
    def aumentarequire(self,data_save):
        data_save["Rebirth"]["require"] *= 1.5
        try:
            with open("database/savegame.json","w") as arquivo:
                json.dump(data_save, arquivo)
                return data_save
        except FileExistsError:
            pass  