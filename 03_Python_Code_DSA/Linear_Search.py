def linear_search(array,num,item):
    for i in range(0,num):
        if(array[i]==item):
            return i
    return -1

array=[3,15,22,35,-47,59,-67,74,82,95,100]
num=len(array)
item=int(input('Enter the Number: '))
index=linear_search(array,num,item)
if(index==-1):
    print('Item is not found')
else:
    print(item,'is found at index ',index)