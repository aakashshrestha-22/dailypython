string = input("Enter your string:-")
removeNum= int(input("Enter the number"))
lenString = len(string)
if(removeNum< lenString):
    finalString= string[removeNum:lenString]
    print(finalString)
    
else:
    print("Cannot remove")