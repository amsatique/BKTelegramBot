from werkzeug.wrappers import Request, Response
import roburger
import mongo_interact


# Emojis and cute stuff
hamburger = u'\U0001F354'
thumbsupsign = u'\U0001F44D'
clappinghandsign = u'\U0001F44D'


def haveAGoodMealString():
    return "\n    " + thumbsupsign + "    Bon appetit!   " + hamburger


def burger_generation():
    e = mongo_interact.MongoInteract()
    q = roburger
    g = e.codecountavailable
    if 0 < g < 5:
        print('g14')
        r = e.getACode()
        u = q.burgermain(2)
        e.insertANewCode(u)
        return r + haveAGoodMealString()
    elif g > 4:
        print('g5or+')
        r = e.getACode()
        return r + haveAGoodMealString()
    else:
        e.updateGeneratedNumber(1)
        print("Else? ")
        return q.burgermain(1)[0] + haveAGoodMealString()


@Request.application
def application():
    return Response(burger_generation())


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 4000, application)