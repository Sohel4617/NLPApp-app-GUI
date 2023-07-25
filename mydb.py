import json
class Database:
    def add_data(self,name,Email,Password):

        with open('db.json','r') as rf:
            database = json.load(rf)

        if Email in database:
            return 0
        else:
            database[Email] = [name,Password]
            with open('db.json','w') as wf:
                json.dump(database,wf)
            return 1

    def search_data(self,Email,Password):

        with open('db.json','r') as rf:
            database = json.load(rf)
            if Email in database:
                if database[Email][1] == Password:
                    return 1
                else:
                    return 0
            else:
                return 0



