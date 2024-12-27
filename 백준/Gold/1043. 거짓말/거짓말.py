import sys

def solution():
    peoples, parties = map(int, sys.stdin.readline().split())
    knowledge = set(list(map(int, sys.stdin.readline().split()))[1:])
    
    partyInfo = []
    for _ in range(parties):
        partyInfo.append(list(map(int, sys.stdin.readline().split()))[1:])

    partySet = set(range(len(partyInfo)))
    sayTruth = set()
    beforeLength = -1
    while beforeLength != len(sayTruth):
        beforeLength = len(sayTruth)
        for i in partySet:
            if SomeoneKnowTruth(partyInfo[i], knowledge):
                sayTruth.add(i)
                for man in partyInfo[i]:
                    knowledge.add(man)
                #partySet.discard(i)

    return len(partyInfo) - len(sayTruth)

def SomeoneKnowTruth(info, knowledge):
    for man in info:
        if man in knowledge:
            return True
    return False

print(solution())