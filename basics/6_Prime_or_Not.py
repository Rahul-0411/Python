num = int(input("Enter the Number : "))

flag = 0
if num < 2:
    flag = 1
else:
    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break

if flag == 1:
    print("Number is Not Prime")
else:
    print("Number is Prime")