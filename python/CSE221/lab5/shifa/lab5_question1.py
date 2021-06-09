def lcs(list1,list2):
    x_length=len(list1)
    y_length=len(list2)
    lcs_string=""
    matrix=[[None for aa in range(x_length+1)] for ab in range(y_length+1)]
    for count1 in range(0,x_length+1):
        matrix[0][count1]=0
    for count2 in range(1,y_length+1):
        matrix[count2][0]=0
    for x_pos in range(x_length):
        for y_pos in range(y_length):
            if list1[x_pos]==list2[y_pos]:
                matrix[y_pos+1][x_pos+1]=matrix[y_pos][x_pos]+1
                if len(lcs_string)!=0:
                    if list1[x_pos]!=lcs_string[-1] and x_pos>=y_pos:
                        lcs_string+=list1[x_pos]
                else:
                    lcs_string+=list1[x_pos]
            elif matrix[y_pos][x_pos+1] >= matrix[y_pos+1][x_pos]:
                matrix[y_pos+1][x_pos+1]=matrix[y_pos][x_pos+1]
            else:
                matrix[y_pos+1][x_pos+1] = matrix[y_pos+1][x_pos]
    lcs_len=matrix[-1][-1]
    return lcs_len,lcs_string
list1=input().split()
list2=input().split()
lcsVal,lcsResult=lcs(list1,list2)
print(lcsResult)
print(str(int(lcsVal/len(list1)*100))+"% PASSED")