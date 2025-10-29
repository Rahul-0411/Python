Start_Y = int(input("Enter the Year : "))
End_Y = int(input("Enter the Year : "))
# list_Y = 

for i in range(Start_Y, End_Y + 1):
    if ((i % 4 == 0) and (i != 0)) or (i % 400 == 0):
        print(i)