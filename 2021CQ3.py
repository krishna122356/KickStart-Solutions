from collections import Counter

t = int(input())
x = int(input())

# Gets us the best answer for a given ratio. There are only 4 ratios in the question, but the below code will work for any given ratio. Here ratio is the ratio between the Win and Tie points.
def fn(ratio):
    # d[(x,y,z)] contains the best possible score we can achieve for a tuple of x,y,z. ans[(x,y,z)] contains the string which does the same.
    d = Counter()
    c = [[1,0,0],[0,1,0],[0,0,1]]
    d[(1, 0, 0)] = (1 + ratio) / 3
    d[(0, 1, 0)] = (1 + ratio) / 3
    d[(0, 0, 1)] = (1 + ratio) / 3
    f=0
    ans={}
    ans[(1, 0, 0)] = "P"
    ans[(0, 1, 0)] = "R"
    ans[(0, 0, 1)] = "S"
    for i in range(62):
        ans[(-1,i,61-i)]=""
    ret=""
    
    # A simple bottom up dynamic Programming approach solves this question. It has been needlessly complicated for some reason, with parametes such as X being useless.
    # Each iteration of the while loop increments the number of games played thus far by 1.
    while (True):
        e = {}
        if (c == []):
            break
        for i in c:
            x, y, z = i[0], i[1], i[2]
            if(x+y+z==61):
                if(d[(x-1,y,z)]>f):
                    f=d[(x-1,y,z)]
                    ret = ans[(x-1,y,z)]
                continue
            if ((x - 1, y, z) in d)and(z / (x + y + z-1) + ratio * y / (x + y + z-1) + d[(x - 1, y, z)]>d[(x,y,z)]):
                d[(x, y, z)] = max(z / (x + y + z-1) + ratio * y / (x + y + z-1) + d[(x - 1, y, z)], d[(x, y, z)])
                ans[(x,y,z)]=ans[(x-1,y,z)]+"P"
            if ((x, y - 1, z) in d)and(x / (x + y + z-1) + ratio * z / (x + y + z-1) + d[(x, y - 1, z)]> d[(x, y, z)]):
                d[(x, y, z)] = max(x / (x + y + z-1) + ratio * z / (x + y + z-1) + d[(x, y - 1, z)], d[(x, y, z)])
                ans[(x, y, z)] = ans[(x, y-1, z)] + "R"
            if ((x, y, z - 1) in d)and(y / (x + y + z-1) + ratio * x / (x + y + z-1) + d[(x, y, z - 1)]> d[(x, y, z)]):
                d[(x, y, z)] = max(y / (x + y + z-1) + ratio * x / (x + y + z-1) + d[(x, y, z - 1)], d[(x, y, z)])
                ans[(x, y, z)] = ans[(x, y, z-1)] + "S"
            e[(x + 1, y, z)] = 1
            e[(x, y+1, z)] = 1
            e[(x, y, z+1)] = 1
        c=[]
        for i in e:
            c.append(list(i))
    return ret


d1 = fn(0)
d2 = fn(0.1)
d3 = fn(0.5)
d4 = fn(1)
# Effectively, the answer is only some permutation of a set of 4 possible output strings. 
for i in range(t):
    w, e = map(int, input().split())
    d=e/w
    if(d==0):
        print("Case #",i+1,": ",d1,sep="")
    elif(d==0.1):
        print("Case #",i+1,": ",d2,sep="")
    elif (d == 0.5):
        print("Case #", i + 1, ": ", d3,sep="")
    else:
        print("Case #", i + 1, ": ", d4,sep="")
