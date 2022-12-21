import numpy as np

def file_read(file_name):
    file1=open(file_name,"r")
    data_matrix=file1.read()
    data_matrix=data_matrix.split("\n")
    return_data_matrix = []
    for row in data_matrix:
        return_data_matrix.append(row.rstrip().split(" "))
    return return_data_matrix


def dfs(matrix,history=None,curr=[0,0],veins=[],level=0):
    if history == None:
        history = [[0 for a in range(len(matrix[b]))] for b in range(len(matrix))]
        history[0][0]=1

    new_finds=[]
    y=curr[0]
    x=curr[1]


    bias=[[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]

    for y_bias,x_bias in bias:
        y_curr=y+y_bias
        if y_curr<0 or y_curr>=len(matrix):
            continue
        x_curr=x+x_bias
        if x_bias==0 and y_bias==0:
            continue
        if x_curr<0 or x_curr>=len(matrix[y]):
            continue
        if history[y_curr][x_curr] != 0:
            continue
        history[y_curr][x_curr] = 1
        print(level,y_curr,x_curr,"\n",np.array(history))
        returned1,returned2,history = dfs(matrix,history,[y_curr,x_curr],level=level+1)
        if matrix[y_curr][x_curr]=="Y":
            sum=0
            while returned1[0]==0:
                returned1.pop(0)
            while returned1[0]!=0:
                sum+=returned1
            new_finds.append(returned1)
        else:
            new_finds.append(0)
        new_finds.append(returned1)
        veins+=returned2
    
    if level==0:
        print(veins)
        return max(veins)
    return new_finds,veins,history



def main():
    data1=file_read("input_1.1.txt")
    data1=dfs(data1)
    print(data1)
main()