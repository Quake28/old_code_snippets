def search(arr1,arr2):
    result=[]

    for searchItem in arr2:
        start=0
        end=len(arr1)
        while True:
            mid=int((end-start)/2)+start
            if arr1[mid]==searchItem:
                if mid==len(arr1)-1 or arr1[mid+1]!=searchItem:
                    result.append(mid+1)
                    break
                else:
                    start=mid+1
            elif mid<len(arr1)-1:
                if arr1[mid]<searchItem and arr1[mid+1]>searchItem:
                    result.append(mid+1)
                    break
                elif arr1[mid]>searchItem:
                    if mid==0:
                        result.append(mid+1)
                        break
                    end=mid
                elif arr1[mid]<searchItem:
                    start=mid
                    
            else:
                result.append(mid+1)
                break
            # if mid==0:
            #     if arr1[mid]<searchItem and arr1[mid+1]>searchItem:
            #         result.append(mid)
            #         break
            #     else:
            #         start+=1
            # elif mid==len(arr1)-1:
            #     if arr1[mid]==searchItem:
            #         result.append(mid+1)
            #         break
            #     elif arr1[mid-1]<searchItem and arr1[mid]>searchItem:
            #         result.append(mid)
            #         break
            # elif arr1[mid]<searchItem:
            #     start=mid+1
            # elif arr1[mid]>searchItem:
            #     end=mid
            # else:
            #     if arr1[mid+1]==searchItem:
            #         start+=1
            #     else:
            #         result.append(mid+1)
            #         break
    return result

if __name__=="__main__":
    readFile=open("input.txt","r")
    readFile.readline().split()
    arr1=readFile.readline().split()
    arr2=readFile.readline().split()
    readFile.close()
    arr1=[int(a) for a in arr1]
    arr2=[int(a) for a in arr2]
    result_arr=search(arr1,arr2)
    writeFile=open("output.txt","w")
    for a in result_arr:
        writeFile.write("{} ".format(a))
    writeFile.close()