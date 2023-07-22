s=input()
n=sorted(list(set (filter(lambda x: x.isdigit(),s))),reverse=True)
even = list(filter(lambda x: int(x)%2==0,n))
if len(even)==0:
    print(-1)
else:
    if int(n[-1])%2==0:
        print("".join(n))
    else:
        n.remove(even[-1])
        n.append(even[-1])
        print("".join(n))