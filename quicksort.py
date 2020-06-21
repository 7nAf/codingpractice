def pick(arr,f,r)->(int,list):
    pivot=arr[r]
    i=f
    for j in range(f,r,1):
        if arr[j]<pivot:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            
    arr[i],arr[r]=arr[r],arr[i]
    return (i,arr)

def quicksort(arr,f,r):
    if f >= r:
        return
    n,arr=pick(arr,f,r)
    quicksort(arr,f,n-1)
    quicksort(arr,n+1,r)

if __name__=="__main__":
    arr=[0,2,5,1,4,3]
    quicksort(arr,0,len(arr)-1)
    for i in arr:
        print(i)






