t=int(input())
import random
d={}

# We need to implement seeds along with our solution to minimize the chances of unfortunate collisions.
def hashingseed(a,b,seed):
    if((a,b,seed) in d):
        return d[(a,b,seed)]
    else:
        d[(a, b, seed)] = random.randint(1, 10 ** 9 + 7)
        return d[(a, b, seed)]

# Evaluates the expression, as a calculator would. It is balanced well by parenthesis, making our job easier.
def eval(s,seed):
    if(s.isdigit()):
        return int(s)
    c=""
    bc=0
    for i in range(1,len(s)-1):
        if(s[i] not in ["+","*","#"]):
            c+=s[i]
            if(s[i]=="("):
                bc+=1
            elif(s[i]==")"):
                bc-=1
        elif(bc==0):
            if(s[i]=="+"):
                return (eval(c,seed)+eval(s[i+1:-1],seed))
            if(s[i]=="*"):
                return (eval(c,seed)*eval(s[i+1:-1],seed))
            if(s[i]=="#"):
                return (hashingseed(eval(c,seed),eval(s[i+1:-1],seed),seed))
        else:
            c+=s[i]

for __ in range(t):
    N=int(input())
    e={}
    co=1
    l=[]
    seeds=[]
    # We use 10 different seeds here, to minimize collisions. One seed would like to collisions, while a hundred would slow down the program too much.
    for j in range(10):
        seeds.append(random.randint(1,10**9+7))
    for i in range(N):
        s=input()
        tip=[]
        for j in seeds:
            tip.append(eval(s,j))
        tip=tuple(tip)
        if tip in e:
            l.append(e[tip])
        else:
            e[tip]=co
            co+=1
            l.append(e[tip])
    d={}
    print("Case #",__+1,": ",end="",sep="")
    print(*l,sep=" ")
