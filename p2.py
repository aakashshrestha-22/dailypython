print("Printing Current and Previous number sum in a range(10)")
previousNumber= 0

for i in range(1,11):
    sum = previousNumber + i
    
    print(" Current number", i, "previous number",previousNumber,"sum:",sum)
    previousNumber = i