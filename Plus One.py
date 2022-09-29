

def add(a,b,c):
    x = str(a)+str(b)+str(c)
    res = x
    add1 = int(res) + 1
    m = str(add1)
    m2 = [ int(i) for i in m]
    return m2
    



x1 = add(1,2,5)
print(x1)