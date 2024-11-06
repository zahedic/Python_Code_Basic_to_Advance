queue=[]
def enqueue():
    element=int(input('Enter the Element'))
    queue.append(element)
    print(element,' is added to queue.')

def dequeue():
    if not queue:
        print('Queue is empty! ')
    else:
        e=queue.pop(0)
        print('Remove element ',e)

def display():
    print(queue)

while True:
    print('Select the Operation 1. Add  2. Remove  3. Show   4. Exit')
    choice=int(input())

    if choice==1:
        enqueue()

    elif choice==2:
        dequeue()

    elif choice==3:
        display()

    elif choice==4:
        break

    else:
        print('Please Enter the Corect Operation.')


