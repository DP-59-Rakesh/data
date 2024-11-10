'''-------------linear search----------'''

l=[2,3,4,57,1,8,0]
target=8
for i in range(len(l)-1):
    for j in range(len(l)-(i+1)):
        if l[j+1]<l[j]:
            l[j+1],l[j]=l[j],l[j+1]
for i in range(len(l)):
    if  target==l[i]:
        print(i)   



'''-----------Bineary  search---------'''       


# for i in range(len(l))


def bs(l,low,high,target):
    while low<=high:
        mid=(low+high)//2
        if target>l[mid]:
            low=mid+1
        elif target<l[mid]:
            high=mid-1
        else:
            print(mid)
            break
bs(l,0,len(l)-1,8)            
