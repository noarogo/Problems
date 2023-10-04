ret = []
k = 3

def powerset(s, k):
    if k == 1:
        for x in range(10):
            ret.append(s + str(x))
    elif k > 1:
        for x in range(10):
            ret.append(powerset(s + str(x), k-1))

def clean():
    A = []
    length = len(ret)
    for i in range(length):
        if ret[i] == None:
            continue
        elif ret[i][0] != '0':
            A.append(ret[i])
    return A

def wellordered(k):
    rem = []
    for num in ret:
        last = int(num[0])
        for i in range(1,k):
            if int(num[i]) <= last:
                rem.append(num)
                break
            else:
                last = int(num[i])
    for r in rem:
        ret.remove(r)                

powerset("",k)
ret = clean()
wellordered(k)
print(ret)