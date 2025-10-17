start = int(input("Enter the Start : "))
end = int(input("Enter the End : "))

for num in range(start, end+1):
    if num < 2:
        flag = 1
        continue

    else:
        flag = 0
        for i in range(2,num):
            if num % i == 0:
                flag = 1
                break

        if flag != 1:
            print(num)
