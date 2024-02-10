number = int(input("Enter the number of list:-"))
numList= []
for i in range(number): 
    numList.append(int(input()))
print(numList)

for i in range(len(numList)):
    if((numList[i]%5)==0):
        print(numList[i])
