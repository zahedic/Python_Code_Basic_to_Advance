def Binary_Search(array,item,left,right):
    while left<=right:
        mid=left+(right-left)//2

        if array[mid]==item:
            return mid

        elif array[mid]<item:
            left=mid+1

        else:
            right=mid-1

    return -1

array=[3,7,9,15,29,30,45,65,78,99,100]
item=int(input('Enter the Number: '))
result=Binary_Search(array,item,0,len(array)-1)
if(result!=-1):
    print('Element is Present at index ',result)
else:
    print('Element is not Present at index')



