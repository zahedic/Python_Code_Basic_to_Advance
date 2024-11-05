def insertion_sort(array):
    for i in range(1,len(array)):
        j=i
        while array[j-1]>array[j] and j>0:
            j-=1

array=[]