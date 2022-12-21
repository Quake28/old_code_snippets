import random

class Node:
    count=1
    comparison=0
    def __init__(self,prev=None,value=None,modifier=1):
        self.count=Node.count
        Node.count+=1
        self.next=[]
        self.value=value
        self.modifier=modifier
        self.prev=prev
    def __repr__(self):
        return str(self.count)

def tree(root, set, depth, choice, modifier=-1):
    set_size=choice**(depth-1)
    for a in range(choice):
        #print(depth, set, modifier)
        if depth==1:
            new_node=Node(prev=root, value=set[a],modifier=modifier)
            root.next.append(new_node)
            print(depth,new_node.count,new_node.value,new_node.next,new_node.prev)
        else:
            new_node=Node(prev=root,modifier=modifier)
            root.next.append(new_node)
            tree(new_node, set[a*set_size:(a+1)*set_size], depth-1, choice, modifier*-1)

def minimax(root,alpha=-float("inf"),beta=float("inf")):
    if len(root.next)==0:
        Node.comparison+=1
        return root.value

    else:
        count=0
        while count<len(root.next) and alpha<beta:
            val=minimax(root.next[count],alpha,beta)
            #print(val, alpha, beta)
            if root.modifier==1:
                if val>alpha:
                    alpha=val
            else:
                if val<beta:
                    beta=val
            count+=1
        if root.modifier==1:
            return alpha
        else:
            return beta
        
def printer(root,depth=0):
    print(depth, root.value, root.next)
    if len(root.next)==0:
        print(depth, root.count, root.value, root.next,root.prev)
    for a in root.next:
        printer(a,depth+1)
    

def main():
    id=input("Enter your student id: ")
    att_hp_range=input("Minimum and Maximum value for the range of negative HP: ")
    turn_count=int(id[0])
    def_hp=int(id[-2:][::-1])
    #print(def_hp)
    bullet_count=int(id[2])
    att_hp_range=att_hp_range.rstrip().split()
    att_hp_range=[int(a) for a in att_hp_range]
    #print(att_hp_range)
    depth=turn_count*2
    print("1. Depth and Branches ratio is",str(depth)+":"+str(bullet_count))
    print("2. Terminal States (leaf node values) are ",end="")
    state_array=[random.randint(att_hp_range[0],att_hp_range[1]) for a in range(bullet_count**depth)]
    #state_array = [19,22,9,2,26,16,16,27,16]
    #state_array = [18,13,5,12,10,5,13,7,17,8,6,8,5,11,13,18]
    for a in state_array[:-1]:
        print(str(a)+",",end="")
    print(state_array[-1], end=".\n")
    #print(state_array)

    root=Node()
    tree(root, state_array, depth, bullet_count)

    #printer(root)

    damage_dealt=minimax(root)
    comparison_count=Node.comparison
    print("3. Left life(HP) of the defender after maximum damage caused by the attacker is",def_hp-damage_dealt)
    print("4. After Alpha-Beta Pruning Leaf Node Comparisons",comparison_count)
    #17301106
    #1 30
    #
    #2:3
    #44
    #7

    #20201003
    #5 20
    #
    #4:2
    #22
    #13

    #All above values are proper tested results

main()