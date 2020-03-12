arr = [2,7,3,4,1,9,8]
target = int(input())
flag =0
for i in range(len(arr)):
    a = arr[i]
    for j in arr[i:]:
        if(a+j==target):
            print(a,j)
            flag = 1
            break
    if (flag==1):
        break




            
    
            
    
