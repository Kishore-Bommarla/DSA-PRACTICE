arr=[10,20,30,40]
temp=arr[0]
arr[0]=arr[-1]
arr[-1]=temp
print(arr)