num = int(input("Enter the Number "))

remain = 0
divd = 0

while(num > 0):
    remain = num % 10
    divd = remain + (divd * 10)
    num = num // 10

print(divd)