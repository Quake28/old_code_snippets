#input = open("input.txt", "r")

#lengths = input.readline().split(" ")
arr1_len = 5 #int(lengths[0])
arr2_len = 5 #int(lengths[1]) 

arr1 = [1,3,5,9] #list(map(int, input.readline().split(" ")))
arr2= [6,4,8]#list(map(int, input.readline().split(" ")))

arr1=[1,1,2,2,5]
arr2=[3,1,4,1,5]

arr1_len=len(arr1)
arr2_len=len(arr2)

out = []

for i in range(arr2_len):
    start = 0
    end = arr1_len - 1  
    while True:
        mid = int((start + end)/2)
        if arr1[mid] == arr2[i]:
            status=False
            for mid in range(mid, arr1_len):
                if arr1[mid] > arr2[i] or mid==arr1_len-1:
                    
                    status=True
                    break
            if status:
                out.append(mid+1)
                break
        elif arr1[mid] < arr2[i] and arr1[mid + 1] > arr2[i]:
            out.append(mid)
            break

        elif arr1[mid] < arr2[i]:
            start = mid + 1
            
        elif arr1[mid] > arr2[i]:
            end = mid - 1

        else:
            out.append(mid)
            break
            
print(out)