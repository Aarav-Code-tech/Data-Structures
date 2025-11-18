arr=[2,5,7,1,3]
for i in range(len(arr)):
    a=i
    for j in range(i+1,len(arr)):
        if arr[a]>arr[j]:
            a=j
    arr[i],arr[a]=arr[a],arr[i]
print("Sorted Array :" )
for c in range(len(arr)):
    print("%d"%arr[c],end='')
