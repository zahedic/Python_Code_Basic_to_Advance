try:
    num1=int(input('Enter the Number:  '))
    num2=int(input('Enter the Number:  '))
    result=num1/num2
    print(result)
except ZeroDivisionError:
    print('Divide by Zero is not possible.')
except ValueError:
    print('You data input is not corect ')

print('Finished')

