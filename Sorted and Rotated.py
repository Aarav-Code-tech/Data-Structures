arr=[7,8,9,10,11]
n=len(arr)
count=0
for i in range(1,n):
    if arr[i-1]>arr[i]:
        count+=1
if arr[n-1]>arr[0]:
    count+=1
print(count<=1)
