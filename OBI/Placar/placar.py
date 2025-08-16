P = list(map(int, input().split()))
p1 = P.pop(0)
mp = P  
C = list(map(int, input().split()))
c2 = C.pop(0)
mc = C  
p = 0
c = 0
print(p, c)
while mp or mc:
    if not mp:
        c += 1
        mc.pop(0)
    elif not mc:
        p += 1
        mp.pop(0)
    elif mp[0] < mc[0]:
        p += 1
        mp.pop(0)
    else:
        c += 1
        mc.pop(0)
    print(p, c)