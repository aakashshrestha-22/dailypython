# checking if the last number 
# and first number of list is same or not 
# def checkNumber(numberList):
#     firstNum = numberList[0]
#     lastNum = numberList[-1]
#     if(firstNum == lastNum):
#         return True
#     else:
#         return False
# number = int(input("Enter the total number of list you want:"))
# listNum=[]
# for i in range(number):
#     listNum.append(int(input()))
# print("result is",checkNumber(listNum))
def checkNumber(numberList):
    return numberList[0] == numberList[-1]
number = int(input("Enter the total number of lists you want: "))
for i in range(number):
    num = int(input("Enter a number: "))
    if i == 0:  # For the first number, just store it in firstNum
        firstNum = num
    if i == number - 1:  # For the last number, check equality with firstNum
        result = num == firstNum

print("Result is", result)