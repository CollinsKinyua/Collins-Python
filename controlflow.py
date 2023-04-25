marks = int(input("Weka alama yako:"))
# programming;is comanding a computer
# if elif else statement
if marks > 80 and marks <= 100:
    print("You scored an A")
elif marks > 60 and marks < 80:
    print("You have a B...")
elif marks > 40 and marks <= 60:
    print("You have a C")
elif marks > 30 and marks <= 40:
    print("You have a D+")
elif marks >=0 and marks <= 30:
    print("You have an F")
else:
    print("Wrong input")

