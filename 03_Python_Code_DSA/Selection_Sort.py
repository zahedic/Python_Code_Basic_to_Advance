
'''
--------------1st Step ------------
list = [30,80,60,50,-80,10,90,20,50,40]
print(list)
min_val=min(list)
print(min_val)
--------------2nd  Step ------------
list = [30,80,60,50,-80,10,-90,20,50,40]
print(list)
min_val=min(list)
min_index=list.index(min_val)
print(min_index)
--------------3rd   Step ------------
list = [30,80,60,50,-80,10,90,20,50,40]
print(list)

min_val=min(list)
min_index=list.index(min_val)
list[0],list[min_index]=list[min_index],list[0]
print(list)

--------------4th Step ------------
list = [30,80,60,50,-80,10,90,20,50,40]
print(list)

for i in range(len(list)):
    min_val=min(list[i:])
    min_index=list.index(min_val)
    list[i],list[min_index]=list[min_index],list[i]
print(list)
-------------5th Step ------------
def selection_sort(list):
    for i in range(len(list)):
        min_val=min(list[i:])
        min_index=list.index(min_val)
        list[i],list[min_index]=list[min_index],list[i]

if __name__=='__main__':
    list = [30,80,60,50,-80,10,90,20,50,40]
    print(list)

    selection_sort(list)
    print(list)

--------------6th Step ------------

def selection_sort(list):
    for i in range(len(list)):
        min_val=min(list[i:])
        min_index=list.index(min_val)
        if list[i]!=list[min_index]:
            list[i],list[min_index]=list[min_index],list[i]

if __name__=='__main__':
    list = [30,80,60,50,-80,10,90,20,50,40]
    print(list)

    selection_sort(list)
    print(list)

--------------7th Step ------------


def selection_sort(list):
    for i in range(len(list)-1):
        min_index=i

        for j in range(i+1,len(list)):
            if list[j]<list[min_index]:
                min_index=j

        #min_val=min(list[i:])
        #min_index=list.index(min_val)

        if list[i]!=list[min_index]:
            list[i],list[min_index]=list[min_index],list[i]

if __name__=='__main__':
    list = [30,80,60,50,-80,10,90,20,50,40]
    print(list)

    selection_sort(list)
    print(list)

--------------8th Step ------------

def selection_sort(list):
    for i in range(len(list)-1):
        min_index=i

        for j in range(i+1,len(list)):
            if list[j]<list[min_index]:
                min_index=j

        #min_val=min(list[i:])
        #min_index=list.index(min_val)

        if list[i]!=list[min_index]:
            list[i],list[min_index]=list[min_index],list[i]

if __name__=='__main__':
    num = int(input('Enter the Number: '))
    list=[int(input()) for x in range(num)]
    print(list)


    selection_sort(list)
    print(list)


'''



def selection_sort(list):
    for i in range(len(list)-1):
        min_index=i

        for j in range(i+1,len(list)):
            if list[j]<list[min_index]:
                min_index=j

        #min_val=min(list[i:])
        #min_index=list.index(min_val)


        if list[i]!=list[min_index]:
            list[i],list[min_index]=list[min_index],list[i]



if __name__=='__main__':
    num=int(input('How many number do you want? : '))
    list = [int(input()) for x in range(num)]
    print(list)
    selection_sort(list)
    print(list)









