num = int(input("Enter the height of pyramid"))
# while(num>1):
#     for i in range(num):
#         print("*", end=" ")
#     print()
#     num = num-1
#for single to many
# for i in range(1,num+1):
#     for j in range(i):
#         print("*",end=" ")
#         j = j+1
#     print()
#for triangular 
max_width = num + num-1
for i in range(num):
    num_spaces = max_width//2-i
    print(" "* num_spaces, end=" ")
    print("* "*(i+1))