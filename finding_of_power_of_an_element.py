def findPowerofElement(a,n):
    if n==1:
        return a
    elif n==0:
        return 1
    else:
        mid=n//2
        b=findPowerofElement(a,mid)
        result=b*b
        if n%2 == 0:
            return result
        return result*a
a=2
n=16
result=findPowerofElement(a,n)
print(result)