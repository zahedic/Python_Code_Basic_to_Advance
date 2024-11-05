# Build in Polimorphic Function
print(len('ICON COMPUTER TECHNOLOGY'))
print(len([10,20,30,40,50,60,70,80,90,100]))


# User define Polimorphic function
def add(x,y,z=0):
    return x+y+z

def mul(x,y,z=1):
    return x*y*z

print(add(10,20))
print(add(10,20,30))

print(mul(10,20))
print(mul(10,20,30))



