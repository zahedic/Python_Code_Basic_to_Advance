Bangla = int(input("Enter Your Bangla Marks:"))
English = int(input("Enter Your English Marks:"))
Math = int(input("Enter Your Math Marks:"))
Physics = int(input("Enter Your Physics Marks:"))
Chemistry = int(input("Enter Your Chemistry Marks:"))
Average= (Bangla+English+Math+Physics+Chemistry)/5
if Average>100:
    print("Wrong Data")
elif Average>= 80:
    print("Your Grade is A+")
elif Average>= 70:
    print("Your Grade is A")
elif Average>= 60:
    print("Your Grade is A-")
elif Average >= 50:
    print("Your Grade is B")
elif Average >= 40:
    print("Your Grade is C")
elif Average >= 33:
    print("Your Grade is D")
else:
    print("Your Grade is F")