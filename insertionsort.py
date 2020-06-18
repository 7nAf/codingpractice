def insertionsort(arr):
    for i in range(1,len(arr)):
        print(i)
        if arr[i]<arr[i-1]:
            j=i-1
            temp=arr[i]
            while(j >= 0 and arr[j]>temp):
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=temp
            

if __name__=="__main__":
    arr=[0,2,3,1,4,5]
    for i in arr:
        print(i)
    insertionsort(arr)
    print("hello world")