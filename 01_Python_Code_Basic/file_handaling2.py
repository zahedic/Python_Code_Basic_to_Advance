try:
    list=[10,0,20]
    result=list[0]/list[3]
    print(result)
except ZeroDivisionError:
    print('Divide by Zero is not possible.')

except IndexError:
    print('Index error')
finally:
    print('Print Done')



