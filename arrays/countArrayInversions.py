#code
def merge(x,y):
    ans=0
    arr=[]
    i=j=0
    n1=len(x)
    n2=len(y)
    while i<n1 and j<n2:
        if x[i]<=y[j]:
            arr.append(x[i])
            i+=1
        else:
            ans+=n1-i
            arr.append(y[j])
            j+=1
    while i<n1:
        arr.append(x[i])
        i+=1
    while j<n2:
        arr.append(y[j])
        j+=1
    #print(ans)
    return ans, arr
    
def mergesort(arr):
    a=b=c=0
    if len(arr)==1:
        return 0, arr
    mid=len(arr)//2
    a, arr1= mergesort(arr[:mid])
    b, arr2=mergesort(arr[mid: ])
    c, arr3= merge(arr1, arr2)
    return a+b+c, arr3
    
for _ in range(int(input())):
    n=int(input())
    l=list(map(int, input().split()))
    m, arr=mergesort(l)
    print(m)
    #print(arr)
