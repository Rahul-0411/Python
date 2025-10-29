num = int(input("Enter the Number : "))

orignal = num
digit = 0
sum = 0


while(num > 0):
    digit = num % 10
    sum += digit * digit * digit 
    num = num // 10

if sum == orignal:
    print("Number is Armstrong ")
else:
    print("Number is not Armstrong ")