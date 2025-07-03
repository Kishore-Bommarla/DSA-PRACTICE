arr=[10,20,30,40,50,60]
for i in range(0,len(arr)-1,2):
    arr[i],arr[i+1]=arr[i+1],arr[i]
print("after swapping ",arr)