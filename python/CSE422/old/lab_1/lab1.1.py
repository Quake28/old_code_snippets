def file_read(file_name):
    file1=open(file_name,"r")
    data_matrix=file1.read()
    data_matrix=data_matrix.split("\n")
    return_data_matrix = []
    for row in data_matrix:
        return_data_matrix.append(row.rstrip().split(" "))
    return return_data_matrix

def groups(matrix,curr=[0,0],history=[[0,0]]):
    # Defining each level of search (searching for surrounding values of one node that has not been looked at before)
    new_finds=0
    y=curr[0]
    x=curr[1]
    for y_bias in range(-1,2):
        y_curr=y+y_bias
        if y_curr<0 or y_curr>=len(matrix):
            continue
        for x_bias in range(-1,2):
            x_curr=x+x_bias
            if x_curr<0 or x_curr>=len(matrix[y]):
                continue
            elif matrix[y_curr][x_curr]=="Y":
                if [y_curr,x_curr] not in history:
                    history.append([y_curr,x_curr])
                    new_finds+=1
            else:
                print(y_curr,x_curr)
            #print(matrix[y_curr][x_curr],y_curr,x_curr)
    return new_finds, history
    
def bfs_search(matrix,history=None,level=[[0,0]],vein=0):
    # traversing through matrix at a preliminary stage
    #for y in range(start[0],len(matrix)-1):
    #    for x in range(start[1],len(matrix[y])-1):
    # for curr in history:
    #     grouped_data = groups(matrix=matrix, curr=curr, history=history)
    #     new_finds=grouped_data[0]
    #     if new_finds==0:
    #         # traversing through matrix at a preliminary stage
    #         for y in range(curr[0],len(matrix)-1):
    #             for x in range(curr[1],len(matrix[y])-1):
    #                 #print(y,x)
    #                 grouped_data = groups(matrix, curr=[y,x], history=history)
    #                 new_finds=grouped_data[0]
    #     print(new_finds)
    vein_lengths = []
    if history == None:
        history = [[0 for a in range(len(matrix[b]))] for b in range(len(matrix))]

    while len(level)!=0:
        new_finds=vein
        y=level[0][0]
        x=level[0][1]
        for y_bias in range(-1,2):
            y_curr=y+y_bias
            if y_curr<0 or y_curr>=len(matrix):
                continue
            for x_bias in range(-1,2):
                x_curr=x+x_bias
                if x_curr<0 or x_curr>=len(matrix[y]):
                    continue
                level.append([y_curr,x_curr])

                if matrix[y_curr][x_curr]=="Y":
                    if history[y_curr][x_curr] == 0:
                        new_finds+=1
                    else:
                        vein+=new_finds
                else:
                    pass

                print(y_curr,x_curr)
                history[y_curr][x_curr] = 1
        level.pop(0)


    print(history[1:])
    print(len(history)-1)
    return new_finds


def main():
    data1=file_read("input_1.1.txt")
    data1=bfs_search(data1)
    for a in data1:
        print(a)
main()