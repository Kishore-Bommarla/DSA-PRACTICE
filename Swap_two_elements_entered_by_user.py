arr=[1,2,3,4,5]
i=int(input("Enter first index to swap : "))
j=int(input("Enter second index to swap : "))
if 0<=i<len(arr) and 0<=j<len(arr):
    arr[i],arr[j]=arr[j],arr[i]
print("After swapping an array:",arr)