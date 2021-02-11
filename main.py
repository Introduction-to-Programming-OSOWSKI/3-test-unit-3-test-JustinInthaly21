def countB(w):
    r = 0
    for i in w:
        if i == 'b':
            r = r + 1
    return r

def removeLast(w, x):
    e = 0
    for i in w:
        e = e + 1
    return e - x
    



def sumBetweenOdd(x, y):
    
    q = 0
    for i in range(x + 1, y):
        if(i % 2 != 0):
            print("{0}".format(i))
            q = q + i
    return q

def firstLast(w):
    if(w[0] == w[-1]):
        return True
    else:
        return False
    
print(sumBetweenOdd(0, 10))