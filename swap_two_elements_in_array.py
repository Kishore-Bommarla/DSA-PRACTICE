arr=[5,8,2,9]
temp=arr[1]
arr[1]=arr[3]
arr[3]=temp
print(arr)


                                                 #OR

arr=[5,8,2,9]
arr[1],arr[3]=arr[3],arr[1]
print(arr)