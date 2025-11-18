def comp(n1,n2):
    str(n1)+str(n2)>str(n2)+str(n1)
def b(nums):
    for i in range(len(nums),0,-1):
        tmp=0
        for j in range(i):
            if not comp(nums[j],nums[tmp]):
                tmp=j
        nums[tmp],nums[i-1]=nums[i-1],nums[tmp]
    return str(int("".join(map(str,nums))))
arr=[7,9,0,5,3]
print(f"Array given-{arr}")
print('largest digit-',b(arr))
    
            
