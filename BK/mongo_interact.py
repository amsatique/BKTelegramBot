from pymongo import MongoClient
import datetime


class MongoInteract(object):
    def __init__(self):
        self.client = MongoClient("mongodb://172.17.0.2:27017")
        self.db = self.client.bktelegram
        self.codecountavailable = self.countBKCodeAvailable()

    def insertANewCode(self, inputbkcode):
        for i in inputbkcode:
            print("# - Add a code " + i)
            result = self.db.code.insert_one({
                "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                "usedcode": False,
                "bkcode": i
            })

    def updateUsedCode(self, bkcode):
        print("# - UpdateCode " + bkcode)
        result = self.db.code.update_one(
            {"bkcode": bkcode},
            {
                "$set": {"usedcode": True}
            }
        )

    def getACode(self):
        print("# - Get a unique code from mongo, set it to false")
        n = ""
        cursor = self.db.code.find({"usedcode": False}).limit(1)
        for doc in cursor:
            n = doc['bkcode']
        self.updateGeneratedNumber(1)
        self.updateUsedCode(n)
        return n

    # def findAllCode(self):
    #     print("# - Find all code ")
    #     # Link recup to send to another bot
    #     n = 0
    #     cursor = self.db.code.find({"usedcode": False})
    #     for doc in cursor:
    #         n = + 1
    #         print(doc)
    #     return n

    def countAllBurgerGenerated(self):
        print("# - Get how much burger has been generated")
        n = ""
        cursor = self.db.code.find({"featurename": "compteur"}).limit(1)
        for doc in cursor:
            n = doc['count_burger']
        return n

    def countBKCodeAvailable(self):
        print("# - Get unused bk code count on mongodb")
        a = self.db.code.count({"usedcode": False})
        return a

    def deleteUsedCode(self, usedCode):
        print("# - Delete code containing " + usedCode)
        result = self.db.code.delete_many({"bkcode": usedCode})
        return result

    def updateGeneratedNumber(self, inputGenerateBurgerNumber):
        print("# - Update Generated count by " + str(inputGenerateBurgerNumber))
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
                        {"count_burger": inputGenerateBurgerNumber},
                    "$currentDate":
                        {"lastburgertime": True}
                }
            )
