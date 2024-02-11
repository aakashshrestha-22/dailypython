def palindrome(number):
    original= number
    rev_num = 0
    while(number>0):
        rem = number %10
        rev_num = (rev_num*10)+rem
        number = number //10
    if(original == rev_num):
        print("Palindrome")
    else:
        print("Not a palindrome")
num = int(input("Enter the number"))
palindrome(num)