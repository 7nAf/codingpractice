from sys import stdin

def heapify(l,f,r):
    left=2*(f+1)-1
    right=2*(f+1)
    hn=(int)(r/2) -1
    if f>hn:
        return
    n=f if l[f]>l[left] else left
    n=n if right >= r or l[n]>l[right] else right

    if n!=f:
        l[f],l[n]=l[n],l[f]
        heapify(l,n,r)
        

def heapsort(l):
    fl=len(l)
    hn=(int)(fl)-1
    while hn>=0:
        heapify(l,hn,len(l))
        hn-=1

    ra=range(fl,0,-1)
    for a in ra:
        l[a-1] , l[0] =l[0],l[a-1]
        heapify(l,0,a-1)
        
    print(l)


if __name__== '__main__':
    l=[7,0,1,6,5,8,-1]
    heapsort(l)

    for line in stdin:
        H = [int(elem) for elem in line.split()]
        heapsort(H)



