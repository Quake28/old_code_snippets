def lcs(list1,list2):
    x_length=len(list1)
    y_length=len(list2)
    matrix=[[None for aa in range(x_length+1)] for ab in range(y_length+1)]
    lcs_string=""
    for count1 in range(0,x_length+1):
        matrix[0][count1]=0
    for count2 in range(1,y_length+1):
        matrix[count2][0]=0
    for x_pos in range(x_length):
        for y_pos in range(y_length):
            if list1[x_pos]==list2[y_pos]:
                matrix[y_pos+1][x_pos+1]=matrix[y_pos][x_pos]+1
                if len(lcs_string)!=0:
                    if list1[x_pos]!=lcs_string[-1] and x_pos<=y_pos:
                        lcs_string+=list1[x_pos]
                else:
                    lcs_string+=list1[x_pos]
            elif matrix[y_pos][x_pos+1] >= matrix[y_pos+1][x_pos]:
                matrix[y_pos+1][x_pos+1]=matrix[y_pos][x_pos+1]
            else:
                matrix[y_pos+1][x_pos+1] = matrix[y_pos+1][x_pos]
    return lcs_string
if __name__=="__main__":
    list1=input().split()
    list2=input().split()
    lcs_string=lcs(list1,list2)
    print(len(lcs_string))
    list1={"A":"are","B":"because","C":"coats","D":"doctors","E":"evolution","M":"monkeys","O":"of","P":"eruption","R":"results","W":"wearing"}
    for a in lcs_string:
        print(list1[a], end=" ")