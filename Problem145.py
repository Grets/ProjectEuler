
def isReversable(x):
    x = str(x+int(str(x)[::-1]))
    for c in x:
        if int(c) % 2 == 0:
            return False
    return True

print(isReversable(63))
