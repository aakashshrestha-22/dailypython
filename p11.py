num = int(input("Enter the number"))
while(num>0):
    digit = num % 10
    num = num//10
    print(digit, end=" ")
# reverse_num = int(str(num)[::-1])
# print(reverse_num, end="")