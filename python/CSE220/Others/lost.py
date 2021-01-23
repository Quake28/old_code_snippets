from typing import Dict, List

def lost(wood:Dict[int,List[int]]) -> float:
    curr_weight=[0 for a in range(len(wood))]
    next_weight=curr_weight[:]
    curr_weight[0]=1
    time=0
    end=len(wood)-1
    for a in range(1,1000+1):
        for b in range(len(curr_weight)):
            if curr_weight[b]!=0:
                for c in wood[b]:
                    next_weight[c]+=curr_weight[b]/len(wood[b])
            time+=a*next_weight[-1]
            next_weight[-1]=0
        curr_weight=next_weight[:]
        next_weight=[0 for d in range(len(next_weight))]
    return round(time,6)

print(lost({0:[1,2],1:[0,2],2:[0,1]}))
print(lost({0:[1,2],1:[0,3],2:[0,4],3:[1,4],4:[2,3]}))
print(lost({0:[1,2,3],1:[0,2],2:[0,1,4],3:[0,4],4:[2,3]}))
print(lost({0:[1,2,3],1:[0,3],2:[0],3:[0,1]}))