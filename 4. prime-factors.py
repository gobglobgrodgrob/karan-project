
y = []
def findfact(x):
    for i in range(0, x/2):
        if x%i == 0:
            y.append(i)

def findpri(x):
    for i in range(2, x/2):
        if x%i != 0:
            break
        else:
            return True

def findprifact(x):
    findpri(x)
    for i in y:
        if findpri(i) == False:
            y.remove(i)
