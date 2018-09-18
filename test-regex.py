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
        if int(stake) < 11 :
            return int(stake)

    # m = re.search("\d+", text)
    # if m and int(m.group(0)):
    #     return int(m.group(0))

if __name__ == "__main__":
    import sys
    text = sys.argv[1]
    # res = findStake(text.lower())
    # print res
    print sports