from entities import *

def findStake(text):
    import re

    # find stake

    m = re.search("(?<=stake)\:?\s+(\d+)", text)
    if m and int(m.group(1)):
        return int(m.group(1))


    # find x/x format
    m = re.search("(\d\/\d+)", text)
    if m:
        stake = m.group(0).split("/")[0]
        if int(stake) < 11:
            return int(stake)
    return None

def findOdds(text):
    import re

    # find odd(s) or Cuota or value
    m = re.search("(?<=odd)s?\:?\s*(\d+[.,]\d+)", text)
    if m:
        return m.group(1)

    m = re.search("(?<=cuota)\:?\s*(\d+[.,]\d+)", text)
    if m:
        return m.group(1)

    m = re.search("(?<=value)\:?\s*(\d+[.,]\d+)", text)
    if m:
        return m.group(1)

    m = re.search("(?<=@)\s*(\d+[.,]\d+)", text)
    if m:
        return m.group(1)

    return None
    # # find x/x format
    # m = re.search("(\d.\d+)", text)
    # if m:
    #     stake = m.group(0).split("/")[0]
    #     if int(stake) < 11:
    #         return int(stake)

def findSport(text):
    for sport in sports:
        if sport in text:

            return sport
    return None
# def findBet(text):


def findEvent(text):
    import re

    m = re.search("(?<=match)s?\:?\s*([a-z()\s]+\s+-\s+[a-z()\s]+)", text)
    if m:
        return m.group(1)

    m = re.search("(?<=match)s?\:?\s*([a-z()\s]+\s+vs\s+[a-z()\s]+)", text)
    if m:
        return m.group(1)

    m = re.search("(?<=evento)s?\:?\s*([a-z()\s]+\s+-\s+[a-z()\s]+)", text)
    if m:
        return m.group(1)

    m = re.search("(?<=evento)\:?\s*([a-z()\s]+\s+vs\s+[a-z()\s]+)", text)
    if m:
        return m.group(1)

    m = re.search("([a-z()\s]+\s+vs\s+[a-z()\s]+)", text)
    if m:
        return m.group(0)

    m = re.search("([a-z()\s]+\s+-\s+[a-z()\s]+)", text)
    if m:
        if len(text.split("-")) ==2:
            return m.group(0)
        else:
            return None

    return None

def checkTrigger(myFunc, args, text):
    if args is None:
        return myFunc(text)
    return args

def extractInfo(text):
    listOfSentences = text.splitlines()
    sport = None
    odd = None
    stake = None
    event = None
    bet = None

    for line in listOfSentences:
        sport = checkTrigger(findSport, sport, line)
        odd = checkTrigger(findOdds, odd, line)
        stake = checkTrigger(findStake, stake, line)
        event = checkTrigger(findEvent, event, line)
    return sport, odd, stake, event


if __name__ == "__main__":
    import sys
    text = sys.argv[1]
    res = extractInfo(text.lower())
    # res = findEvent(text.lower())
    print res
    # print sports