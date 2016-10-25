from pymongo import MongoClient
import datetime

class MongoInteract(object):
    def __init__(self):
        self.client = MongoClient("mongodb://172.17.0.2:27017")
        self.db = self.client.bktelegram
        self.codecountavailable = self.countBKCodeAvailable()

    def insertANewCode(self, bkcode):
        result = self.db.code.insert_one({
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "usedcode": False,
            "bkcode": bkcode
        })


    def updateUsedCode(self, bkcode):
        result = self.db.code.update_one(
            {"bkcode": bkcode},
            {
                "$set": {"usedcode": True}
            }
        )


    def findAllCode(self):
        # Link recup to send to another bot
        n = 0
        cursor = self.db.code.find({"usedcode": False})
        for doc in cursor:
            n =+ 1
            print(doc)
        return n

    def countBKCodeAvailable(self):
        a = self.db.code.count({"usedcode": False})
        return a


    def deleteUsedCode(self, usedCode):
        result = self.db.code.delete_many({"bkcode": usedCode})
        return result


    def updateGeneratedNumber(self):
        a = self.db.code.count('count_burger')
        if a == 0:
            result = self.db.code.insert_one({
                "featurename": "compteur",
                "lastburgertime": "",
                "count_burger": 241
            })
        else:
            result = self.db.code.update_one(
                {"featurename": "compteur"},
                {
                    "$inc":
                        {"count_burger": 1},
                    "$currentDate":
                        {"lastburgertime": True}
                }
            )


# TODO : When 1 code is ok, if there is less than 5 code, go generate
# TODo : A generate code factory, just an int and bim, he create codes and add them to an array
# Todo : Code given : if 0 in db, generate, give, generate 5
# todo : Code given : if 1 in db, give it, remove it, generate

e = MongoInteract()
# insertANewCode("BK12348")
e.findAllCode()
print(e.countBKCodeAvailable())
e.updateGeneratedNumber()
e.updateUsedCode("BK12348")
print(e.countBKCodeAvailable())
# u = deleteUsedCode("BK1234")
# findAllCode()