#KeyExpansion and AddRoundKey Module
def shift_l(lis):
    lis = lis[-1:]+lis[:-1]
    return lis

def numer(arg):
    ret = []
    for item in arg:
        ret.append(ord(item))
    return ret

def tempo(keyarg, round):
    pass

def keyexpand(key):
    WordSpace= []
    x = 0
    for i in range(4):
        WordSpace.append(numer(key[x:x+4]))
        x += 4
    print(WordSpace)

keyexpand("YukariReimuSuika")
