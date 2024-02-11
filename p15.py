# # if(exponent<0):
# #     print("Exponent cannot be negative")
# # for i in range(exponent):
# result = base**exponent
# print(result)
def exponent (b, e):
    result = 1
    while e>0:
        result = result*b   
        e= e-1
    print(result)
exponent(5, 4)     
    
        