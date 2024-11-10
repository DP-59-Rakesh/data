'''------------Bubble sort-------------'''


l=[9,8,7,4,2,1,4,5,3]



for i in range(len(l)):
    for j in range(len(l)-(i+1)):
        if l[j+1]<l[j]:
            l[j+1],l[j]=l[j],l[j+1]
print("-----------Bubble sort----------- ")        
print()    
print(l)            
print()


for i in range(len(l)-1,-1,-1):
    for j in range(len(l)-1,(len(l)-(i+2)),-1):
        if l[j]<l[j-1]:
            l[j],l[j-1]=l[j-1],l[j]

print("-----------Reversed Bubble sort---------")
print()
print(l)     
print()       


'''------------selection sort--------------'''
ls=[4,3,1,2]
for i in range(len(ls)):
    mini=i
    for j in range(i+1,len(ls)):
        if ls[j]<ls[mini]:
            mini=j
    if mini!=i:
        ls[mini],ls[i]=ls[i],ls[mini]    
print('---------------selection sort-----------')        
print()
print(ls)
print()



'''-------------Insertion sort-------------'''


for i in range(1,len(l)):
    j=i-1
    key=l[i]
    while j>=0 and key<l[j]:
        l[j+1]=l[j]
        j-=1
    l[j+1]=key
print('-----------Insertion sort-----------')
print()
print(l)        
print()





'''----------------Merge sort------------'''

ll=[4,3,1,2]

def ms(ll,low,high):
    if low<high:
        mid=(low+high)//2
        ms(ll,low,mid)
        ms(ll,mid+1,high)
        merge(ll,low,mid,high)
    return ll
def merge(ll,low,mid,high):
    left=low
    right=mid+1
    temp=[]
    while left<=mid and right<=high:
        if ll[left]<=ll[right]:
            temp.append(ll[left])
            left+=1
        else:
            temp.append(ll[right])
            right+=1
    while left<=mid:
        temp.append(ll[left])
        left+=1
    while right<=high:
        temp.append(ll[right])
        right+=1
    for i in range(low,high+1):
        ll[i]=temp[i-low]
    return ll
r=ms(ll,0,len(ll)-1)
print('----------Merge sort----------')
print()
print(r)
print()



# def cal_sum(n):
#     if n==0:
#         return 0
#     return cal_sum(n-1)+n
# print(cal_sum(5))     

# k=[1,2,3,4]
# def fun(k,i):
#     if i==len(k):
#         return
    
#     print(k[i])     
#     return fun(k,i+1)
# fun(k,0)




# l=[9,8,7,4,2,1,4,5,3]
# low=0
# high=len(l)-1
# def mergeSort(l,low,high):
#     if low<high:
#         mid=(low+high)//2
#         mergeSort(l,low,mid)
#         mergeSort(l,mid+1,high)
#         merge(l,low,mid,high)
#     return l
# def merge(l,low,mid,high):
#     left=low
#     right=mid+1
#     temp=[]
#     while left<=mid and right<=high:
#         if l[left]<=l[right]:
#             temp.append(l[left])
#             left+=1
#         else:
#             temp.append(l[right])
#             right+=1
#     while left<=mid:
#         temp.append(l[left])
#         left+=1
#     while right<=high:
#         temp.append(l[right])
#         right+=1
#     for i in range(low,high+1):
#         l[i]=temp[i-low]
#     return l
# mergeSort(l,low,high)
# print(l)




'''---------------Quick sort-----------------''' 


def quicksort(l,low,high):
    if low < high:
        loc=quick(l,low,high)
        quicksort(l,low,loc-1)
        quicksort(l,loc+1,high)
    return l
def quick(l,low,high):
    start=low
    end=high
    pivot=l[low]
    while True:
        while start<=end and l[start]<=pivot:
            start+=1
        while start<=end and l[end]>pivot:
            end-=1
        if start<=end:
            l[start],l[end]=l[end],l[start]
        else:
            break    
    l[end],l[low]=l[low],l[end]
    return end    
q=quicksort(l,0,len(l)-1)
print('--------quick sort--------')
print()
print(q)
print()