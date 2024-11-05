Stack=[]
def push():
    if len(Stack)==num:
        print('Stack is Full')
    else:
        elements=int(input('Enter the Element. '))
        Stack.append(elements)
        print(Stack)

def pop():
    if not Stack:
        print('Stack is Empty!')
    else:
        e=Stack.pop()
        print('Remove the Element',e)
        print(Stack)

def display():
    print(Stack)
num=int(input('How many Stack do you need? : '))
while True:
    print('Select the Correct Operation 1. Push     2. Pop     3. Show    4. Quite')
    choice=int(input())

    if choice==1:
        push()

    elif choice==2:
        pop()

    elif choice==3:
        display()

    elif choice==4:
        break

    else:
        print('Enter the Correct Operation.')





















