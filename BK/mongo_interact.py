from pymongo import MongoClient
import datetime
# URL Mongo on Docker
client = MongoClient("mongodb://172.17.0.2:27017")
db = client.bktelegram



def insertANewCode(bkcode):
    result = db.code.insert_one({
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        "usedcode": False,
        "bkcode": bkcode
    })


def updateUsedCode(bkcode):
    result = db.code.update_one(
        {"bkcode": bkcode},
        {
            "$set": {"usedcode": True}
        }
    )


def findAllCode():
    # Link recup to send to another bot
    n = 0
    cursor = db.code.find({"usedcode": False})
    for doc in cursor:
        n =+ 1
        print(doc)
    return n


def countBKCodeAvailable():
    a = db.code.count({"usedcode": False})
    return a


def deleteUsedCode(usedCode):
    result = db.code.delete_many({"bkcode": usedCode})
    return result


def updateGeneratedNumber():
    a = db.code.count('count_burger')
    if a == 0:
        result = db.code.insert_one({
            "featurename": "compteur",
            "lastburgertime": "",
            "count_burger": 241
        })
    else:
        result = db.code.update_one(
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
# Todo : Code given : if  0 in db, generate, give, generate 5
# todo : Code given : if 1 in db, give it, remove it, generate


# insertANewCode("BK12348")
findAllCode()
print(countBKCodeAvailable())
updateGeneratedNumber()
updateUsedCode("BK12348")
print(countBKCodeAvailable())
# u = deleteUsedCode("BK1234")
# findAllCode()