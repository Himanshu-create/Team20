"""
- Given an array of integers, return indices of the two numbers such that they add up to a specific target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

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




            
    
            
    
