# -*- coding: utf-8 -*-
from entities import *
import unidecode
teams = []

def findStake(text):
    import re

    # find stake
    m = re.search("(?<=stake)\:?\s+(\d+)", text)
    if m and int(m.group(1)):
        z = re.sub("(stake)\:?\s+(\d+)", '',text)
        return int(m.group(1)), z.strip()


    # find x/x format
    m = re.search("(\d\/\d+)", text)
    if m:
        stake = m.group(0).split("/")[0]
        if int(stake) < 11:
            z = re.sub("(\d\/\d+)", '',text)
            return int(stake), z.strip()
    return None, text

def findOdds(text):
    import re

    # find odd(s) or Cuota or value
    m = re.search("(?<=odd)s?\:?\s*(\d+[.,]\d+)", text)
    if m:
        z = re.sub("(odd)s?\:?\s*(\d+[.,]\d+)", '',text)
        return m.group(1), z.strip()

    m = re.search("(?<=cuota)\:?\s*(\d+[.,]\d+)", text)
    if m:
        z = re.sub("(cuota)\:?\s*(\d+[.,]\d+)", '',text)
        return m.group(1), z.strip()

    m = re.search("(?<=value)\:?\s*(\d+[.,]\d+)", text)
    if m:
        z = re.sub("(value)\:?\s*(\d+[.,]\d+)", '',text)
        return m.group(1), z.strip()

    m = re.search("(?<=@)\s*(\d+[.,]\d+)", text)
    if m:
        z = re.sub("(@)\s*(\d+[.,]\d+)", '',text)
        return m.group(1), z.strip()

    return None, text
    # # find x/x format
    # m = re.search("(\d.\d+)", text)
    # if m:
    #     stake = m.group(0).split("/")[0]
    #     if int(stake) < 11:
    #         return int(stake)

def findSport(text):
    for sport in sports:
        if sport in text:

            return sport, text.strip()
    return None, text
# def findBet(text):


def findEvent(text):
    import re
    expressionHalfDash = "[a-z()\s]+(u[1-9]*)?[a-z()\s]+"
    expressionDash = '({0}\s+-\s+{0})'.format(expressionHalfDash)
    expressionVersus = "([a-z()\s]+\s+vs\s+[a-z()\s]+)"
    m = re.search("(?<=match)s?\:?\s*" + expressionDash, text)
    if m:
        z = re.sub("(match)s?\:?\s*" + expressionDash, '',text)
        return m.group(1), z.strip()

    m = re.search("(?<=match)s?\:?\s*" + expressionVersus, text)
    if m:
        z = re.sub("(match)s?\:?\s*" + expressionVersus, '',text)
        return m.group(1), z.strip()

    m = re.search("(?<=evento)s?\:?\s*" + expressionDash, text)
    if m:
        z = re.sub("eventos?\:?\s*" + expressionDash, '',text)
        return m.group(1), z.strip()

    m = re.search("(?<=evento)\:?\s*" + expressionVersus, text)
    if m:
        z = re.sub("evento\:?\s*" + expressionVersus, '',text)
        return m.group(1), z.strip()

    m = re.search(expressionVersus, text)
    if m:
        z = re.sub(expressionVersus, '',text)
        return m.group(0), z.strip()

    m = re.search(expressionDash, text)
    if m:
        if len(text.split("-")) ==2:
            z = re.sub("([a-z()\s]+\s+-\s+[a-z()\s]+)",'', text)
            return m.group(0), z.strip()
        else:
            return None, text

    m = re.search("(over\s+-?[0-9]+.?[0-9]*)", text)
    if m:
        z = re.sub("(over\s+-?[0-9]+.?[0-9]*)", '',text)
        return m.group(0), z.strip()

    return None, text

def findBet(text):
    import re

    m = re.search("(?<=pick)\s*\:\s*(.*)", text)
    if m:
        z = re.sub("(pick)\s*\:\s*(.*)",'', text)
        return m.group(1), z.strip()

    m = re.search("(?<=pronostico)\:\s*(.*)", text)
    if m:
        z = re.sub("(pronostico)\:\s*(.*)",'', text)
        return m.group(1), z.strip()

    m = re.search("(over\s*-?[0-9]+.?[0-9]*)", text)
    if m:
        z = re.sub("(over\s*-?[0-9]+.?[0-9]*)",'', text)
        return m.group(0), z.strip()

    m = re.search("(under\s*-?[0-9]+.?[0-9]*)", text)
    if m:
        z = re.sub("(under\s*-?[0-9]+.?[0-9]*)",'', text)
        return m.group(0), z.strip()

    m = re.search("(home\s*\+?[0-9]+.?[0-9]*)", text)
    if m:
        z = re.sub("(home\s*\+?[0-9]+.?[0-9]*)", '', text)
        return m.group(0), z.strip()
    m = re.search("(away\s*\+?[0-9]+.?[0-9]*)", text)

    if m:
        z = re.sub("(away\s*\+?[0-9]+.?[0-9]*)", '', text)
        return m.group(0), z.strip()


    m = re.search("[a-z]+\s(win(s?)\s*)", text)
    if m:
        # z = re.sub("(under\s*-?[0-9]+.?[0-9]*)", '', text)
        return m.group(0), ''


    return None, text



def checkTrigger(myFunc, args, text):
    if args is None:
        return myFunc(text)
    return args, text

def extractInfo(processedText):
    import re
    listOfSentences = prerpocess(processedText.lower().splitlines())
    sport = None
    odd = None
    stake = None
    event = None
    bet = None
    auxListSport = []
    auxListOdd = []
    auxListStake = []
    auxListSEvent = []

    for line in listOfSentences:
        sport, text = checkTrigger(findSport, sport, line)
        if sport is None:
            auxListSport.append(line)
        else:
            newLine = re.sub(sport, '', line)
            if newLine:
                auxListSport.append(newLine)

    for line in auxListSport:
        odd, text = checkTrigger(findOdds, odd, line)
        if text:
            auxListOdd.append(text)

    for line in auxListOdd:
        stake, text = checkTrigger(findStake, stake, line)
        if text:
            auxListStake.append(text)

    for line in auxListStake:
        event, text = checkTrigger(findEvent, event, line)
        if text:
            auxListSEvent.append(text)
    if event:
        teams.extend(event.split(' '))

    if len(auxListSEvent) == 1:
        bet = auxListSEvent[0]
    for line in auxListSEvent:
        bet, text = checkTrigger(findBet, bet, line)
        # auxListBet.append(text)

    print(sport, odd, stake, event, bet)
    if odd is None:
        odd = 1.00
    if sport and odd and stake and event and bet:
        return sport, odd, stake, event, bet
    else:
        return None


def prerpocess(text):
    import re
    import string
    printable = set(string.printable)
    lines = []
    for line in text:
        newLine = re.sub("(pinnacle)", '',line)
        newLine = re.sub("(bet365)", '', newLine)
        newLine = re.sub("(maps handicap)", '', newLine)
        newLine = re.sub("(maps handicap)", '', newLine)
        newLine = newLine.strip()
        if newLine:
            newLine = unidecode.unidecode(newLine)
            lines.append(newLine)
    return lines

if __name__ == "__main__":
    import sys
    text = sys.argv[1]
    res = extractInfo(text)
    print(res)