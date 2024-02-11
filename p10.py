num = int(input("Enter the number of elements:"))
list1=[int(input("Enter the list1")) for _ in range(num)]
print("The list 1 is:",list1)
list2=[int(input("Enter the list2")) for _ in range(num)]
print("The list2 is:",list2)
newArr=[]
for i in list1:
    if(i%2!=0):
        newArr.append(i)
for i in list2:
    if(i%2!=0):
        newArr.append(i)
        
print(newArr) 