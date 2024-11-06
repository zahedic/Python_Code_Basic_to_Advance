
def bubble_sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]


if __name__== '__main__':
    num=int(input('Enter the Number: '))
    list=[int(input()) for x in range(num)]

    bubble_sort(list)
    print(list)