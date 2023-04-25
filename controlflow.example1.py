route = int(input("sacco name:"))
route_number = [22, 27, 33, 37, 44, 47, 55, 57, 66, 67, 77, 99]

# if
if route > 77 and route <= 99:
    print("SuperMetro")
elif route > 66 and route <= 77:
    print("Latema")
elif route > 55 and route <= 66:
    print("Lopha")
elif route > 44 and route <= 55:
    print("Ganaki")
elif route > 33 and route <= 44:
     print("Kakose")
elif route > 22 and route <= 33:
     print("Uber")
else:
     print("Unavailable")
