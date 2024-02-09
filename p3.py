value = input("Enter your string:")
print("Original String is:",value)
print("Printing only even index chars:-")
# arrValue= list(value)
# arrValue = (char for char in value)
for i in range (len(value)):
    if i %2==0:
        print(value[i])