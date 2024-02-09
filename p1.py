def calculate(num1, num2):
    product = num1*num2
    if(product<1000):
        return product
    else:
        return num1+num2
a= int(input("Enter first number:-"))
b= int(input("Enter Second number:-"))

result = calculate(a, b)
print("The Result is",result)
#It calculates the number: if product is less than 1000 it will return multiplied value if not then it will return add
